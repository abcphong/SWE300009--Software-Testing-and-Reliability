# Original Merge Sort Implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Recursive call on each half
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = j = k = 0
        
        # Copy data to temp arrays left_half and right_half
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# Example usage
example = [3, 12, 3, 4, 5, 623, -1, 2, -3, -22, -12, -1, 0, -22, 3, 623, 11, 3, 12]
sorted_arr = merge_sort(example)
print("The sorted list:", sorted_arr)
