def sort_list(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


my_list = [5, 3, 8, 1, 4]
print("Sorted list:", sort_list(my_list))
