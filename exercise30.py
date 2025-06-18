def safe_access(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

my_list = [10, 20, 30]
print(safe_access(my_list, 1))
print(safe_access(my_list, 5))
