def chai_flavour(flavour = "masala"):
   
    """Return the flavour of chai""" # this line is doc string or function documents string
    return flavour


print(chai_flavour.__doc__)
print(chai_flavour.__name__)

#help(len)

def generate_bill(chai=0, samosa= 0):
    
    """
    Calculate the total bill for chai and samosa

    :param chai: Number of chai cup (10 rupess each)
    :param samsosa: Number of samosa (15 rupess each)
    : return: (total amount, thank you message as string)
    """

    total = chai*10 + samosa*15
    return total, "Thank your for visiting chaicode.com"
print(generate_bill.__doc__)