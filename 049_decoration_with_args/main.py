
# DECORATIONS WITH PARAMETERS

def add_two(a,b):
    sum = a +b
    print(sum)


def decorate_add_two(func,x,y):
    print("Before calling add_two")
    add_two(x,y)
    print("After calling add_two")


decorate_add_two(add_two,5,10)









