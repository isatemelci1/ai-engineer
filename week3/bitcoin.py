import requests
import sys
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    api_key = os.getenv("COINCAP_API_KEY")
    if not api_key:
        sys.exit("Missing COINCAP_API_KEY. Add it to your .env file.")
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 bitcoin.py AMOUNT")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument must be a number.")

    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin",
            params={"apiKey": api_key},
            timeout=10,
        )
        response.raise_for_status()
    except requests.RequestException:
        sys.exit("Could not reach CoinCap")

    try:
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except (KeyError, ValueError):
        sys.exit("Unexpected response from CoinCap.")

    amount = bitcoins * price
    print(f"${amount:,.4f}")


if __name__ == "__main__":
    main()