import requests
from tools import getWeather

URL: str = "http://localhost:11434/api/chat"
MODEL_NAME: str = "phi3"


def chatRequest(messages: list[dict]) -> str:
    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "stream": False
    }
    resp = requests.post(URL, json=payload)
    resp.raise_for_status()
    data = resp.json()
    return data["message"]["content"]


def main():
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistence. Answer briefly and clearly"
        }
    ]
    print("Phi-3 simple chat. Type 'exit' for quit")
    print("Type weather city")

    while True:
        user_input = input("You: ")

        if user_input == "exit":
            print("bye")
            break
        if user_input.startswith("/weather"):
            parts = user_input.split(maxsplit=1)
            if len(parts) == 1 or len(parts[1].strip()) == 0:
                print("Agent: please write city after /weather, e.g. /weather London")
                print("_" * 60)
                continue

            city = parts[1].strip()
            try:
                weather_info = getWeather(city)
                print("\nAgent (weather):")
                print(weather_info)
            except ValueError as e:
                print("\nAgent (weather error):", e)
            except RuntimeError as e:
                print("\nAgent (system error):", e)

            print("_" * 60)
            continue
        messages.append({"role": "user", "content": user_input})
        try:
            reply = chatRequest(messages)
        except requests.RequestException as e:
            print("Agent: request error:", e)
            print("_" * 60)
            continue

        messages.append({"role": "assistant", "content": reply})
        print("\nAgent:", reply)
        print("_" * 60)


if __name__ == "__main__":
    main()
