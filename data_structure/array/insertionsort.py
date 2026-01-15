my_array = [64,34,25,5,22,11,90,12]

def insertion_sort(arr):
    n=len(arr)
    for i in range (1,n):
        key = arr[i]
        j = i - 1
        while j>= 0 and arr[j]> key:
            arr[j+1] = arr [j]
            j-= 1    
        arr[j+1] = key
    return arr

arr = insertion_sort(my_array)

print("arr",arr)