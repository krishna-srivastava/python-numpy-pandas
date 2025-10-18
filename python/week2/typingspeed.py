import time
import random

def timetaken(a, b):
    time_taken = b - a
    print(f"\n⏱ Time taken: {round(time_taken, 2)} seconds")
    return time_taken

def wordpermin(sentence, times):
    word_type = len(sentence.split())
    wpm = (word_type / times) * 60
    print(f"🧠 Typing Speed: {round(wpm)} WPM")

def accuracy(original, sentence):
    originalword = original.split()
    typeword = sentence.split()
    count = 0

    for i in range(min(len(originalword), len(typeword))):
        if originalword[i] == typeword[i]:
            count += 1

    accuracy = (count / len(originalword)) * 100
    print(f"🎯 Accuracy: {round(accuracy, 2)}%")

easy = [
    "The quick brown fox jumps over the lazy dog",
    "Python is a powerful programming language",
    "Practice makes a man perfect",
    "Typing fast takes time and consistency",
    "Errors are part of the learning process",
    "Never stop learning and growing",
    "Code is like humor when you have to explain it it’s bad",
    "Stay focused and never give up",
    "Debugging is like being the detective in a crime movie",
    "A journey of a thousand miles begins with a single step",
    "Success is not final failure is not fatal",
    "Hard work beats talent when talent doesn’t work hard",
    "The only way to do great work is to love what you do",
    "In the middle of difficulty lies opportunity",
    "Simplicity is the soul of efficiency"
]
medium = [
    "Artificial intelligence is shaping the future of technology and innovation",
    "Keyboard shortcuts can significantly improve your typing productivity",
    "Learning to code requires patience practice and problem solving skills",
    "Machine learning models rely heavily on high quality training data",
    "Consistency is the key to mastering any new skill in life or work",
    "Proper posture and hand placement help reduce typing strain over time",
    "Debugging code is a crucial step in the software development process",
    "The internet has revolutionized communication education and commerce",
    "Typing with accuracy is more important than typing with speed initially",
    "Software engineering combines logic creativity and collaboration",
    "Always test your code thoroughly before final deployment",
    "Reading documentation helps you understand libraries and frameworks better",
    "Productivity increases when distractions are minimized during work",
    "Every expert was once a beginner who refused to give up",
    "A good developer never stops learning and improving their skills"
]
hard = [
    "In a world driven by relentless technological advancements, adaptability and continuous learning are the keys to survival and success.",
    "The ability to remain calm under pressure while debugging a complex piece of software is what separates good developers from great ones.",
    "Even the most experienced programmers spend countless hours perfecting their logic and eliminating minute syntax errors in large codebases.",
    "Success in any technical field demands discipline, dedication, and the willingness to dive deep into problems others are afraid to touch.",
    "As artificial intelligence continues to evolve, ethical considerations and responsible development have become more important than ever before.",
    "Typing quickly and accurately is not just a skill, it's an essential asset for anyone working in tech, writing, or creative professions.",
    "Long hours spent solving one stubborn bug often teach you more than a dozen hours of passive coding tutorials and online courses.",
    "Reading books, writing clean code, and collaborating with others are timeless habits that elevate a developer from average to excellent.",
    "While building scalable systems, one must consider not only performance and reliability but also maintainability and long-term costs.",
    "Keyboard mastery comes with deliberate practice, focusing on reducing mistakes and improving muscle memory through daily consistent effort.",
    "Balancing speed and accuracy while typing technical documentation requires both language proficiency and subject matter expertise.",
    "The most challenging aspect of learning programming is not understanding syntax, but building the mindset to solve real-world problems.",
    "A true craftsman in the digital age knows that perfect code is not written quickly, but thoughtfully and iteratively over time.",
    "Effective time management is critical when juggling tight deadlines, team communication, and writing efficient, bug-free code.",
    "In complex projects, understanding the problem deeply is often more valuable than jumping into a solution that only scratches the surface."
]

# 🔁 Main Loop
while True:
    print('''
Welcome to the Typing Speed Test!
1) Easy
2) Medium
3) Hard
''')

    try:
        choice = int(input("Choose your difficulty (1/2/3): "))
    except ValueError:
        print("❌ Please enter a valid number.\n")
        continue

    levels = {1: easy, 2: medium, 3: hard}

    if choice in levels:
        original = random.choice(levels[choice])
        print("Type the following sentence:\n")
        print(original, "\n")

        start_time = time.time()
        sentence = input("Type the above sentence: ")
        end_time = time.time()

        times = timetaken(start_time, end_time)
        wordpermin(sentence, times)
        accuracy(original, sentence)
    else:
        print("❌ Invalid choice. Please select 1, 2, or 3.\n")
        continue

    again = input("\n🔁 Do you want to try again? (y/n): ").lower()
    if again != 'y':
        print("\n👋 Thank you for using the Typing Speed Test! Goodbye!")
        break
