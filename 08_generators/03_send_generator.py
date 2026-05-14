# ============================================================
#         GENERATOR WITH .send() METHOD
# ============================================================
# Normal generators use next() to get values OUT of a generator.
# But .send() lets you push values INTO a generator while it runs.
#
# Think of it like a tea stall worker:
#   - Worker greets you → PAUSES and waits for your order
#   - You SEND your order → Worker prepares it → PAUSES again
#   - You SEND next order → Worker prepares it → PAUSES again
#   - This continues forever (while True) until you close the stall
# ============================================================

def chai_customer():
    print("Welcome ! What chai would you like ?")
    order = yield          # PAUSE POINT 1: waits to receive first order via .send()
    while True:
        print(f"Preparing: {order}")
        order = yield      # PAUSE POINT 2: prints order, then waits for next .send()


# ── Step 1: Create the generator (worker is hired but NOT started yet) ──
stall = chai_customer()

# ── Step 2: next() STARTS the generator ─────────────────────────────────
# Runs the function until the FIRST yield → prints welcome message → PAUSES
# ⚠️ This line is REQUIRED before any .send() call
# If you comment this out, .send() will crash with:
#   TypeError: can't send non-None value to a just-started generator
# Because there is no active yield to receive the value yet.
next(stall)   # Output: Welcome ! What chai would you like ?

# ── Step 3: .send() resumes the generator AND passes a value into yield ──
stall.send("Masala Chai")   # order = "Masala Chai" → Output: Preparing: Masala Chai
stall.send("Lemon Chai")    # order = "Lemon Chai"  → Output: Preparing: Lemon Chai

# ============================================================
# EXPECTED OUTPUT:
# Welcome ! What chai would you like ?
# Preparing: Masala Chai
# Preparing: Lemon Chai
# ============================================================

# ============================================================
# HOW next() vs .send() WORK:
# ============================================================
#   next(gen)         → resumes the generator, passes None into yield
#   gen.send(value)   → resumes the generator, passes 'value' into yield
#
#   Both advance the generator to the NEXT yield and then PAUSE again.
# ============================================================

# ============================================================
# WHY while True IS INTENTIONAL (not a bug!):
# ============================================================
# The while True loop keeps the worker alive forever.
# The generator PAUSES at each yield — it does NOT spin endlessly.
# It only moves forward when you call next() or .send().
# To stop it, call: stall.close()
# ============================================================

# ============================================================
# STEP-BY-STEP EXECUTION TRACE:
# ============================================================
#
#  stall = chai_customer()
#    → Generator created. Function body NOT executed yet.
#
#  next(stall)
#    → Enters function → prints "Welcome ! What chai would you like ?"
#    → Hits: order = yield  → PAUSES here (PAUSE POINT 1)
#
#  stall.send("Masala Chai")
#    → Resumes from PAUSE POINT 1
#    → order = "Masala Chai"
#    → Enters while True loop
#    → Prints "Preparing: Masala Chai"
#    → Hits: order = yield  → PAUSES here (PAUSE POINT 2)
#
#  stall.send("Lemon Chai")
#    → Resumes from PAUSE POINT 2
#    → order = "Lemon Chai"
#    → Prints "Preparing: Lemon Chai"
#    → Hits: order = yield  → PAUSES again (PAUSE POINT 2)
#
# ============================================================

# ============================================================
# PRACTICAL REAL-WORLD USES OF .send() GENERATORS:
# ============================================================
#
#  1. Live order processing systems (like this chai stall)
#  2. Running total / accumulator without restarting the function
#  3. Chatbots / interactive CLI tools
#  4. Data pipelines — feed data one chunk at a time
#  5. Foundation of Python's async/await (coroutines)
#
# Example — running total accumulator:
#
#   def running_total():
#       total = 0
#       while True:
#           amount = yield total   # receive amount, send back total
#           total += amount
#
#   counter = running_total()
#   next(counter)
#   print(counter.send(30))   # 30
#   print(counter.send(50))   # 80
#   print(counter.send(20))   # 100
# ============================================================
