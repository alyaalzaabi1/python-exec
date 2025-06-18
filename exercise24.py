friends = ["Ali", "Fatima", "Hassan", "Sara", "Mohammed"]

with open("friends.txt", "w") as file:
    for friend in friends:
        file.write(friend + "\n")

print("Friends list written to friends.txt")

