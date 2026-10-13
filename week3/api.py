import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python3 api.py ArtistName")

try:
    response = requests.get(
        "https://itunes.apple.com/search",
        params={
            "entity": "song",
            "limit": 20,
            "term": sys.argv[1]
        },
        timeout=10,
    )
    response.raise_for_status()

except requests.exceptions.RequestException as e:
    sys.exit(f"Network error: {e}")

data = response.json()

if not data["results"]:
    sys.exit("No tracks found.")

for result in data["results"]:
    print(result["trackName"])