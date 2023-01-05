class Human:
    def __init__(self, glasses, video_games, friends, IQ):
        self.glasses = glasses
        self.video_games = video_games
        self.friends = friends
        self.iq = IQ
    def cool(self):
        if self.friends >= 5:
            return True
        else:
            return False
    #class methods are used to create objects with special attributes
    #classmethod decorator required
    #class methods do not need self as an argument as they do not require an object
    @classmethod
    def nerd(cls,IQ):
        #cls makes the object instance
        #The values in cls are put into __init__
        return cls(True, True, 0, IQ)
Tyler = Human.nerd(140)
print(Tyler.cool())