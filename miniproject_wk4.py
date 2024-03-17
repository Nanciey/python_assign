from difflib import get_close_matches

def get_definition(word):
    # Dictionary of words and their definitions
    dictionary = {
        "rain": "Moisture condensed from the atmosphere that falls visibly in separate drops.",
        "pot": "A container, typically rounded or cylindrical and of ceramic ware or metal, used for storage or cooking.",
        # Add more words and definitions as needed
    }
    
    # Convert the word to lowercase for case-insensitive matching
    word = word.lower()
    
    # Check if the word is in the dictionary
    if word in dictionary:
        return dictionary[word]
    else:
        # If the word is not found, try to find similar words
        similar_words = get_close_matches(word, dictionary.keys(), n=3, cutoff=0.8)
        
        if similar_words:
            suggestion = ", ".join(similar_words)
            return f"Word not found. Did you mean: {suggestion}?"
        else:
            return "Sorry, the word was not found in the dictionary and no similar words were found."

# Test the function
user_input = input("Enter a word: ")
definition = get_definition(user_input)
print(definition)
