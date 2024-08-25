
# REDUCE FUNCTION
# reduce needs importing (unlike map and filter) in Python 3

from functools import reduce

my_list = ["jo","jil","pete","pauly"]

def add_two_strings (s1,s2):
    return s1 + s2
    

reduced_result = reduce(add_two_strings,my_list)

print(reduced_result)




