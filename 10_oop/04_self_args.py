# ============================================================
# 📘 OOP - 04: self and Method Arguments
# ============================================================
# SELF is a reference to the CURRENT INSTANCE of the class.
# It is the first parameter of every instance method.
#
# HOW IT WORKS:
#   When you call  cup.describe()
#   Python translates it to  Chaicup.describe(cup)
#   i.e., the instance is automatically passed as the first argument.
#
# KEY CONCEPTS:
#   - 'self' is just a convention — you could name it anything,
#     but 'self' is the universally accepted standard in Python.
#   - Through 'self', a method can access all instance & class attributes.
#   - Calling a method on the CLASS directly requires passing the
#     instance manually: ClassName.method(instance)
#   - Each instance can have its own attribute values, and 'self'
#     ensures the method uses the correct instance's data.
# ============================================================

class Chaicup:
    size = 150  # ml — class attribute shared by all instances

    def describe(self):
        # 'self' gives access to the instance's attributes
        # Here it reads 'size' — first checks instance, then class namespace
        return f"A {self.size} ml chai cup"


# ── Calling via instance (standard way) ──────────────────
cup = Chaicup()
print(cup.describe())           # A 150 ml chai cup
# Python internally calls: Chaicup.describe(cup)

# ── Calling via class (explicit way) ─────────────────────
# You must pass the instance manually when calling from the class
print(Chaicup.describe(cup))    # A 150 ml chai cup  (same result)

# ── Uncommenting the line below would raise a TypeError ──
# print(Chaicup.describe())
# ❌ TypeError: Chaicup.describe() missing 1 required positional argument: 'self'
# Because no instance is passed, Python doesn't know what 'self' should be.

# ── Instance with a shadowed attribute ───────────────────
cup_two = Chaicup()
cup_two.size = 100   # Instance attribute shadows the class attribute (150)

# When describe() runs for cup_two, self.size reads 100 (instance attr)
print(Chaicup.describe(cup_two))   # A 100 ml chai cup

# ── Uncommenting the line below would raise an AttributeError ──
# print(cup.two.describe())
# ❌ AttributeError: 'Chaicup' object has no attribute 'two'
# Python tries to find attribute 'two' on 'cup', which doesn't exist.

# ============================================================
# 💡 SUMMARY:
#   - 'self' is the first parameter of every instance method
#   - It refers to the specific instance the method is called on
#   - instance.method()  ==  ClassName.method(instance)
#   - Through 'self', methods access instance and class attributes
#   - Each instance can have different attribute values; 'self'
#     ensures the right data is used for each object
# ============================================================
