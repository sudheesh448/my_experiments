my_array = [64,34,25,12,22,11,90,5]

print(f"initial array :: {my_array}")
n = len(my_array)

for i in range (n):
    print(n-i-1)
    for j in range (n-i-1):
        if my_array[j] > my_array[j + 1]:
            my_array[j], my_array[j + 1] = my_array[j + 1], my_array[j]
        print(f" j loop iteration ::: {j} array :: {my_array}")
    
    print()
    print(f" i loop iteration ::: {i} array :: {my_array}")
print(my_array)

"""
After completing the 1st iteration of j loop the larger number will be in righ most place. 
so in next loop we dont want to look in to that place thats why n-i-1
"""