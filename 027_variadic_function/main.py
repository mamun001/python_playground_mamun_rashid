
# variadic func in Python even though that is not what it is called in Python

def sum_all (*args):
    sum = 0
    for number in args:
        sum = sum + number
    return sum


print(sum_all(0))
print(sum_all(0,7,9))
print(sum_all(0,7,9,89,908,9876,4543))




