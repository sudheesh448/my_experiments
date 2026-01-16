my_array = [64,34,25,5,22,11,90,12]


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = []
    right = []
    
    for i in range (len(arr)-1):
        if arr[i]< pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    print("left", left,"right",right)
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(my_array))

text = ["quicksort","sdfgsdgsdg","afsadfe"]
print(quick_sort(text))