my_large_array = [170, 45, 75, 90, 802, 24, 2, 66]



def counting_sort_for_radix(exp,arr):
    n = len(arr)
    output = [0] * n
    counts = [0] * 10

    for num in arr:
        index = (num//exp)%10
        counts[index] += 1

    for i in range(1,10):
        counts[i]+= counts[i-1]
    for i in range(n-1,-1,-1):
        num = arr[i]
        index = (num //exp)%10
        output[counts[index]-1] = num
        counts[index] -=1

    for i in range(n):
        arr[i] = output[i]
    print(f"array after :: {exp} :: {arr}")

def radix_sort(arr):
    if not arr: return arr

    max_val = max(arr)

    exp = 1
    while max_val // exp >0:
        counting_sort_for_radix(exp,arr)
        exp *= 10
    return arr

print(radix_sort(my_large_array))

