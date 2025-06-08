import requests

# Wikipedia API endpoint for Iban language
url = "https://iba.wikipedia.org/w/api.php"

# API parameters
params = {
    "action": "query",
    "format": "json",
    "prop": "extracts",
    "titles": "Jaku Iban",
    "explaintext": True,
    "redirects": 1
}

# Send the request
response = requests.get(url, params=params)
data = response.json()

# Extract text
page = next(iter(data["query"]["pages"].values()))
iban_text = page.get("extract", "")

# Save to .txt file
filename = "jaku_iban_wikipedia.txt"
with open(filename, "w", encoding="utf-8") as file:
    file.write(iban_text)

print(f"Saved clean Iban text to '{filename}'")

