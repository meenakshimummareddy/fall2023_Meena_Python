import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from difflib import SequenceMatcher

# Initialize NLTK
nltk.download("punkt")
nltk.download("wordnet")


# Function to calculate similarity between two strings
def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()


# Medical knowledge base (simplified for demonstration)
medical_conditions = {
    "cold": "A common viral infection of the nose and throat.",
    "flu": "A contagious respiratory illness caused by influenza viruses.",
    "headache": "A pain in the head or upper neck.",
    # Add more medical conditions and information
}


# Function to perform symptom checking
def symptom_checker(symptoms):
    best_match = None
    max_similarity = 0

    for condition, description in medical_conditions.items():
        condition_tokens = word_tokenize(condition)
        similarity_score = max(similarity(symptoms, condition), similarity(symptoms, condition_tokens))

        if similarity_score > max_similarity:
            max_similarity = similarity_score
            best_match = (condition, description)

    return best_match


# Main program loop
while True:
    user_input = input("Please describe your symptoms (or 'exit' to quit): ").lower()

    if user_input == "exit":
        print("Goodbye!")
        break

    result = symptom_checker(user_input)

    if result:
        condition, description = result
        print(f"Possible condition: {condition}")
        print(f"Description: {description}")
    else:
        print("No matching condition found.")
