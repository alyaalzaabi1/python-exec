numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
average = total / len(numbers)
above_avg = [num for num in numbers if num > average]

print("Sum:", total)
print("Average:", average)
print("Numbers above average:", len(above_avg))
