🐍 Python Magic Methods (Dunder Methods)
Welcome to my experiments with Magic Methods in Python! Magic methods (short for Double Underscore) are special methods that allow custom objects to act like built-in types. They enable Operator Overloading and help integrate custom classes seamlessly with Python's native syntax.

Magic methods (also known as dunder methods, short for Double Underscore) are special, pre-defined methods in Python that have double underscores at the beginning and the end of their names—like **init** or **add**.

They are called "Magic" because you don't usually call them manually. Instead, Python triggers them automatically when you perform a specific action on an object.

🛠️ Operator Overloading in Python
Operator Overloading is the ability to define custom behavior for standard Python operators (+, -, \*, /, ==, etc.) when applied to user-defined classes. It allows our custom objects to follow "Pythonic" syntax, making code more readable and intuitive.

1. The Core Concept: Symbols as Shortcuts
   In Python, every operator is a shortcut to a specific Magic Method. When Python sees an operator, it checks the object's class for the corresponding "dunder" method.
