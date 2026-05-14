from functools import wraps

# Simulated current logged-in user
# Change role to "user" or set to None to test different scenarios
current_user = {"username": "atul", "role": "admin"}

# ─────────────────────────────────────────────
# 🔐 Decorator 1: login_required
# Checks if a user is logged in before allowing access
# ─────────────────────────────────────────────
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user:
            print("❌ Access Denied: Please log in first!")
            return None
        print(f"✅ Logged in as: {current_user['username']}")
        return func(*args, **kwargs)
    return wrapper


# ─────────────────────────────────────────────
# 🛡️ Decorator 2: admin_required
# Checks if the logged-in user has admin role
# ─────────────────────────────────────────────
def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.get("role") != "admin":
            print(f"⛔ Access Denied: Admins only! Your role: '{current_user.get('role')}'")
            return None
        return func(*args, **kwargs)
    return wrapper


# ─────────────────────────────────────────────
# 🔒 Using stacked decorators
# Applied bottom-up: first admin_required, then login_required
# ─────────────────────────────────────────────

@login_required
@admin_required
def delete_user(username):
    print(f"🗑️  User '{username}' has been deleted successfully.")


@login_required
def view_dashboard():
    print(f"📊 Welcome to the dashboard, {current_user['username']}!")


@login_required
@admin_required
def view_admin_panel():
    print("🔧 Admin Panel: All system settings are accessible.")


# ─────────────────────────────────────────────
# 🚀 Running the examples
# ─────────────────────────────────────────────

print("=" * 50)
print("Test 1: Admin trying to delete a user")
print("=" * 50)
delete_user("john_doe")

print()
print("=" * 50)
print("Test 2: Viewing the dashboard")
print("=" * 50)
view_dashboard()

print()
print("=" * 50)
print("Test 3: Accessing admin panel")
print("=" * 50)
view_admin_panel()

print()
print("=" * 50)
print("Test 4: Non-admin user trying to delete")
print("=" * 50)
# Temporarily change role to simulate a regular user
current_user["role"] = "user"
delete_user("jane_doe")

print()
print("=" * 50)
print("Test 5: Logged-out user trying to access dashboard")
print("=" * 50)
# Simulate logged-out state
saved_user = current_user.copy()
current_user.clear()
view_dashboard()
