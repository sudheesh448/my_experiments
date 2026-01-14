class Coordinate:
    def __init__(self,x,y):
        self.x,self.y = x,y
    def __add__(self,other):
        return Coordinate(self.x + other.x ,self.y + other.y)
    
    def __sub__(self,other):
        return Coordinate(self.x - other.x,self.y - other.y)
    
    def __mul__ (self, scalar):
        return Coordinate(self.x * scalar,self.y * scalar)
    
    def __truediv__(self,scalar):
        return Coordinate(self.x/scalar,self.y/scalar)
    
    def __repr__(self):
        return f"Coordinate ({self.x},{self.y})"

    def __mod__(self,screen_width):
        return Coordinate(self.x % screen_width,self.y % screen_width)

p1 = Coordinate(805,10)
p2 = Coordinate(5,2)

print(f"Addition: {p1 + p2}")    # Coordinate(15, 22)
print(f"Subtraction: {p1 - p2}") # Coordinate(5, 18)
print(f"Multiplication: {p1 * 2}") # Coordinate(20, 40)
print(f"Modulus: {p1 % 800}") # Coordinate(20, 40)
print(f"Division: {p1 / 2}")