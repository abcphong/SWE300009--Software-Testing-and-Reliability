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

# Metamorphic Testing of Merge Sort

# Test MR1: Reversing and Sorting
def test_mr1(sort_function):
    original_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_list = sort_function(original_list.copy())
    reversed_sorted_list = sorted_list[::-1]
    re_sorted_list = sort_function(reversed_sorted_list.copy())
    print("MR1 - Original List: ", original_list)
    print("MR1 - Sorted List: ", sorted_list)
    print("MR1 - Reversed Sorted List: ", reversed_sorted_list)
    print("MR1 - Re-sorted List: ", re_sorted_list)
    return sorted_list == re_sorted_list

# Test MR2: Concatenating and Sorting
def test_mr2(sort_function):
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8, 9, 10]
    concatenated_sorted_list = sort_function(list1 + list2)
    individually_sorted_concatenated_list = sort_function(list1) + sort_function(list2)
    print("MR2 - List 1: ", list1)
    print("MR2 - List 2: ", list2)
    print("MR2 - Concatenated and Sorted List: ", concatenated_sorted_list)
    print("MR2 - Individually Sorted and Concatenated List: ", individually_sorted_concatenated_list)
    return concatenated_sorted_list == individually_sorted_concatenated_list

# Example mutant functions for testing
def mutant1(arr):
    # ROR Mutation: <= instead of <
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mutant1(left_half)
        mutant1(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:  # Mutation here
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

def mutant2(arr):
    # AOR Mutation: // 3 instead of // 2
    if len(arr) > 1:
        mid = len(arr) // 2  # Change back to //2 to fix the bug
        left_half = arr[:mid]
        right_half = arr[mid:]

        mutant2(left_half)
        mutant2(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# List of mutant functions
mutants = [
    mutant1,  # Function implementing the first mutant
    mutant2,  # Function implementing the second mutant
    # ... up to mutant20
]

def test_mutants():
    for i, mutant in enumerate(mutants, start=1):
        try:
            # Replace merge_sort with mutant in tests
            mr1_result = test_mr1(mutant)
            mr2_result = test_mr2(mutant)
            if mr1_result and mr2_result:
                print(f"Mutant {i} survived.")
            else:
                print(f"Mutant {i} killed.")
        except AssertionError as e:
            print(f"Mutant {i} killed: {str(e)}")
        except RecursionError:
            print(f"Mutant {i} failed due to recursion error.")

# def test_mutants():
#     for i, mutant in enumerate(mutants, start=1):
#         try:
#             # Replace merge_sort with mutant in tests
#             mr1_result = test_mr1(mutant)
#             mr2_result = test_mr2(mutant)
#             if mr1_result and mr2_result:
#                 print(f"Mutant {i} survived.")
#             else:
#                 print(f"Mutant {i} killed.")
#         except AssertionError as e:
#             print(f"Mutant {i} killed: {str(e)}")

# Run tests on the original function
print("Testing original merge_sort:")
assert test_mr1(merge_sort), "MR1 failed on original function"
assert test_mr2(merge_sort), "MR2 failed on original function"
print("All metamorphic tests passed for the original function.\n")

# Example test execution for mutation analysis
print("Testing mutants:")
test_mutants()
