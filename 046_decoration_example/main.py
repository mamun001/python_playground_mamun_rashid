
# DECORATIONS

def print_hello():
    print("Hello")


def decorate_print_hello(func):
    print("Before calling print_hello")
    print_hello()
    print("After calling print_hello")


decorate_print_hello(print_hello)









