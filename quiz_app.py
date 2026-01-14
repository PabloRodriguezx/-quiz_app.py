print("📘 Welcome to the Python Quiz App")
print("--------------------------------")

questions = {
    "What is the capital of France?": {
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    "Which language is used for web development?": {
        "options": ["A. Python", "B. HTML", "C. Java", "D. All of these"],
        "answer": "D"
    },
    "Who developed Python?": {
        "options": ["A. Dennis Ritchie", "B. Guido van Rossum", "C. Elon Musk", "D. Mark Zuckerberg"],
        "answer": "B"
    },
    "What does CPU stand for?": {
        "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Computer Personal Unit", "D. Control Processing Unit"],
        "answer": "B"
    }
}

score = 0

for question, data in questions.items():
    print("\n" + question)
    for option in data["options"]:
        print(option)

    user_answer = input("Your answer (A/B/C/D): ").upper()

    if user_answer == data["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong! Correct answer is", data["answer"])

print("\n🎯 Quiz Finished!")
print(f"Your Score: {score}/{len(questions)}")

if score == len(questions):
    print("🏆 Excellent! Perfect score!")
elif score >= len(questions) // 2:
    print("👍 Good job!")
else:
    print("📚 Keep practicing!")