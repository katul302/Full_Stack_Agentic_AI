# ============================================================
#         GENERATOR EXPRESSIONS IN PYTHON
# ============================================================
# A Generator is like a LAZY WAITER at a restaurant.
#
# 🍽️  Normal waiter (List):
#     Goes to the kitchen, brings ALL dishes at once,
#     puts them all on the table — uses a LOT of space!
#
# 🍽️  Lazy waiter (Generator):
#     Brings ONE dish at a time, only when you ask for it.
#     Saves space, saves time — especially for large orders!
#
# In Python terms:
#   List comprehension  → stores ALL values in memory at once
#   Generator expression → produces ONE value at a time, on demand
# ============================================================


# ============================================================
# YOUR ORIGINAL CODE (with explanations added)
# ============================================================

daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]
# These are cups of tea sold each day for 8 days

# ── Generator Expression ──────────────────────────────────
# Uses ( ) round brackets
# Does NOT compute or store values yet — it's just a "plan"
# Values are produced ONE AT A TIME when you ask for them
total_cups = (sale for sale in daily_sales if sale > 5)

# ── List Comprehension ────────────────────────────────────
# Uses [ ] square brackets
# Computes and stores ALL matching values in memory RIGHT NOW
total_cups1 = [sale for sale in daily_sales if sale > 5]

# ── Generator directly inside sum() ──────────────────────
# Most memory-efficient way to sum filtered values
# No intermediate list is created at all!
total_cups2 = sum(sale for sale in daily_sales if sale > 5)

print("Generator object:", total_cups)    # just shows the object, not values
print("List result:     ", total_cups1)   # shows all values
print("Sum result:      ", total_cups2)   # shows the total


# ============================================================
# UNDERSTANDING GENERATORS DEEPER
# ============================================================

print("\n" + "=" * 50)
print("HOW GENERATORS WORK — STEP BY STEP")
print("=" * 50)

daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]

# Create a generator
gen = (sale for sale in daily_sales if sale > 5)

# Use next() to get ONE value at a time — like calling the lazy waiter
print("First value: ", next(gen))   # 10
print("Second value:", next(gen))   # 12
print("Third value: ", next(gen))   # 8  (7 and 3 are skipped — they're ≤ 5)

# You can also loop through a generator (it picks up from where it left off)
print("\nRemaining values from the generator:")
for sale in gen:
    print(" -", sale)

# ⚠️ Once a generator is exhausted (all values used), it's EMPTY
# Trying to call next() again will raise StopIteration error


# ============================================================
# GENERATOR vs LIST — MEMORY COMPARISON
# ============================================================

print("\n" + "=" * 50)
print("GENERATOR vs LIST — MEMORY USAGE")
print("=" * 50)

import sys

# Imagine 1 million sales records
big_sales = range(1_000_000)

# List comprehension — stores ALL 1 million numbers in memory
list_version = [sale for sale in big_sales]

# Generator expression — stores NOTHING, produces on demand
gen_version = (sale for sale in big_sales)

print(f"List size in memory:      {sys.getsizeof(list_version):,} bytes")
print(f"Generator size in memory: {sys.getsizeof(gen_version):,} bytes")
print("→ Generator uses MUCH less memory!")


# ============================================================
# PRACTICAL EXAMPLE — TEA SHOP DAILY REPORT
# ============================================================

print("\n" + "=" * 50)
print("PRACTICAL EXAMPLE — TEA SHOP REPORT")
print("=" * 50)

weekly_sales = [3, 15, 22, 8, 5, 30, 18]
# Cups sold each day: Mon to Sun

# 1. Find days where sales were above 10 (using generator + list)
high_sales_days = list(sale for sale in weekly_sales if sale > 10)
print("High sales days (>10 cups):", high_sales_days)

# 2. Total cups sold on high-sales days (generator directly in sum)
total_high = sum(sale for sale in weekly_sales if sale > 10)
print("Total cups on high-sales days:", total_high)

# 3. Average cups per day (generator in sum, then divide)
average = sum(weekly_sales) / len(weekly_sales)
print(f"Average cups per day: {average:.1f}")

# 4. Check if ANY day had more than 25 cups (generator with any())
had_great_day = any(sale > 25 for sale in weekly_sales)
print("Had at least one great day (>25 cups)?", had_great_day)

# 5. Check if ALL days had at least 3 cups (generator with all())
always_open = all(sale >= 3 for sale in weekly_sales)
print("Sold at least 3 cups every day?", always_open)

# 6. Find the maximum sales day
best_day = max(weekly_sales)
print("Best day sales:", best_day, "cups")


# ============================================================
# WHEN TO USE WHAT?
# ============================================================

print("\n" + "=" * 50)
print("WHEN TO USE WHAT?")
print("=" * 50)
print("""
  Use LIST comprehension [ ] when:
    ✅ You need to access items by index (e.g., result[0])
    ✅ You need to reuse the result multiple times
    ✅ The data is small enough to fit in memory
    ✅ You need to know the length (len())

  Use GENERATOR expression ( ) when:
    ✅ You only need to loop through results ONCE
    ✅ You're working with large or infinite data
    ✅ You're passing directly into sum(), any(), all(), max(), min()
    ✅ You want to save memory

  Quick rule of thumb:
    → Need the full list?        Use [ ]
    → Just processing/summing?   Use ( )
""")


# ============================================================
# SUMMARY
# ============================================================
print("=" * 50)
print("SUMMARY")
print("=" * 50)
print("""
  Syntax comparison:
    List comprehension:      [x for x in data if condition]
    Generator expression:    (x for x in data if condition)

  Key difference:
    List      → Computes everything NOW, stores in memory
    Generator → Computes ONE item at a time, only when needed

  Works great with built-in functions:
    sum(x for x in data)
    any(x > 5 for x in data)
    all(x > 0 for x in data)
    max(x for x in data)
    min(x for x in data)
""")
