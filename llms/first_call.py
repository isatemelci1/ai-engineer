
import os
import requests
from dotenv import load_dotenv


API_URL = "https://api.anthropic.com/v1/messages"
MODEL = "claude-haiku-5-5"


def main() -> None:
    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")

    if not api_key:
        print("Error: ANTHROPIC_API_KEY is not set.")
        return

    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    }

    messages = [
        {
            "role": "user",
            "content": "What is Python in 1 short sentence?",
        }
    ]

    body = {
        "model": MODEL,
        "max_tokens": 300,
        "messages": messages,
    }

    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json=body,
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()

    except requests.RequestException:
        print("Error: API request failed. Check your connection and API configuration.")
        return
    except ValueError:
        print("Error: API returned invalid JSON.")
        return

    # 1. Print the answer
    print("\n--- Answer ---")
    for block in data.get("content", []):
        if block.get("type") == "text":
            print(block["text"])

    # 2. Print token usage
    usage = data.get("usage", {})
    print("\n--- Usage ---")
    print(f"Input tokens:  {usage.get('input_tokens', 'unknown')}")
    print(f"Output tokens: {usage.get('output_tokens', 'unknown')}")

    # 3. Print the stop reason
    print("\n--- Stop reason ---")
    print(data.get("stop_reason", "unknown"))


if __name__ == "__main__":
    main()
