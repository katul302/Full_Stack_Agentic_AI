# ============================================================
#         PYTHON DATA TYPES - FOR COMPLETE BEGINNERS
#         Covers: List, Tuple, Dictionary, Set
# ============================================================
# Think of Python data types like different kinds of containers
# in your kitchen — each one has a specific purpose!
# ============================================================


# ============================================================
# 1. LIST  📋
# ============================================================
# A LIST is like a shopping list written on paper.
# - You can ADD items
# - You can REMOVE items
# - You can CHANGE items
# - Items stay in the ORDER you added them
# - You CAN have DUPLICATE items
# - Uses square brackets [ ]

print("=" * 50)
print("1. LIST EXAMPLE")
print("=" * 50)

# Creating a list of teas
tea_menu = ["Masala Chai", "Green Tea", "Lemon Tea", "Masala Chai"]
#            index 0          index 1      index 2      index 3
# Note: "Masala Chai" appears twice — lists allow duplicates!

print("Our tea menu:", tea_menu)

# Accessing items by position (index starts at 0)
print("First tea:", tea_menu[0])       # Masala Chai
print("Second tea:", tea_menu[1])      # Green Tea
print("Last tea:", tea_menu[-1])       # Masala Chai (use -1 for last item)

# Adding an item
tea_menu.append("Ginger Tea")
print("After adding Ginger Tea:", tea_menu)

# Removing an item
tea_menu.remove("Lemon Tea")
print("After removing Lemon Tea:", tea_menu)

# Changing an item
tea_menu[1] = "Iced Tea"
print("After changing index 1 to Iced Tea:", tea_menu)

# Looping through a list
print("\nAll teas on the menu:")
for tea in tea_menu:
    print(" -", tea)

# Useful list info
print("\nTotal teas:", len(tea_menu))
print("Is 'Green Tea' in menu?", "Green Tea" in tea_menu)
print("Is 'Iced Tea' in menu?", "Iced Tea" in tea_menu)

# ✅ Use a LIST when:
#    - Order matters
#    - You need to add/remove/change items
#    - Duplicates are okay


# ============================================================
# 2. TUPLE  🔒
# ============================================================
# A TUPLE is like a printed receipt — it's FIXED and cannot be changed.
# - You CANNOT add, remove, or change items after creation
# - Items stay in ORDER
# - You CAN have DUPLICATE items
# - Uses round brackets ( )

print("\n" + "=" * 50)
print("2. TUPLE EXAMPLE")
print("=" * 50)

# Creating a tuple — these GPS coordinates should never change!
shop_location = (28.6139, 77.2090)   # (latitude, longitude)
print("Shop location (lat, lon):", shop_location)

# Accessing items (same as list, using index)
print("Latitude:", shop_location[0])
print("Longitude:", shop_location[1])

# Another example — days of the week never change!
days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("\nDays of the week:", days_of_week)
print("First day:", days_of_week[0])
print("Last day:", days_of_week[-1])

# Trying to change a tuple will cause an ERROR:
# shop_location[0] = 99.99   ← This will crash! Tuples are immutable.

# Looping through a tuple (same as list)
print("\nWorking days:")
for day in days_of_week[:5]:   # first 5 days
    print(" -", day)

# Useful tuple info
print("\nNumber of days:", len(days_of_week))
print("Is 'Monday' in days?", "Monday" in days_of_week)

# ✅ Use a TUPLE when:
#    - Data should NEVER change (e.g., coordinates, config values)
#    - You want to protect data from accidental modification
#    - Slightly faster than lists


# ============================================================
# 3. DICTIONARY  📖
# ============================================================
# A DICTIONARY is like a real dictionary or a contact book.
# - Every item has a KEY (the word) and a VALUE (the meaning/info)
# - You look up items by KEY, not by position
# - Keys must be UNIQUE (no duplicate keys)
# - Values CAN be duplicated
# - Uses curly brackets { } with key: value pairs

print("\n" + "=" * 50)
print("3. DICTIONARY EXAMPLE")
print("=" * 50)

