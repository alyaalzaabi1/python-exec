def find_max(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

my_list = [3, 7, 2, 8, 5]
print("Maximum number:", find_max(my_list))
