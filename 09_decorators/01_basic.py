from functools import wraps
def my_decorators(func):
    @wraps(func)
    def wrapper():
        print("Before functions run")

        func()

        print("After functions run")

    return wrapper

@my_decorators
def greet():
    print("Hello From decorators class from chai code")


greet()
print(greet.__name__)