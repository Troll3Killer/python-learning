class fancy:
    def __init__(self,string):
        self.string = string
    def __floordiv__(self,other):
        if len(self.string) > len(other.string):
            line = "~" * len(self.string)
        else:
            line = "~" * len(other.string)
        return "\n".join([line,self.string,line,line,other.string,line])
meat = fancy("meat")
juice = fancy("juice")
print(meat//juice)