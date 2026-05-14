# ============================================================
# 📘 OOP - 01: Simple Class
# ============================================================
# A CLASS is a blueprint/template for creating objects.
# Think of a class like a recipe — it defines what an object
# will look like and how it will behave.
#
# KEY CONCEPTS:
#   - class keyword is used to define a class
#   - 'pass' is used when the class body is intentionally empty
#   - Objects (instances) are created by calling the class like a function
#   - type() returns the type/class of any object
#   - Every class itself is of type <class 'type'> (metaclass)
# ============================================================

class Chai:
    pass  # Empty class — no attributes or methods yet

class ChaiTime:
    pass  # Another empty class for comparison

# type() on a CLASS returns <class 'type'>
# because in Python, classes are themselves objects of type 'type'
print(type(Chai))           # <class 'type'>

# Creating an INSTANCE (object) of the Chai class
ginger_tea = Chai()

# type() on an INSTANCE returns the class it was created from
print(type(ginger_tea))             # <class '__main__.Chai'>

# Checking if the instance belongs to a specific class
print(type(ginger_tea) is Chai)     # True  — ginger_tea is a Chai object
print(type(ginger_tea) is ChaiTime) # False — ginger_tea is NOT a ChaiTime object

# ============================================================
# 💡 SUMMARY:
#   - class Chai: defines a new class named Chai
#   - ginger_tea = Chai() creates an instance of Chai
#   - type(obj) tells you what class the object belongs to
#   - 'is' checks identity (exact type match), not inheritance
# ============================================================
