import os
import sys
from typing import Any

import requests
from dotenv import load_dotenv


API_URL = "https://api.anthropic.com/v1/messages"
ANTHROPIC_VERSION = "2023-06-01"
MODEL = "claude-haiku-5-5"
MAX_TOKENS = 1024
TIMEOUT_SECONDS = 30
SYSTEM_PROMPT = (
    "You are a concise assistant. "
    "Answer in plain text without Markdown formatting, "
    "because your answers are shown in a terminal. "
    "If you don't know something, say so instead of guessing."
)


def load_api_key() -> str:
    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")

    if not api_key:
        sys.exit("Error: ANTHROPIC_API_KEY is not set. Add it to your .env file.")
        
    return api_key


def build_headers(api_key: str) -> dict[str, str]:
    return {
        "x-api-key": api_key,
        "anthropic-version": ANTHROPIC_VERSION,
        "content-type": "application/json",
    }


def build_messages(question: str) -> list[dict[str, str]]:
    return [
        {"role": "user", "content": question},
    ]


def build_body(
    messages: list[dict[str, str]],
    system: str = SYSTEM_PROMPT,
) -> dict[str, Any]:
    return {
        "model": MODEL,
        "max_tokens": MAX_TOKENS,
        "system": system,
        "messages": messages,
    }


def extract_error_message(response: requests.Response) -> str:
    try:
        return response.json()["error"]["message"]
    except (ValueError, KeyError, TypeError):
        return response.text or "No details provided."


def send_request(headers: dict[str, str], body: dict[str, Any]) -> dict[str, Any]:
    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json=body,
            timeout=TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        return response.json()
    except requests.HTTPError:
        sys.exit(f"API error {response.status_code}: {extract_error_message(response)}")
    except requests.Timeout:
        sys.exit(f"Error: no response within {TIMEOUT_SECONDS} seconds.")
    except requests.ConnectionError:
        sys.exit("Error: could not connect to the API. Check your internet connection.")
    except requests.JSONDecodeError:
        sys.exit("Error: the API returned a response that isn't valid JSON.")
    except requests.RequestException:
        sys.exit("Error: the request failed for an unexpected reason.")


def extract_text(data: dict[str, Any]) -> str:
    texts = [
        block["text"]
        for block in data.get("content", [])
        if block.get("type") == "text"
    ]
    return "".join(texts)


def extract_stop_reason(data: dict[str, Any]) -> str:
    return data.get("stop_reason", "unknown")


def extract_usage(data: dict[str, Any]) -> tuple[int, int]:
    usage = data.get("usage", {})
    return usage.get("input_tokens", 0), usage.get("output_tokens", 0)


def main():
    question = input("Ask me anything: ").strip()
    if not question:
        sys.exit("Error: no question provided.")

    api_key = load_api_key()
    headers = build_headers(api_key)
    messages = build_messages(question)
    body = build_body(messages)

    data = send_request(headers, body)

    text = extract_text(data)
    if not text:
        print("\n[No answer: the model used its whole token budget before responding.]")
    else:
        print(f"\n{text}")
        if extract_stop_reason(data) == "max_tokens":
            print("\n[Warning: the answer was cut off at the token limit.]")

    input_tokens, output_tokens = extract_usage(data)
    print(f"\nUsage: {input_tokens} input tokens, {output_tokens} output tokens.")

if __name__ == "__main__":
    main()