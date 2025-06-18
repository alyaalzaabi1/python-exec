def shift_letters(word):
    shifted = ''
    for char in word:
        if char.isalpha():
            if char.lower() == 'z':
                shifted += 'a' if char.islower() else 'A'
            else:
                shifted += chr(ord(char) + 1)
        else:
            shifted += char
    return shifted

text = input("Enter a word: ")
print("Ciphered:", shift_letters(text))
