
import json
from chat_request import chatRequest, processLLM
from system_rules import APP_SYSTEM_CONTENT
from thinking_dots import start_thinking_dots

def main():
    messages = [
        {
            "role":"system",
            "content": APP_SYSTEM_CONTENT
        }
    ]
    print("Phi-3 simple chat. Type 'exit' for quit")
    while True:
        user_input = input("You: ")
        if user_input == 'exit': 
            print('bye')
            break
        messages.append({"role": "user", "content": user_input})
        stopEvent = start_thinking_dots("Model Thinking", 0.5)
        reply = chatRequest(messages)
        stopEvent.set()
        response:dict = processLLM(reply)
        messages.append(response)
        print("\nAgent: ", response["content"] if response["role"] == "assistant" else json.loads(response["content"])["result"])
        print("_"*60)
if __name__ == "__main__":
    main()        
        