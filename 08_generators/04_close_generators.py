# ============================================================
#         CLOSING A GENERATOR — gen.close()
# ============================================================
# When you're done with a generator, you should CLOSE it.
#
# Think of it like a tea stall:
#   - You open the stall (create generator)
#   - Customers place orders (send values)
#   - At the end of the day, you CLOSE the stall (gen.close())
#   - After closing, no more orders can be taken
#
# What does .close() do internally?
#   → It throws a special exception called GeneratorExit
#     INSIDE the generator at the point where it is paused (yield).
#   → The generator catches it silently and shuts down cleanly.
#   → After .close(), the generator is EXHAUSTED — cannot be used again.
# ============================================================


# ============================================================
# EXAMPLE 1: Basic .close() usage
# ============================================================

print("=" * 50)
print("EXAMPLE 1: Basic close()")
print("=" * 50)

def chai_stall():
    print("🍵 Stall is OPEN!")
    while True:
        order = yield
        print(f"  Preparing: {order}")

stall = chai_stall()
next(stall)                    # Start the generator

stall.send("Masala Chai")      # Output: Preparing: Masala Chai
stall.send("Green Tea")        # Output: Preparing: Green Tea

stall.close()                  # ✅ Stall is now CLOSED
print("🔒 Stall is CLOSED for the day!")

# Trying to use the generator after closing raises StopIteration:
# stall.send("Lemon Tea")  ← This would raise: StopIteration


# ============================================================
# EXAMPLE 2: Detecting when generator is closed using try/finally
# ============================================================

print("\n" + "=" * 50)
print("EXAMPLE 2: Detecting close with try/finally")
print("=" * 50)

def chai_stall_with_cleanup():
    print("🍵 Stall is OPEN!")
    try:
        while True:
            order = yield
            print(f"  Preparing: {order}")
    except GeneratorExit:
        # This block runs when .close() is called
        print("🧹 Cleaning up the stall... washing cups, turning off stove.")
    finally:
        # finally ALWAYS runs — whether closed normally or due to an error
        print("🔒 Stall officially CLOSED. Goodbye!")

stall2 = chai_stall_with_cleanup()
next(stall2)

stall2.send("Elaichi Chai")
stall2.send("Ginger Tea")

stall2.close()   # Triggers GeneratorExit inside the generator


# ============================================================
# EXAMPLE 3: Generator auto-closes when it runs out of values
# ============================================================

print("\n" + "=" * 50)
print("EXAMPLE 3: Auto-close when generator is exhausted")
print("=" * 50)

def limited_orders(menu):
    """A generator that only serves items from a fixed menu"""
    for item in menu:
        print(f"  Serving: {item}")
        yield item
    print("  ✅ All items served — generator done!")
    # Generator ends naturally here → auto-closes (raises StopIteration)

today_menu = ["Masala Chai", "Green Tea", "Lemon Tea"]
order_gen = limited_orders(today_menu)

for order in order_gen:
    pass   # loop handles StopIteration automatically

# Generator is now exhausted — calling next() would raise StopIteration
# order_gen.close() is safe to call even on an exhausted generator (no error)
order_gen.close()
print("  Generator closed (was already exhausted).")


# ============================================================
# EXAMPLE 4: Checking generator state after close
# ============================================================

print("\n" + "=" * 50)
print("EXAMPLE 4: Generator state after close()")
print("=" * 50)

from inspect import getgeneratorstate

def simple_gen():
    yield 1
    yield 2
    yield 3

g = simple_gen()
print("State after creation:    ", getgeneratorstate(g))   # GEN_CREATED

next(g)
print("State after first next():", getgeneratorstate(g))   # GEN_SUSPENDED

g.close()
print("State after close():     ", getgeneratorstate(g))   # GEN_CLOSED

# Trying to call next() on a closed generator:
try:
    next(g)
except StopIteration:
    print("⚠️  Cannot use a closed generator — StopIteration raised!")


# ============================================================
# EXAMPLE 5: Real-world use — file reader that cleans up on close
# ============================================================

print("\n" + "=" * 50)
print("EXAMPLE 5: Real-world — resource cleanup on close")
print("=" * 50)

def tea_log_reader(log_data):
    """
    Simulates reading log entries one at a time.
    Cleans up resources when closed.
    """
    print("📂 Opening log file...")
    try:
        for entry in log_data:
            yield entry
    except GeneratorExit:
        print("🛑 Reader closed early — cleanup done!")
    finally:
        print("📂 Log file closed.")

# Simulated log data
logs = ["Order: Masala Chai", "Order: Green Tea", "Order: Lemon Tea",
        "Order: Ginger Tea", "Order: Iced Tea"]

reader = tea_log_reader(logs)

# Read only first 2 entries, then close early
print(next(reader))   # Order: Masala Chai
print(next(reader))   # Order: Green Tea

reader.close()        # Close before reading all entries — cleanup still runs!


# ============================================================
# SUMMARY
# ============================================================

print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)
print("""
  gen.close()  →  Shuts down a generator cleanly

  What happens internally:
    1. Python throws GeneratorExit at the yield where gen is paused
    2. Generator can catch it with: except GeneratorExit
    3. finally block ALWAYS runs (great for cleanup)
    4. Generator state becomes GEN_CLOSED

  Generator states (from inspect module):
    GEN_CREATED    → created but next() not called yet
    GEN_RUNNING    → currently executing
    GEN_SUSPENDED  → paused at a yield (waiting)
    GEN_CLOSED     → finished or .close() was called

  Best practices:
    ✅ Use try/finally inside generator for cleanup (files, DB connections)
    ✅ Call .close() when you're done — especially for infinite generators
    ✅ .close() on an already-closed generator is safe (no error)
    ❌ Don't try to send/next after closing — raises StopIteration
""")
