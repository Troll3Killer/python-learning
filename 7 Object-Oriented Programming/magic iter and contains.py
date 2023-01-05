class Yolo:
    def __init__(self, yum):
        self.yum = yum
    #cool cool 
    def __iter__(self):
        x = self.yum
        for i in x:
            print(i + "!!!")
    #I honestly can't be bothered to find a use case for this, just imagine it does something cool
    def __contains__(self):
        print( "Cheese man")
hmm = Yolo(["1","2","3","4","5"])
hmm.__iter__()
hmm.__contains__()