# ============================================================
# 📘 OOP - 03: Attribute Shadowing
# ============================================================
# ATTRIBUTE SHADOWING occurs when an instance attribute has
# the SAME NAME as a class attribute.
#
# When you assign a value to an instance attribute that shares
# a name with a class attribute, Python creates a NEW entry in
# the INSTANCE's own namespace — it does NOT modify the class.
# The instance attribute then "shadows" (hides) the class one.
#
# KEY CONCEPTS:
#   - Class attributes are defined directly inside the class body
#   - Instance attributes are set on individual objects
#   - del obj.attr removes the instance attribute, revealing
#     the class attribute again (un-shadowing)
#   - del obj.attr on a non-existent instance attr → AttributeError
# ============================================================

class Chai:
    temperature = "hot"    # Class attribute — shared by all instances
    strength = "Strong"    # Class attribute — shared by all instances

# Create an instance — it inherits class attributes
cutting_chai = Chai()
print(cutting_chai.temperature)   # hot  (reads from class namespace)

# ── Shadowing a class attribute ───────────────────────────
# This creates a NEW instance attribute 'temperature' on cutting_chai.
# The class attribute Chai.temperature is NOT changed.
cutting_chai.temperature = "Mild"

# Adding a brand-new attribute that only exists on this instance
cutting_chai.cup = "small"

print(f"After changing", cutting_chai.temperature)   # Mild  (instance attr)
print(f"Cup size is", cutting_chai.cup)              # small (instance attr)

# The class attribute is still unchanged
print(f"Direct look into the class", Chai.temperature)  # hot

# ── Removing instance attributes with del ─────────────────
# del removes the INSTANCE attribute, not the class attribute.
# After deletion, the instance falls back to the class attribute.
del cutting_chai.temperature   # removes instance shadow → class attr visible again
del cutting_chai.cup           # removes instance-only attr

print(cutting_chai.temperature)  # hot  — class attribute is visible again
# print(cutting_chai.cup)        # ❌ AttributeError: 'Chai' object has no attribute 'cup'
                                  #    (cup was only on the instance, now deleted)

# ============================================================
# 💡 SUMMARY:
#   - Instance attributes SHADOW class attributes of the same name
#   - The class attribute itself is never modified by instance assignment
#   - del obj.attr removes the instance attribute (un-shadows)
#   - After un-shadowing, Python falls back to the class attribute
#   - Deleting an attribute that doesn't exist raises AttributeError
# ============================================================
