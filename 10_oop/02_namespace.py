# ============================================================
# 📘 OOP - 02: Namespace in Classes
# ============================================================
# A NAMESPACE is a mapping from names to objects.
# In Python OOP, there are two main namespaces:
#
#   1. CLASS NAMESPACE  — attributes shared by ALL instances
#   2. INSTANCE NAMESPACE — attributes unique to each object
#
# HOW ATTRIBUTE LOOKUP WORKS:
#   Python first checks the INSTANCE namespace,
#   then falls back to the CLASS namespace if not found.
#
# You can also ADD new attributes to a class or instance
# DYNAMICALLY (at runtime) — Python allows this!
# ============================================================

class Chai:
    origin = "India"   # Class-level attribute — shared by all instances

# Accessing a class attribute directly via the class name
print(Chai.origin)     # India

# Dynamically adding a new attribute to the CLASS at runtime
Chai.is_hot = True
print(Chai.is_hot)     # True

# ── Creating an instance ──────────────────────────────────
masala = Chai()

# Instance inherits class attributes (looks up class namespace)
print(f"Masala {masala.origin} ")   # Masala India
print(f"Masala {masala.is_hot} ")   # Masala True

# ── Instance Attribute Shadowing ──────────────────────────
# Setting an attribute on the INSTANCE creates a new entry
# in the INSTANCE namespace — it does NOT change the class attribute.
masala.is_hot = False   # Only affects 'masala', not the Chai class

print("Class: ", Chai.is_hot)          # True  — class attribute unchanged
print(f"Masala:  {masala.is_hot}")     # False — instance has its own copy

# ── Adding a brand-new attribute to just one instance ─────
# This attribute exists ONLY on 'masala', not on the Chai class
masala.flavour = "Masala"
print(masala.flavour)   # Masala

# ============================================================
# 💡 SUMMARY:
#   - Class attributes are shared across all instances
#   - You can add attributes to a class or instance dynamically
#   - Assigning to an instance attribute SHADOWS the class attribute
#     for that instance only — the class attribute stays unchanged
#   - Lookup order: instance namespace → class namespace
# ============================================================
