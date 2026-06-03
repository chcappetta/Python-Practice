from openrouter import OpenRouter
import os
from tools.calculator import calc_script
from tools.weather import weather_script

def ai_response(client, messages):  
    response = client.chat.send(
        model="poolside/laguna-m.1:free",
        messages= messages)
    output = response.choices[0].message.content
    return output

def get_prompt(username):
    userinput= input(f"{username}: ")
    return userinput

def main():
    ai_name = "EDITH"
    user_name = input(f"{ai_name}: Welcome to ChristopherAI. What is your name? ")
    q1=input(f"{ai_name}: Hello {user_name}! Would you like to pick out a name for me? [y/n] ")
    if q1 == "y":
        ai_name = input("My New Name: ")
        print(f"{ai_name}: Awesome choice! I love my new name.")
    print() 
    print(f"{ai_name}: What would you like to ask me? I can give you temperature with /weather <city>, open calculator with /calc, and quick math with /math <num1> <+,-,*,/,%> <num2>. Type Quit to exit")
    print()
    messages = [
        {
            "role": "system",
            "content": f"You are a helpful AI assistant named {ai_name}."
        }
    ]
    while True:
        prompt = get_prompt(user_name)
        if prompt.lower() == "quit":
            break
        if "/weather" in prompt.lower():
            weather_script(ai_name)
            continue
        if "/math" in prompt.lower():
            calc_script(ai_name, "quick")
            continue
        if "/calc" in prompt.lower():
            calc_script(ai_name, "full")
            continue
        print()
        messages.append({
            "role": "user",
            "content": prompt
        })
        print(f"{ai_name}: Thinking...")
        client = OpenRouter(KEY)
        try:
            output = ai_response(client, messages)
        except Exception as e:
            output = f"Sorry, AI is unavailable: {e}. Other tools still available."
        print(f"{ai_name}:", output)
        messages.append({
            "role": "assistant",
            "content": output
        })

main()
