import string

def calculate_word_frequency(file_path):
    # Open the file and read its content
    with open(file_path, 'r') as file:
        text = file.read().lower()  # Convert text to lowercase to make counting case-insensitive

    # Remove punctuation from the text
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Split the text into words
    words = text.split()

    # Create a dictionary to store word frequency
    word_frequency = {}

    # Count the frequency of each word
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    # Sort the dictionary by frequency in descending order
    sorted_word_frequency = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

    return sorted_word_frequency
file_path = input("Enter the path to the text file: ")

try:
    word_frequency = calculate_word_frequency(file_path)
    total_words = sum(word[1] for word in word_frequency)

    print("Word Frequency and Count:")
    for word, frequency in word_frequency:
        print(f"{word}: {frequency}")

    print("\nTotal words in the file:", total_words)
except FileNotFoundError:
    print("File not found. Please enter a valid file path.")

