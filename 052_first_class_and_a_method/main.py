
# DECORATIONS WITH PARAMETERS

class chess_player:
    def __init__(self, name , rating):
        self.name = name
        self.rating = rating

    def get_rating(self):
        result = self.rating
        return result
        
    


magnus = chess_player(name="magnus", rating="2800")

print(magnus.get_rating())











