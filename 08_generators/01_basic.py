def serve_chai():
    yield "Cup 1: Masala chai"
    yield "Cup 2: Ginger chai"
    yield "Cup 3: Elaichi chai"

stall = serve_chai()

print(stall)

for cup in stall:
    print(cup)

# what is the differnce in having normal function and regaular function in python

#normal function

def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

listed_chai = get_chai_list()
print(listed_chai)

#generator functions

def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai_gen()
print(next(chai))
print(next(chai))
print(next(chai))
#print(next(chai)) give error 