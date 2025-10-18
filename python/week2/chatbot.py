import openai

openai.api_key = "your api key"

print("Lala: Hello! I'm Lala, your chatbot. Type 'bye' to exit.")
while True:
    user = input("you: ")
    if user.lower() == "bye":
        print("Lala: Bye! Take care.")
        break
    
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant named Lala."},
                {"role": "user", "content": user}
            ]
        )

        bot_reply = response.choices[0].message.content
        print(f"Lala: {bot_reply}")

    except Exception as e:
        print(f"Lala: Error aaya bhai - {e}")