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


