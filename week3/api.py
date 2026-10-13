import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python3 api.py ArtistName")

try:
    response = requests.get(
    "https://itunes.apple.com/search",
    params={"entity": "song", "limit": 20, "term": sys.argv[1]},
    timeout=10,
)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    sys.exit(f"Network error: {e}")

#print(json.dumps(response.json(), indent=4))

data = response.json()

if data["results"] is not None:
    for result in data["results"]:
        print(result["trackName"])