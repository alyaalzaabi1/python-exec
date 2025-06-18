questions = {
    "What is the capital of France?": "a",
    "What is 5 + 3?": "b",
    "Which planet is known as the Red Planet?": "c",
    "What is the color of the sun?": "a",
    "Who wrote 'Hamlet'?": "d"
}

options = {
    "What is the capital of France?": ["a) Paris", "b) Rome", "c) Madrid", "d) Berlin"],
    "What is 5 + 3?": ["a) 6", "b) 8", "c) 10", "d) 5"],
    "Which planet is known as the Red Planet?": ["a) Venus", "b) Earth", "c) Mars", "d) Jupiter"],
    "What is the color of the sun?": ["a) Yellow", "b) Blue", "c) Green", "d) White"],
    "Who wrote 'Hamlet'?": ["a) Charles Dickens", "b) Mark Twain", "c) Jane Austen", "d) William Shakespeare"]
}

score = 0

for q in questions:
    print("\n" + q)
    for opt in options[q]:
        print(opt)
    answer = input("Your answer (a/b/c/d): ").lower()
    if answer == questions[q]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Correct answer: {questions[q]}")

print(f"\nFinal Score: {score}/5")
