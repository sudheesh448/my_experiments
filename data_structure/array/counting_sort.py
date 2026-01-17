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
n = len(arr) --  length of the array
max_val = max(arr) -- maximum value present in the array


counts = [0] *(max_val +1) --  counts array - which have indexes till max value (from 0 to max value thats why max +1)
output = [0] * n  -- out put array same as input array

for num in arr:
    counts[num] +=1  --- counting the number of occurances of each element in the input array

for i in range(1,len(counts)):
        counts [i]+=counts [i-1] --- determines the last position of each element in the output array
        cumulative position while building output array for each element in input array we will look in to this cumulative array to
        determine the position of the element in the output array.

for i in range(n-1,-1,-1):
        val = arr[i]
        position = counts[val] - 1
        output[position] = val
        counts[val]-=1                  ---- Preparing output array
                                            iteration start from the reverse order (that is n-1 to 0) step is reverse (-1)
                                            picking the value from input array
                                            determine the exact position position = counts[val] - 1 (-1 because indexing is from 0)
                                            add the value to the correct position
                                            substracting the position value in counts (for handling the multiple occurance of same element
                                            if the element occure again it will be next to the same element)


"""