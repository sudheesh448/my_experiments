# 🧠 Python Memory Management

Python manages memory automatically, so developers don't have to manually allocate or free space (unlike C or C++).
This system relies on two main pillars: **Reference Counting** and **Generational Garbage Collection**.

---

## 1. Objects and References

In Python, variables are not "containers" for data; they are **labels (pointers)** that point to an object sitting in the **Heap Memory**.

```python
x = [1, 2, 3]  # The list object is created in the Heap. 'x' is a label.
y = x          # 'y' now points to the exact same list object.
```

2. Reference Counting (The Primary System)
   Every object in Python maintains a "reference count"—a number representing how many variables or containers are currently pointing to it.

Count Increases: When an object is assigned to a new variable or added to a list/dictionary.

Count Decreases: When a variable is deleted (del x), reassigned, or goes out of scope.

Auto-Deletion: When the count reaches zero, Python's memory manager immediately reclaims that memory.

3. Generational Garbage Collection (The Cleanup Crew)
   Reference counting alone cannot handle Circular References (where Object A points to Object B, and Object B points to Object A, but no one else uses them).

To fix this, Python uses a Generational Garbage Collector (GC) that categorizes objects into three generations based on how long they have existed:

Generation 0: New objects. Checked very often.

Generation 1: Objects that survived one cleanup.

Generation 2: Long-lived objects (like constants or modules). Checked rarely.

4. Stack vs. Heap Memory

Python organizes memory into two distinct areas:
Memory Area Responsibility Speed
Stack Memory Stores function calls, return addresses, and local variable "names". Fast
Heap Memory Stores the actual objects (integers, strings, class instances). Slower but Flexible

💡 Summary Checklist
[x] Everything is an object stored in the Heap.

[x] Reference Counting handles 90% of memory cleanup instantly.

[x] Garbage Collection runs periodically to find and destroy circular references.

[x] del is the magic method triggered just before an object is destroyed.

🔒 The Global Interpreter Lock (GIL)

1. What is the GIL?
   The GIL is a mutex (a lock) that allows only one thread to hold control of the Python interpreter at any given time.

Even if you have a processor with 16 cores, and your Python code uses 16 threads, the GIL ensures that only one thread is executing Python bytecode at any single moment.

2. The **dict** vs **slots** Architecture
   Every time you create a class instance, Python stores its attributes in a dictionary called **dict**. Dictionaries are powerful but memory-heavy.

**slots**: By defining this special attribute, you tell Python: "Don't create a dictionary for this class. Only allow these specific attributes."

Benefit: This can reduce the memory usage of your Coordinate class by up to 50-60% if you are creating millions of points.
