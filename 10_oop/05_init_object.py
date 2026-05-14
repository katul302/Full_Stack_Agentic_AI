# ============================================================
# 📘 OOP - 05: __init__ and Object Initialization
# ============================================================
# __init__ is a SPECIAL (dunder/magic) METHOD in Python.
# It is automatically called when a new instance is created.
# Think of it as the CONSTRUCTOR of the class.
#
# PURPOSE:
#   - Initialize instance attributes with values specific to each object
#   - Ensures every object starts with a well-defined state
#   - Accepts arguments so each instance can be customized at creation
#
# SYNTAX:
#   def __init__(self, param1, param2, ...):
#       self.attr1 = param1
#       self.attr2 = param2
#
# NOTE:
#   - 'type_' is used instead of 'type' because 'type' is a
#     built-in Python function — using it as a variable name
#     would shadow the built-in. Adding '_' is the convention.
#   - self.type and self.size are INSTANCE attributes — each
#     object gets its own separate copy.
# ============================================================

class ChaiOrder:
    def __init__(self, type_, size):
        # Called automatically when ChaiOrder(...) is invoked
        # 'self' refers to the newly created instance
        self.type = type_   # Store the chai type on this instance
        self.size = size    # Store the size (ml) on this instance

    def summary(self):
        # Accesses instance attributes via 'self'
        return f"{self.size}ml of {self.type} chai"


# ── Creating instances ────────────────────────────────────
# __init__ is called automatically with the provided arguments
order = ChaiOrder("Masala", 200)
# Internally: order.__init__("Masala", 200)
# Sets: order.type = "Masala", order.size = 200
print(order.summary())       # 200ml of Masala chai

order_two = ChaiOrder("Ginger", 220)
# Sets: order_two.type = "Ginger", order_two.size = 220
print(order_two.summary())   # 220ml of Ginger chai

# ── Each instance is INDEPENDENT ─────────────────────────
# order and order_two have their own separate attribute values
# Changing one does NOT affect the other

# ============================================================
# 💡 SUMMARY:
#   - __init__ is the constructor — runs automatically on object creation
#   - Use it to set up instance attributes with initial values
#   - Parameters after 'self' are passed when creating the object
#   - Each instance gets its own copy of the attributes set in __init__
#   - Use trailing underscore (type_) to avoid clashing with built-ins
# ============================================================
