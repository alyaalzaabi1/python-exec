def reverse_words(sentence):
    words = sentence.split()
    return ' '.join(reversed(words))

text = input("Enter a sentence: ")
print("Reversed:", reverse_words(text))