# Creating a dictionary — a tea menu with prices
tea_prices = {
    "Masala Chai": 30,
    "Green Tea":   25,
    "Lemon Tea":   20,
    "Ginger Tea":  35,
}

print("Tea prices:", tea_prices)

# Accessing a value using its key
print("Price of Masala Chai: ₹", tea_prices["Masala Chai"])
print("Price of Green Tea: ₹", tea_prices["Green Tea"])

# Adding a new key-value pair
tea_prices["Iced Tea"] = 40
print("After adding Iced Tea:", tea_prices)

# Updating an existing value
tea_prices["Green Tea"] = 28
print("After updating Green Tea price:", tea_prices)

# Removing a key-value pair
del tea_prices["Lemon Tea"]
print("After removing Lemon Tea:", tea_prices)

# Looping through a dictionary
print("\nFull tea menu with prices:")
for tea, price in tea_prices.items():
    print(f"  {tea}: ₹{price}")

# Getting just keys or just values
print("\nTea names:", list(tea_prices.keys()))
print("Prices:", list(tea_prices.values()))

# Safe way to access a key (won't crash if key doesn't exist)
price = tea_prices.get("Black Tea", "Not available")
print("\nPrice of Black Tea:", price)

# ✅ Use a DICTIONARY when:
#    - You want to label your data (name → value)
#    - You need fast lookup by a specific key
#    - Examples: contact book, product catalog, student grades


# ============================================================
# 4. SET  🎯
# ============================================================
# A SET is like a bag of unique marbles.
# - NO DUPLICATES allowed — automatically removes them!
# - Items have NO ORDER (you can't access by index)
# - Great for finding unique items or comparing groups
# - Uses curly brackets { } but WITHOUT key: value pairs

print("\n" + "=" * 50)
print("4. SET EXAMPLE")
print("=" * 50)

# Creating a set — notice "Masala Chai" appears 3 times in the list
orders_today = {"Masala Chai", "Green Tea", "Masala Chai", "Lemon Tea", "Masala Chai", "Green Tea"}
print("Unique orders today:", orders_today)
# Output will only show each tea ONCE — duplicates are gone!

# Adding an item
orders_today.add("Ginger Tea")
print("After adding Ginger Tea:", orders_today)

# Removing an item
orders_today.discard("Lemon Tea")   # discard won't crash if item doesn't exist
print("After removing Lemon Tea:", orders_today)

# Real-world use: finding common items between two sets
menu_A = {"Masala Chai", "Green Tea", "Lemon Tea"}
menu_B = {"Green Tea", "Ginger Tea", "Lemon Tea"}

common_teas = menu_A & menu_B          # intersection — items in BOTH
only_in_A   = menu_A - menu_B          # difference — items only in A
all_teas    = menu_A | menu_B          # union — all items from both

print("\nMenu A:", menu_A)
print("Menu B:", menu_B)
print("Common teas (in both menus):", common_teas)
print("Only in Menu A:", only_in_A)
print("All teas combined (unique):", all_teas)

# ✅ Use a SET when:
#    - You want only UNIQUE values
#    - You need to compare two groups (common, difference, union)
#    - Order doesn't matter


# ============================================================
# QUICK SUMMARY TABLE
# ============================================================
print("\n" + "=" * 50)
print("QUICK SUMMARY")
print("=" * 50)
print("""
| Type       | Brackets | Ordered | Changeable | Duplicates |
|------------|----------|---------|------------|------------|
| List       |  [ ]     |  Yes    |    Yes     |    Yes     |
| Tuple      |  ( )     |  Yes    |    No      |    Yes     |
| Dictionary |  { }     |  Yes    |    Yes     | Keys: No   |
| Set        |  { }     |  No     |    Yes     |    No      |

Real-life analogy:
  List       → Shopping list (ordered, can edit, duplicates ok)
  Tuple      → Printed receipt (fixed, cannot change)
  Dictionary → Contact book (name → phone number)
  Set        → Bag of unique marbles (no duplicates, no order)
""")
