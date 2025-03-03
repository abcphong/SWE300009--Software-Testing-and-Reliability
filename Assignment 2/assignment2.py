def split_and_sort(nums):
    # check if input list length is less than or equal to 20
    if len(nums) > 20:
        print("Error: Input list should not contain more than 20 integers.")
        return None, None

    # check if 0 is in the input list
    if 0 in nums:
         print("Error: The number 0 is not a valid input.")
         return None, None

    # filter odd and even numbers into two separate lists
    odd_nums = [num for num in nums if num % 2 == 1]
    even_nums = [num for num in nums if num % 2 == 0]

    # remove duplicates and sort
    odd_nums = sorted((odd_nums))
    even_nums = sorted((even_nums))

    return odd_nums, even_nums

nums = [6, 1, 3, 4, 3, 5, 1, 19, 17, 18, 11, 13, 11, 12, 14, 20, 1, 22]
odd_nums, even_nums = split_and_sort(nums)

print("Odd numbers:", odd_nums)
print("Even numbers:", even_nums)
