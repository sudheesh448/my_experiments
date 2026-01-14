


class Coordinate:
    def __init__(self,x,y):
        self.x,self.y = x,y
    
    def __str__(self):
        return f"Point at ({self.x},{self.y})"
    def __repr__(self):
        return f"Coordinate(x={self.x},y={self.y})"
    
    def __bool__(self):
        return self.x !=0 or self.y != 0
    
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x,self.y))




p1= Coordinate(10,20)

# 1. Testing __str__
print("--- Testing __str__ ---")
print(p1)  
print(str(p1))

print("\n--- Testing __repr__ ---")
# 2. Testing __repr__ (inside a list)
points_list = [p1]
print(points_list)

# 3. Testing __repr__ (explicit call)
print(repr(p1))


p1 = Coordinate(0, 0)
p2 = Coordinate(10, 5)

print(bool(p1))
print(bool(p2))

if not p1:
    print("Point 1 is at the center!")


locations = {Coordinate(0,0): "Home", Coordinate(10,10): "Office"}
print(locations[Coordinate(0,0)])