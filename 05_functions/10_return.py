# def make_chai():
#     #return "Here is your masala chai"
#     print("Here is your masala chai")

# return_value = make_chai()


#print(return_value)


def idle_chaiwala():
    pass

print(idle_chaiwala())


def sold_cups():
    return 120

total = sold_cups()

print(total)

def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, chai over"
    return "chai is ready"
    print("chai")


print(chai_status(0))
print(chai_status(5))


def chai_report():
    return 100,20, 30#sold and remaining 


sold, remaining, not_paid  = chai_report()
print(f"Sold : {sold}, Remaining: {remaining} ")



# A function can return none value implicityly  line 11 to 14 is that example
# One Value one value example is from line 17 to 22
# Multiple Value
# Early from a function. line number 24 to 32 is an example


