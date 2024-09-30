#  Example of "MAP" (dictionary) in Python

chess_player_ratings = {"Magnus": 2800, "Hikaru": 2750, "Mamun": 1700}


# print the whole dictionary
print(chess_player_ratings)    


# print type of a dictionarty
print(type(chess_player_ratings))

# print only element's value
print(chess_player_ratings["Magnus"])    

# print count of key/values
print(len(chess_player_ratings))
   
# print only the keys
print(chess_player_ratings.keys())

# print only the values
print(chess_player_ratings.values())

# use get method to get a value
print(chess_player_ratings.get("Magnus"))


# use pop method to prove that dictionary is mutable
print(chess_player_ratings.pop("Magnus"))
# now the dictionary has 1 less key/value pair
print(chess_player_ratings)
