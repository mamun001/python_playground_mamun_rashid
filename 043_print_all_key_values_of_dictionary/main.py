
# Use of *args and **kwargs

def print_args_and_kwargs (*args, **kwargs) :
    print(args)
    print(kwargs)

    print(args[0])

    for key,value in kwargs.items():
        print(key,value)
    



print_args_and_kwargs("GM",10,20.5,name="Magnus",rating="2800")





