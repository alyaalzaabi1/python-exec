def count_vowels(sentence):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count

text = input("Enter a sentence: ")
print("Vowel count:", count_vowels(text))
