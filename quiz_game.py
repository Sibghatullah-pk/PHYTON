# print("Welcome to my very basic QUIZ Game")


# playing = input("Do you want to play? (yes/no): ").lower()
# if playing != "yes":
#     print("Okay, maybe next time!")
#     quit()

# print("great! Let's start the quiz! ")

# score = 0
# answer =input("What does CPU stand for? ").lower()

# if answer == "central processing unit":
#     print("Correct!")
#     score += 1
# else:
#     print("Incorrect! The correct answer is 'Central Processing Unit'.")

print("🎯 Welcome to my very basic QUIZ Game!")

playing = input("Do you want to play? (yes/no): ").strip().lower()
if playing != "yes":
    print("Okay, maybe next time! 👋")
    quit()

print("\nGreat! Let's start the quiz! 🚀\n")

score = 0
questions = [
    {"question": "What does CPU stand for? ", "answer": ["central processing unit", "cpu"]},
    {"question": "What does GPU stand for? ", "answer": ["graphics processing unit", "gpu"]},
    {"question": "What is the capital of France? ", "answer": ["paris"]},
    {"question": "Which planet is known as the Red Planet? ", "answer": ["mars"]},
]

for q in questions:
    answer = input(q["question"]).strip().lower()
    if answer in q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Incorrect! The correct answer is '{q['answer'][0].title()}'.")
    print()




print(f"🎯 You got {score} out of {len(questions)} correct!")
percentage = (score / len(questions)) * 100
print(f"📊 Your score: {percentage:.2f}%")

# Performance Feedback
if percentage == 100:
    print("🏆 Perfect! You’re a quiz master!")
elif percentage >= 50:
    print("👍 Good job! Keep learning!")
else:
    print("📚 You need to brush up on your knowledge!")












# import openai
# import random
# import json

# openai.api_key = "YOUR_OPENAI_API_KEY"

# def get_random_questions(num_questions=3):
#     prompt = f"""
#     Generate {num_questions} general knowledge quiz questions with answers in JSON format.
#     Example:
#     [
#         {{"question": "What is the capital of Japan?", "answer": "Tokyo"}},
#         {{"question": "What does HTTP stand for?", "answer": "Hypertext Transfer Protocol"}}
#     ]
#     """

#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": prompt}],
#         temperature=0.8
#     )

#     try:
#         return json.loads(response.choices[0].message["content"])
#     except json.JSONDecodeError:
#         print("Error decoding JSON from LLM.")
#         return []

# # Main game
# print("🎯 Welcome to the LLM-powered QUIZ Game!")
# play = input("Do you want to play? (yes/no): ").strip().lower()
# if play != "yes":
#     print("Maybe next time!")
#     quit()

# questions = get_random_questions(5)
# score = 0

# for q in questions:
#     answer = input(q["question"] + " ").strip().lower()
#     if answer == q["answer"].lower():
#         print("✅ Correct!")
#         score += 1
#     else:
#         print(f"❌ Incorrect! The correct answer was '{q['answer']}'.")
#     print()

# print(f"🎯 You scored {score}/{len(questions)}!")
