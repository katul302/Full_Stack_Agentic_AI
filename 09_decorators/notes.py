"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                     🎨 PYTHON DECORATORS - NOTES                            ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 WHAT IS A DECORATOR?
─────────────────────────────────────────────────────────────────────────────
A decorator is a function that:
  ✅ Takes another function as input
  ✅ Adds some extra behavior (before/after)
  ✅ Returns a new function (wrapper)

Think of it like a "wrapper" around your function — like gift wrapping a box.
The box (original function) is still inside, but now it has extra packaging!

Syntax:
    @decorator_name
    def my_function():
        ...

This is equivalent to:
    my_function = decorator_name(my_function)

─────────────────────────────────────────────────────────────────────────────
📁 FILE 01: basic.py — Basic Decorator
─────────────────────────────────────────────────────────────────────────────

CONCEPT: How a simple decorator works

    from functools import wraps

    def my_decorators(func):       # Takes a function as argument
        @wraps(func)               # Preserves original function metadata
        def wrapper():             # Inner wrapper function
            print("Before")
            func()                 # Calls the original function
            print("After")
        return wrapper             # Returns the wrapper

    @my_decorators
    def greet():
        print("Hello!")

    greet()           # Output: Before → Hello! → After
    greet.__name__    # Output: "greet" (thanks to @wraps)

KEY POINTS:
  • @wraps(func) — preserves __name__, __doc__ of the original function
  • Without @wraps, greet.__name__ would return "wrapper" (misleading!)
  • The decorator pattern: define → wrap → return wrapper

─────────────────────────────────────────────────────────────────────────────
📁 FILE 02: logging_decorators.py — Logging Decorator
─────────────────────────────────────────────────────────────────────────────

CONCEPT: Decorators that accept arguments (*args, **kwargs)

    def log_activity(func):
        @wraps(func)
        def wrapper(*args, **kwargs):       # Accepts any arguments
            print(f"🚀 Calling: {func.__name__}")
            result = func(*args, **kwargs)  # Passes args to original func
            print(f"✅ Finished: {func.__name__}")
            return result
        return wrapper

    @log_activity
    def brew_chai(type):
        print(f"Brewing {type} chai")

    brew_chai("Masala")
    # Output:
    # 🚀 Calling: brew_chai
    # Brewing Masala chai
    # ✅ Finished: brew_chai

KEY POINTS:
  • *args  → captures positional arguments as a tuple
  • **kwargs → captures keyword arguments as a dict
  • Using both makes the decorator work with ANY function signature
  • Always return result so the original return value is not lost
  • Great use case: logging, timing, monitoring function calls

─────────────────────────────────────────────────────────────────────────────
📁 FILE 03: auth_decorators.py — Authentication Decorator
─────────────────────────────────────────────────────────────────────────────

CONCEPT: Decorators for access control / authentication

    current_user = {"username": "atul", "role": "admin"}

    def login_required(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not current_user:
                print("❌ Access Denied: Please log in first!")
                return None
            return func(*args, **kwargs)
        return wrapper

    def admin_required(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if current_user.get("role") != "admin":
                print("⛔ Access Denied: Admins only!")
                return None
            return func(*args, **kwargs)
        return wrapper

    @login_required
    @admin_required
    def delete_user(username):
        print(f"🗑️ User '{username}' has been deleted.")

KEY POINTS:
  • Multiple decorators can be stacked (applied bottom-up)
  • @login_required → @admin_required → def delete_user
    means: login_required(admin_required(delete_user))
  • Auth decorators are widely used in web frameworks like Flask/Django
  • They enforce rules WITHOUT modifying the original function

─────────────────────────────────────────────────────────────────────────────
🔑 SUMMARY TABLE
─────────────────────────────────────────────────────────────────────────────

  Concept              | Description
  ─────────────────────|──────────────────────────────────────────────────
  Decorator            | A function that wraps another function
  @wraps(func)         | Preserves original function's name & docstring
  *args, **kwargs      | Makes decorator work with any function signature
  Stacked decorators   | Multiple decorators applied to one function
  Use cases            | Logging, Auth, Timing, Caching, Retry logic

─────────────────────────────────────────────────────────────────────────────
💡 REAL-WORLD USE CASES
─────────────────────────────────────────────────────────────────────────────

  1. 🔐 Authentication   → @login_required, @admin_required
  2. 📝 Logging          → @log_activity, @log_errors
  3. ⏱️  Timing           → @measure_time (performance profiling)
  4. 🔁 Retry Logic      → @retry(times=3) (API calls)
  5. 💾 Caching          → @lru_cache (memoization)
  6. ✅ Validation        → @validate_input

─────────────────────────────────────────────────────────────────────────────
⚡ QUICK REFERENCE — DECORATOR TEMPLATE
─────────────────────────────────────────────────────────────────────────────

    from functools import wraps

    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # --- Code BEFORE the function runs ---
            result = func(*args, **kwargs)
            # --- Code AFTER the function runs ---
            return result
        return wrapper

    @my_decorator
    def any_function():
        pass

─────────────────────────────────────────────────────────────────────────────
"""
