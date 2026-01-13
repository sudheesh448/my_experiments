""" Python Magic Methods
Below are the lists of Python magic methods and their uses.

1. Initialization and Construction
__new__: To get called in an object's instantiation.
__init__: To get called by the __new__ method.
__del__: It is the destructor. """


class Profile:

    """
    1. __init__: The Decorator (The Most Common)
    Use Case: Setting up the initial values of an object. 
    Think of this as "painting the walls" and "moving in furniture" after the house is already built. 
    """
    def __init__(self,username):
        self.username = username
        print(f"Initializing {self.username}")

user = Profile("Sudheesh")




"""
__new__: The Builder (The Advanced)
Use Case: Controlling how the object is actually created in memory. 
__new__ runs before __init__. It is the method that actually returns the new instance.
"""

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating a new connection")

            cls._instance = super(DatabaseConnection,cls).__new__(cls)
        return cls._instance
db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1 is db2)


"""
3. __del__: The Cleanup Crew (The Destructor)
Use Case: Closing resources like files, network sockets,
or database connections when the object is no longer needed.
"""

class TempFile:
    def __init__(self,name):
        self.name = name
        print(f"File {self.name} created.")
    
    def __del__(self):
        print(f"Cleaning up: {self.name} deleted from disk")

f = TempFile("data.txt")
del f


"""
1. The Real Constructor: __new__
__new__ is the method that actually creates the object in your computer's memory. It is the "builder" that pours the concrete for the house.

When it runs: Before __init__.

What it returns: A brand-new, empty instance of the class.

2. The Initializer: __init__
__init__ is the method that sets up the object. It takes the empty house built by __new__ and paints the walls, installs the plumbing, and moves in the furniture.

When it runs: Immediately after the object is created.

What it returns: Nothing (None).
"""