# ============================================================
# 📘 OOP - 06: Inheritance & Composition
# ============================================================
#
# ── INHERITANCE ───────────────────────────────────────────
# Inheritance is an "IS-A" relationship.
# A child class INHERITS attributes and methods from a parent class.
# The child can also ADD new methods or OVERRIDE existing ones.
#
# SYNTAX:
#   class Child(Parent):
#       ...
#
# BENEFITS:
#   - Reuse code from the parent class
#   - Extend or specialise behaviour in the child class
#   - Supports polymorphism (different classes, same interface)
#
# ── COMPOSITION ───────────────────────────────────────────
# Composition is a "HAS-A" relationship.
# Instead of inheriting, a class CONTAINS an instance of another class.
# This gives more flexibility than inheritance.
#
# EXAMPLE:
#   A ChaiShop HAS-A Chai (it owns/uses a Chai object internally)
#
# WHEN TO USE WHICH?
#   - Use INHERITANCE when the child truly "is a" type of the parent
#     e.g. MasalaChai IS-A BaseChai
#   - Use COMPOSITION when one class "uses" or "has" another
#     e.g. ChaiShop HAS-A Chai object
# ============================================================


# ── BASE CLASS (Parent) ───────────────────────────────────
class BaseChai:
    """
    The parent/base class that defines the common interface
    for all types of chai.
    """
    def __init__(self, type_):
        # Instance attribute: stores the type of chai
        self.type = type_

    def prepare(self):
        # A method all chai types share
        print(f"Preparing {self.type} chai....")

    def serve(self):
        # Another shared method
        print(f"Serving {self.type} chai.")


# ── INHERITANCE: MasalaChai IS-A BaseChai ────────────────
class MasalaChai(BaseChai):
    """
    Child class that inherits from BaseChai.
    It gets __init__, prepare(), and serve() for free.
    It also adds its own method: add_spices().
    """

    def add_spices(self):
        # New method specific to MasalaChai — not in BaseChai
        print("Adding cardamom, ginger, cloves.")

    def prepare(self):
        # OVERRIDING the parent's prepare() method
        # super() calls the parent class method first, then extends it
        super().prepare()                    # Runs BaseChai.prepare()
        self.add_spices()                    # Then adds spices


# ── INHERITANCE: GingerChai IS-A BaseChai ────────────────
class GingerChai(BaseChai):
    """
    Another child class — demonstrates multiple subclasses
    sharing the same parent.
    """

    def add_ginger(self):
        print("Adding fresh ginger slices.")

    def prepare(self):
        super().prepare()       # Calls BaseChai.prepare()
        self.add_ginger()       # Then adds ginger


# ── COMPOSITION: ChaiShop HAS-A Chai ─────────────────────
class ChaiShop:
    """
    Composition example: ChaiShop does NOT inherit from BaseChai.
    Instead, it CONTAINS a chai object (HAS-A relationship).

    chai_cls is a class attribute that holds the class to use
    for creating chai. This makes it easy to swap chai types
    without changing the ChaiShop logic.
    """
    chai_cls = BaseChai   # Default chai type — can be overridden in subclasses

    def __init__(self):
        # The shop creates (owns) a chai object internally
        # This is COMPOSITION — ChaiShop HAS-A BaseChai instance
        self.chai = self.chai_cls("Regular")

    def serve(self):
        # Delegates the serve action to the contained chai object
        print(f"Serving {self.chai.type} chai in shop.")

    def prepare_and_serve(self):
        # Uses the chai object's methods
        self.chai.prepare()
        self.serve()


# ── COMPOSITION with a specialised shop ──────────────────
class MasalaChaiShop(ChaiShop):
    """
    A specialised shop that overrides chai_cls to use MasalaChai.
    This shows how composition + inheritance work together:
      - MasalaChaiShop IS-A ChaiShop (inheritance)
      - ChaiShop HAS-A Chai (composition)
    """
    chai_cls = MasalaChai   # Override the class attribute

    def __init__(self):
        # Calls ChaiShop.__init__ but now self.chai_cls is MasalaChai
        super().__init__()
        # Re-create chai as MasalaChai with a specific type
        self.chai = MasalaChai("Masala")


# ============================================================
# 🔬 DEMO / TESTING
# ============================================================

print("=" * 50)
print("── BaseChai ──")
base = BaseChai("Plain")
base.prepare()    # Preparing Plain chai....
base.serve()      # Serving Plain chai.

print("\n── MasalaChai (Inheritance + Override) ──")
masala = MasalaChai("Masala")
masala.prepare()  # Preparing Masala chai.... + Adding cardamom, ginger, cloves.
masala.serve()    # Serving Masala chai.  (inherited from BaseChai)

print("\n── GingerChai (Inheritance + Override) ──")
ginger = GingerChai("Ginger")
ginger.prepare()  # Preparing Ginger chai.... + Adding fresh ginger slices.
ginger.serve()    # Serving Ginger chai.

print("\n── ChaiShop (Composition) ──")
shop = ChaiShop()
shop.prepare_and_serve()   # Preparing Regular chai.... → Serving Regular chai in shop.

print("\n── MasalaChaiShop (Composition + Inheritance) ──")
masala_shop = MasalaChaiShop()
masala_shop.prepare_and_serve()  # Preparing Masala chai.... + spices → Serving Masala chai in shop.

# ── isinstance() checks ───────────────────────────────────
print("\n── isinstance() checks ──")
print(isinstance(masala, BaseChai))    # True  — MasalaChai IS-A BaseChai
print(isinstance(masala, MasalaChai)) # True  — exact type
print(isinstance(shop, BaseChai))     # False — ChaiShop does NOT inherit BaseChai

# ============================================================
# 💡 SUMMARY:
#
#   INHERITANCE (IS-A):
#     - class Child(Parent): gives Child all of Parent's methods
#     - Child can add new methods or override existing ones
#     - super() calls the parent's version of a method
#     - isinstance(obj, Parent) returns True for child instances
#
#   COMPOSITION (HAS-A):
#     - A class stores an instance of another class as an attribute
#     - More flexible than inheritance — easy to swap components
#     - Avoids deep inheritance chains (prefer composition over inheritance)
#
#   TOGETHER:
#     - Real-world designs often combine both patterns
#     - Use inheritance for shared behaviour, composition for shared objects
# ============================================================
