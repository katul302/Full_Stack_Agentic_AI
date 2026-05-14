def make_chai():
    if not kettle_has_water():
        fill_kettle()
    plug_in_kettle()
    boil_water()
    if not is_cup_clean():
        wash_cup()
    add_to_cup("tea levaes")
    add_to_cup("sugar")
    pour("boiled water")
    stir("cup")
    server("chai")

make_chai()
