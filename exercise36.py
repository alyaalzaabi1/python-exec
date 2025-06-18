import random

# Generate 10 random numbers
random_nums = [random.randint(1, 100) for _ in range(10)]
print("Random numbers:", random_nums)
print("Largest number:", max(random_nums))

# Simulate 100 dice rolls
doubles = 0
for _ in range(100):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    if die1 == die2:
        doubles += 1

print("Doubles in 100 rolls:", doubles)
