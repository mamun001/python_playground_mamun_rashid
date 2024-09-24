# Base Class that we will use to inherit  
class chess_player:
    def __init__(self, name , rating):
        self.name = name
        self.rating = rating
    def get_rating(self):
        return self.rating
   
# Creating another class that wil inherit chess_player class
class grandmaster(chess_player):
    # we have pass the right parameters to the base class
    def __init__(self, name, rating):
        # this init has to call the init of the base class; NOT "self" is missing
        super().__init__(name, rating)
        print("I am a Grandmaster")
   

   
# making an object of the base class
magnus = chess_player('magnus', 2800)
print(magnus.name)
print(magnus.get_rating())
# making an object of the sub class
hikaru = grandmaster('hikaru', 2750)
print(hikaru.name)
print(hikaru.get_rating())

