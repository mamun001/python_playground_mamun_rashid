
# KEYWORD VARIABLE ARGUMENTS
# you know this, when you see double stars in the function definition


def print_key_values (**args):
    
    for k,v in args.items():
        print(k,v)
    


print_key_values(a=5,x="hello",y=5.5)




