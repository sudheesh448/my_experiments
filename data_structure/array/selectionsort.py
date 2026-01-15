"""
The Selection Sort algorithm finds the lowest value in an array and moves it to the front of the array.
o(n^2)
"""

my_array = [64,34,25,5,22,11,90,12]

n = len(my_array)

for i in range(n-1):
    for j in range(i+1,n):
        if my_array[i] > my_array[j]:
            my_array[i],my_array[j] = my_array[j],my_array[i]

print(my_array)