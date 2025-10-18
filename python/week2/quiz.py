quiz = [
    {
        "question": "why shahrukh khan is famous for?",
        "option": ["A. Acting", "B. Hakla", "C. Dance", "D. Singing"],
        "answer": "B"
    },
    {
        "question": "why arjun kapoor is famous for?",
        "option": ["A. because he is not famous", "B. Hakla", "C. Dance", "D. Singing"],
        "answer": "A"
    }
]

score = 0

for i in quiz:
    print("\n"+i["question"])
    for option in i["option"]:
        print(option)

    while True:
        user = input("Enter your answer (A/B/C/D): ").strip().upper()
        if(user == "A" or user == "B" or user == "C" or user == "D"):
            if user == i["answer"]:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer is {i['answer']}")
            break
        else:
            print("Invalid option, Try again!")

print(f"\nYour score is: {score}/{len(quiz)}")