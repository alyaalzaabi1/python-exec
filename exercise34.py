names = ["Fatima", "Ali", "Zahra", "Mohammed"]
sorted_by_length = sorted(names, key=lambda x: len(x))

numbers = [-5, 3, -1, 7, -9, 10]
positives = list(filter(lambda x: x > 0, numbers))

print("Names sorted by length:", sorted_by_length)
print("Positive numbers:", positives)
