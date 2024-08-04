# Import the merge_sort function
from project import merge_sort

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

# Test MR3: Doubling the List
def test_mr3(sort_function):
    original_list = [2323, 111, -22, -111111, 22335, 129, 22, 11126, 335, 13, 5]
    sorted_list = sort_function(original_list.copy())
    doubled_list = original_list + original_list
    sorted_doubled_list = sort_function(doubled_list.copy())
    expected_sorted_doubled_list = sorted(sorted_list + sorted_list) 
    print("MR3 - Original List: ", original_list)
    print("MR3 - Sorted List: ", sorted_list)
    print("MR3 - Doubled List: ", doubled_list)
    print("MR3 - Sorted Doubled List: ", sorted_doubled_list)
    print("MR3 - Expected Sorted Doubled List: ", expected_sorted_doubled_list)
    return sorted_doubled_list == expected_sorted_doubled_list

# Test MR4: Adding a Constant
def test_mr4(sort_function):
    original_list = [183, 11122, 234412, -1123, -50022, -90238, -223, -16, 2135, 323,-12391203 ]
    constant = 10
    modified_list = [x + constant for x in original_list]
    sorted_list = sort_function(original_list.copy())
    sorted_modified_list = sort_function(modified_list.copy())
    expected_sorted_modified_list = [x + constant for x in sorted_list]
    print("MR4 - Original List: ", original_list)
    print("MR4 - Sorted List: ", sorted_list)
    print("MR4 - Modified List: ", modified_list)
    print("MR4 - Sorted Modified List: ", sorted_modified_list)
    print("MR4 - Expected Sorted Modified List: ", expected_sorted_modified_list)
    return sorted_modified_list == expected_sorted_modified_list


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
        mid = len(arr) // 3  # Change back to //2 to fix the bug
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

def mutant3(arr):
    # Replace ‘>’ with ‘>=’ in length check
    if len(arr) >= 1:  # Mutation here
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mutant3(left_half)
        mutant3(right_half)

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

def mutant4(arr):
    # Replace ‘<’ with ‘>’ in comparison
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mutant4(left_half)
        mutant4(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] > right_half[j]:  # Mutation here
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

def mutant5(arr):
    # Swap ‘left_half’ and ‘right_half’ only in the recursive call order
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Swap the order of recursive calls
        mutant5(right_half)
        mutant5(left_half)

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

def mutant6(arr):
    # Do not merge the left half
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mutant6(left_half)
        mutant6(right_half)

        i = j = k = 0

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
    return arr

def mutant7(arr):
    # Replace ‘k += 1’ with ‘k -= 1’
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mutant7(left_half)
        mutant7(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k -= 1  # Mutation here

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k -= 1  # Mutation here

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k -= 1  # Mutation here
    return arr

def mutant8(arr):
    # Always return the original array
    return arr

def mutant9(arr):
    # Replace ‘if left_half[i] < right_half[j]’ with ‘if left_half[i] <= right_half[j]’
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mutant9(left_half)
        mutant9(right_half)

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

def mutant10(arr):
    # Change ‘mid = len(arr) // 2’ to ‘mid = (len(arr) // 2) + 1’
    if len(arr) > 1:
        mid = (len(arr) // 2) + 1  # Mutation here
        left_half = arr[:mid]
        right_half = arr[mid:]

        mutant10(left_half)
        mutant10(right_half)

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

def mutant11(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mutant11(left_half)
        mutant11(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = right_half[j]  # Mutation here
                j += 1
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

def mutant12(arr):
    return sorted(arr)  # Mutation here

def mutant13(arr):
    # Do not merge the left half
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mutant13(left_half)
        mutant13(right_half)

        i = j = k = 0

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

def mutant14(arr):
    if len(arr) > 1:
        mid = (len(arr) + 2)  # Mutation here
        left_half = arr[:mid]
        right_half = arr[mid:]

        mutant14(left_half)
        mutant14(right_half)

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

def mutant15(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mutant15(left_half)
        mutant15(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            arr[k] = right_half[j]  # Mutation here
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

def mutant16(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mutant16(left_half)
        mutant16(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            arr[k] = left_half[i]  # Mutation here
            i += 1
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

def mutant17(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mutant17(left_half)
        mutant17(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 2  # Mutation here
            else:
                arr[k] = right_half[j]
                j += 2  # Mutation here
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

def mutant18(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mutant18(left_half)
        mutant18(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 2  # Mutation here
            else:
                arr[k] = right_half[j]
                j += 2  # Mutation here
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 2  # Mutation here
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 2  # Mutation here
            k += 1
    return arr

def mutant19(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mutant19(left_half)
        mutant19(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if i < len(left_half):  # Mutation here
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

def mutant20(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mutant20(left_half)
        mutant20(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if j < len(right_half):  # Mutation here
                arr[k] = right_half[j]
                j += 1
            else:
                arr[k] = left_half[i]
                i += 1
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
    mutant3,   
    mutant4,
    mutant5,
    mutant6,
    mutant7,
    mutant8,
    mutant9,
    mutant10,
    mutant11,
    mutant12,
    mutant13,
    mutant14,
    mutant15,
    mutant16,
    mutant17,
    mutant18,
    mutant19,
    mutant20
]

def test_mutants():
    for i, mutant in enumerate(mutants, start=1):
        try:
            # Replace merge_sort with mutant in tests
            mr1_result = test_mr1(mutant)
            mr2_result = test_mr2(mutant)
            mr3_result = test_mr3(mutant)
            mr4_result = test_mr4(mutant)
            if mr1_result and mr2_result and mr3_result and mr4_result:
                print(f"Mutant {i} survived.")
            else:
                print(f"Mutant {i} killed.")
        except AssertionError as e:
            print(f"Mutant {i} killed: {str(e)}")
        except RecursionError:
            print(f"Mutant {i} failed due to recursion error.")

# Run tests on the original function
print("Testing original merge_sort:")
assert test_mr1(merge_sort), "MR1 failed on original function"
assert test_mr2(merge_sort), "MR2 failed on original function"
assert test_mr3(merge_sort), "MR3 failed on original function"
assert test_mr4(merge_sort), "MR4 failed on original function"
print("All metamorphic tests passed for the original function.\n")

# Example test execution for mutation analysis
print("Testing mutants:")
test_mutants()
