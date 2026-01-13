
"""
1. Unary Operators: __neg__ and __pos__These handle the plus ($+$) and 
minus ($-$) signs placed directly in front of an object.
A great use case is a Coordinate or Vector system.
"""
class Coordinate:
    def __init__(self,x,y):
        self.x,self.y = x,y

    def __neg__(self):
        return Coordinate(-self.x,-self.y)

    def __pos__(self):
        print("--Unary plus triggered--")
        return Coordinate(+self.x,+self.y)
    
    def __repr__(self):
        return f"Coordinates ({self.x},{self.y})"

point = Coordinate(-10, 5)

neg_point = -point  # Triggers __neg__
pos_point = +point  # Triggers __pos__

print(f"Original : {point}")
print(f"Negated:  {neg_point}")
print(f"Positive: {pos_point}")


"""
The Magnitude: __abs__This is used to calculate the "absolute" value. 
For a number, it turns $-5$ into $5$. For a Vector, 
it usually calculates the distance from zero using the Pythagorean theorem: $\sqrt{x^2 + y^2}$.
"""

import math

class Vector:
    def __init__(self,x,y):
        self.x,self.y = x,y

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

v = Vector (3,4)
print(abs(v))



"""
3. Precision: __round__ and __trunc__
These tell Python how to shorten your object when it’s too "long" or has too many decimals.

__round__(self, n): Called by round(obj, n).

__trunc__(self): Called by math.trunc(obj). It just cuts off the decimals without rounding up.

"""
import math

class Bill:
    def __init__(self,amount):
        self.amount = amount

    def __round__(self,n):
        return round(self.amount,n)
    def __trunc__(self):
        return math.trunc(self.amount)

dinner = Bill(105.789)

print(round(dinner,1))
print(math.trunc(dinner))

