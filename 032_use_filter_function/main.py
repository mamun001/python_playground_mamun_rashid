
# BUILT-IN FILTER FUNCTION

my_list = ["jo","jil","pete","pauly"]

def longer_than_4 (s):
    if len(s) > 2:
        return True
    else:
        return False
    

filtered_list = list(filter(longer_than_4,my_list))

print(filtered_list)




