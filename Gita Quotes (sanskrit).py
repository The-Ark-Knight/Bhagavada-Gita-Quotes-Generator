import json
import random

def load_quotes(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            gita = json.load(f)
            if not isinstance(gita, list):
                raise ValueError("JSON data should be a list of quotes.")
            return gita
    except FileNotFoundError:
        raise FileNotFoundError("JSON file not found.")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format in the file.")

def get_random_quote(quotes):
    if not quotes:
        raise ValueError("No quotes found in the JSON data.")
    return random.choice(quotes)

def display_quote(quote):
    if isinstance(quote, dict):
        quote = quote.get("text", "")
    print(quote)

if __name__ == "__main__":
    try:
        quotes = load_quotes("verse.json")
        random_quote = get_random_quote(quotes)
        display_quote(random_quote)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")

import json
import random

# Load the Bhagavad Gita JSON file
with open("verse.json", "r", encoding="utf-8") as f:
    gita = json.load(f)

# Access the list of verses directly
quotes = gita  # In this data structure, "quotes" is the entire list of verses

# Get a random quote from the Bhagavad Gita
random_quote = random.choice(quotes)

# Access the text of the quote
quote_text = random_quote["text"]

# Display the random quote
print(quote_text)
