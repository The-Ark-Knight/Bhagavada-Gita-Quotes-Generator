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