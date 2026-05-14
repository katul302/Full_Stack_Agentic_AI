essential_spices = {"cardamon", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "cinnamon", "black pepper"}

#union

all_spices = essential_spices | optional_spices

print(f"All spices: {all_spices}")

#intersection
common_spices = essential_spices & optional_spices
print(f"common spices: {common_spices}")


#differences

only_in_essential = essential_spices - optional_spices
print(f"only_in_essential: {only_in_essential}")

#memebershipt test

print(f"Is cloves in essential spices?  {'cloves' in essential_spices}")