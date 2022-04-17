class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        if isinstance(other, Vector2):
            return(Vector2(self.x + other.x, self.y + other.y))
        elif isinstance(other, tuple):
            return(Vector2(self.x + other[0], self.y + other[1]))
        else:
            print("Can't equlas these objects")
            exit()

    def __eq__(self, other):
        if isinstance(other, Vector2):
            if self.x == other.x and self.y == other.y:
                return True
            else:
                return False
        elif isinstance(other, tuple):
            if self.x == other[0] and self.y == other[1]:
                return True
            else:
                return False
        else:
            print("Can't match these objects:", type(self), type(other))
            exit()
    
    def __lt__(self, other):
        if isinstance(other, Vector2):
            if self.x < other.x and self.y < other.y:
                return True
            else:
                return False
        elif isinstance(other, tuple):
            if self.x < other[0] and self.y < other[1]:
                return True
            else:
                return False
        else:
            print("Can't match these objects:", type(self), type(other))
            exit()
      
    def __le__(self, other):
        if self < other or self == other:
            return True
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Vector2):
            if self.x > other.x and self.y > other.y:
                return True
            else:
                return False
        elif isinstance(other, tuple):
            if self.x > other[0] and self.y > other[1]:
                return True
            else:
                return False
        else:
            print("Can't match these objects:", type(self), type(other))
            exit()
    
    def __ge__(self, other):
        if self > other or self == other:
            return True
        else:
            return False
