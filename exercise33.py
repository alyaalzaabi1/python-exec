set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

both = set1 & set2
only_one = set1 ^ set2

print("Common numbers:", both)
print("Unique numbers:", only_one)
