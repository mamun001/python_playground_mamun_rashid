class chess_player:
    def __init__(self, name , rating):
        self.name = name
        self.rating = rating
    def get_rating(self):
        return self.rating
   

magnus = chess_player('magnus', 2800)
print(magnus.get_rating())
