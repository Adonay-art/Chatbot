import groq
import os
import time

# Optional: Load from .env file if needed
# from dotenv import load_dotenv
# load_dotenv()

# 1. Initialize Groq client with API key
client = groq.Groq(api_key="")
# OR use this line if using env variable:
# client = groq.Groq(api_key=os.getenv("GROQ_API_KEY"))

# 2. Ask user for their name and greet them
user_name = input("🤖 Yo human! What's your name, superhero? 🦸‍♂️🦸‍♀️: ")
print(f"🎉 Sup {user_name}! I'm ChatBot 3000 🤪 — half genius, half comedian, all yours. Type 'exit' if you wanna escape my awesomeness.\n")

# 3. Set up initial chat history
chat_history = [
    {"role": "system", "content": "You're a funny and sarcastic assistant who loves cracking jokes, using emojis, and keeping things light-hearted."}
]
# 4. Start the chat loop
while True:
    user_input = input(f"{user_name}: ")
    if user_input.lower() == 'exit':
        print("👋 Goodbye! It was great chatting with you.")
        break

    # Add user input to chat history
    chat_history.append({"role": "user", "content": user_input})

    # Simulate typing delay
    print("AI is typing", end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()

    # 5. Send request to Groq
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=chat_history
    )

    # 6. Get and print assistant's reply
    reply = response.choices[0].message.content
    print(f"🤖 {reply}\n")

    # Add assistant reply to chat history
    chat_history.append({"role": "assistant", "content": reply})
