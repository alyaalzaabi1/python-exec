def count_letter(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count

word = input("Enter a word: ")
letter = input("Enter a letter to count: ")
print(f"'{letter}' appears {count_letter(word, letter)} times in '{word}'.")
