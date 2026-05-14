chai = "Ginger chai"


def prepare_order():
    print("Preparing", chai)
    

prepare_order()

print(chai)


chai1 = [1,2,3]
 
 
def edit_chai(cup):   # cup here is an aruguments
   cup[1] = 42

edit_chai(chai1) # chai here is parameter
print(chai1)



def make_chai(tea, milk, sugar):
    print(tea,milk,sugar)


make_chai("Darjeeling", "Yes", "Low") # poisitional parameter

make_chai(tea = "Green", sugar= "Medium", milk = "No") #kwargs


def special_chai(*ingredients, **extras): #args keywords def special_chai(*args, **kwargs)
    print("Ingredients", ingredients)
    print("Extras", extras)


special_chai("Cinnamon", "Cardmom", sweetener = "Honey", foam = "yes")


def chai_order(order= []):  #default 
    order.append("Masala ")
    print(order)


chai_order()
chai_order()