questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A) Python", "B) HTML", "C) C++", "D) Java"],
        "answer": "B"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A) Central Process Unit", "B) Central Processing Unit", "C) Computer Personal Unit", "D) Central Program Unit"],
        "answer": "B"
    }
]

score = 0

print("🧠 Welcome to the Quiz App!\n")

for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)

    user_answer = input("Your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer was {q['answer']}\n")

print(f"🎯 Final Score: {score} out of {len(questions)}")
