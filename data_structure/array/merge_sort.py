def merge_sort(arr):
    # Print the current split
    print(f"Splitting: {arr}")
    
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge and print the result of this specific merge
    result = merge(left_sorted, right_sorted)
    print(f"Merged {left_sorted} and {right_sorted} -> {result}")
    return result
    
def merge(left, right):
    sorted_array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array

my_list = [64, 34, 25, 12] # Used a shorter list so the output is easier to read
print("--- STARTING MERGE SORT ---")
sorted_list = merge_sort(my_list)
print(f"\nFINAL RESULT: {sorted_list}")