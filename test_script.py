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


# Run tests on the original function
print("Testing original merge_sort:")
assert test_mr1(merge_sort), "MR1 failed on original function"
assert test_mr2(merge_sort), "MR2 failed on original function"
assert test_mr3(merge_sort), "MR3 failed on original function"
assert test_mr4(merge_sort), "MR4 failed on original function"
print("All metamorphic tests passed for the original function.\n")

