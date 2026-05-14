#scopes and namespace in functions
def serve_chai():
    chai_type = "Masala chai" #local scope
    print(f"Inside functions {chai_type}")

chai_type = "Lemon"

serve_chai()

print(f"Outside function: {chai_type}")


def chai_counter():
    chai_order = "lemon" # enclosing scope
    def print_order():
        chai_order = "Ginger"
        print("Inner:" , chai_order)

    print_order()
    print("Outer: ", chai_order)


chai_order = "Tulse" #global
chai_counter()
print("global scope: ", chai_order)

