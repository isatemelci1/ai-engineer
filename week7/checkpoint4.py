
import time
from collections.abc import Generator


def stream_sentence(sentence: str) -> Generator[str, None, None]:
    """Yield one word at a time with a short delay."""
    for word in sentence.split():
        time.sleep(0.5)
        yield word


def main() -> None:
    sentence = "Learning Python prepares us for streaming LLM responses"

    for word in stream_sentence(sentence):
        print(word, end=" ", flush=True)

    print()  # Finish with a newline


if __name__ == "__main__":
    main()
