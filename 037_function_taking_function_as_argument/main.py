
# function taking another function as argument and calling it

def print_hello():
    print("Hello")

def takes_another_function (func):
    func()



takes_another_function(print_hello)



