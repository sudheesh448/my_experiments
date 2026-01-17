my_array = [64,34,25,64,5,22,11,90,12]

def counting_sort_unstable(arr):
    if not arr: return arr
    max_val = max(arr)

    counts = [0]*(max_val + 1)

    for num in arr:
        counts[num]+=1
    index = 0
    for i in range (len(counts)):
        if counts[i]>0:
            for j in range(counts[i]):
                arr[index]=i
                index+=1
    return arr

print(counting_sort_unstable(my_array))


def counting_sort_stable(arr):
    if not arr: return arr
    n = len(arr)
    max_val = max(arr)

    counts = [0] *(max_val +1)
    output = [0] * n

    for num in arr:
        counts[num] +=1
    print(counts)
    for i in range(1,len(counts)):
        counts [i]+=counts [i-1]

    print(counts)

    for i in range(n-1,-1,-1):
        val = arr[i]
        position = counts[val] - 1
        output[position] = val
        counts[val]-=1

    return output


print(counting_sort_stable(my_array))


"""


"""