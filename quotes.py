import json
import random

# Load the Bhagavad Gita JSON file
with open("verse.json", "r", encoding="utf-8") as f:
    gita = json.load(f)

# Define a function to get quotes from a specific chapter
def get_quotes_by_chapter(chapter_number):
    quotes = []
    for verse in gita:
        if "chapter_number" in verse and verse["chapter_number"] == chapter_number:
            quotes.append(verse["text"])
    return quotes

# Prompt the user to enter a chapter number
while True:
    try:
        chapter_number = int(input("Enter the chapter number to get quotes (1-18): "))
        if 1 <= chapter_number <= 18:
            break
        else:
            print("Invalid chapter number. Please enter a number between 1 and 18.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Get quotes from the specified chapter
quotes = get_quotes_by_chapter(chapter_number)

if not quotes:
    print(f"No quotes found for Chapter {chapter_number}.")
else:
    # Get a random quote from the specified chapter
    random_quote = random.choice(quotes)

    # Display the random quote
    print(random_quote)
