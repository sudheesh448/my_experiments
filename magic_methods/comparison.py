class Coordinate:
    def __init__(self,x,y):
        self.x,self.y = x,y
    def __eq__(self,other):
        if not isinstance(other,Coordinate):
            return False
        return self.x==other.x and self.y == other.y

    def __ne__(self,other):
        return not self.__eq__(other)

    def _magnitude(self):
        return (self.x**2 + self.y**2)**0.5

    # 3. Less Than (<)
    def __lt__(self, other):
        return self._magnitude() < other._magnitude()

    # 4. Greater Than (>)
    def __gt__(self, other):
        return self._magnitude() > other._magnitude()

    # 5. Less Than or Equal (<=)
    def __le__(self, other):
        return self._magnitude() <= other._magnitude()

    # 6. Greater Than or Equal (>=)
    def __ge__(self, other):
        return self._magnitude() >= other._magnitude()

    def __repr__(self):
        return f"({self.x}, {self.y})"
     


# --- Testing ---
p1 = Coordinate(10, 10)  # Dist: ~14.14
p2 = Coordinate(5, 5)    # Dist: ~7.07
p3 = Coordinate(10, 10)

print(f"p1 == p3: {p1 == p3}")  # True
print(f"p1 != p2: {p1 != p2}")  # True
print(f"p2 < p1:  {p2 < p1}")   # True (5,5 is closer to origin than 10,10)
print(f"p1 >= p3: {p1 >= p3}")  # True