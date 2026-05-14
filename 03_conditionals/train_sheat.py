seat_type = input("Enter seat type (sleeper/AC/general/luxury)").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - NO AC, beds are available")

    case "ac":
        print("AC - Air Conditioned, comfy ride")

    case "general":
        print("General these are cheapesr options, no reservation")

    case "luxury":
        print("Premium sheat with meals")

    case _:
        print("Invalid sheat type")
