    #non-local vs global scopes
def update_order():
    chai_type = "Elaichi"
    def kitchen():
        nonlocal chai_type
        chai_type = "Kesar"

    kitchen()
    print("After kitchen update", chai_type)

    #non-local vs global scopes