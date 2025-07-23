"""
Plagiarism Detector L

Compares two essays for common words, word frequency, and plagiarism percentage.


import string  # For removing punctuation
import sys     # For system-level error handling


def load_and_preprocess(filename):
    """
    Loads a text file, removes punctuation, lowercases, and splits into words.
    Returns a list of words.
    Handles FileNotFoundError and empty files.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
            if not text.strip():
                print(f"Error: '{filename}' is empty.")
                return []
            # Remove punctuation and convert to lowercase for uniformity
            translator = str.maketrans('', '', string.punctuation)
            text = text.translate(translator).lower()
            # Split into words, ignoring any blank entries
            words = [w for w in text.split() if w.strip()]
            return words
    except FileNotFoundError:
        # Handle missing file gracefully
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An error occurred while reading '{filename}': {e}")
        return []

def count_word_frequency(words):
    """
    Counts word frequency in a list of words.
    Returns a dictionary: {word: count}
    """
    freq = {}
    for word in words:
        # Increment count for each word
        freq[word] = freq.get(word, 0) + 1
    return freq

def print_essay_stats(words, essay_label):
    """
    Prints statistics about an essay (total and unique word counts).
    """
    print(f"\n{essay_label} Statistics:")
    print(f"  Total words: {len(words)}")
    print(f"  Unique words: {len(set(words))}")

def find_common_words(freq1, freq2):
    """
    Finds and prints words common to both essays, with their counts in each essay.
    """
    common = set(freq1) & set(freq2)  # Set intersection for common words
    if not common:
        print("No common words found.")
        return
    print("\nCommon Words:")
    print(f"{'Word':<15}{'Essay 1':<10}{'Essay 2':<10}")
    print("-"*37)
    for word in sorted(common):
        # Print word and its count in both essays
        print(f"{word:<15}{freq1[word]:<10}{freq2[word]:<10}")

def search_word(word, freq1, freq2):
    """
    Searches for a word in both essays and prints its counts.
    Returns False if not found in either essay.
    """
    if not word:
        print("Error: Empty input. Please enter a word.")
        return False
    w = word.lower()
    count1 = freq1.get(w, 0)
    count2 = freq2.get(w, 0)
    if count1 == 0 and count2 == 0:
        print(f"'{word}' not found in either essay.")
        return False
    # Print a clear, specific result statement
    print(f"The word '{word}' appears {count1} time(s) in Essay 1 and {count2} time(s) in Essay 2.")
    return True

def calculate_plagiarism_percentage(freq1, freq2):
    """
    Calculates and prints the plagiarism percentage using set intersection and union.
    Reports if plagiarism is detected (>=50%) or not.
    """
    set1 = set(freq1)
    set2 = set(freq2)
    intersection = set1 & set2
    union = set1 | set2
    if not union:
        print("Cannot calculate plagiarism: no words in essays.")
        return
    percentage = (len(intersection) / len(union)) * 100
    print(f"\nPlagiarism Percentage: {percentage:.2f}%")
    if percentage >= 50:
        print("Plagiarism Detected!")
    else:
        print("No Plagiarism Detected.")

def main():
    """
    Main function to run the plagiarism detector application.
    Loads essays, shows stats, finds common words, calculates plagiarism,
    and allows the user to search for specific words interactively.
    """
    print("\n==============================")
    print("    Plagiarism Detector Lab 2   ")
    print("==============================")
    print("Compare two essays for common words and plagiarism percentage.\n")

    essay1_file = 'essay-1.txt'  # First essay filename
    essay2_file = 'essay-2.txt'  # Second essay filename

    # Load and preprocess both essays
    words1 = load_and_preprocess(essay1_file)
    words2 = load_and_preprocess(essay2_file)
    if not words1 or not words2:
        print("Cannot proceed without both essays.")
        return
    # Count word frequencies for both essays
    freq1 = count_word_frequency(words1)
    freq2 = count_word_frequency(words2)

    # Print statistics for each essay
    print_essay_stats(words1, 'Essay 1')
    print_essay_stats(words2, 'Essay 2')

    # Find and display common words
    find_common_words(freq1, freq2)

    # Calculate and display plagiarism percentage
    print("\nChecking for plagiarism...")
    set1 = set(freq1)
    set2 = set(freq2)
    intersection = set1 & set2  # Words in both essays
    union = set1 | set2         # All unique words
    if not union:
        print("Cannot calculate plagiarism: no words in essays.")
        return
    percentage = (len(intersection) / len(union)) * 100
    print(f"Plagiarism Percentage: {percentage:.2f}%")
    if percentage >= 50:
        print("Result: Plagiarism Detected!")
    else:
        print("Result: No Plagiarism Detected.")

    # Word search functionality
    print("\n--- Word Search ---")
    print("Type a word to search for its count in both essays, or 'q' to quit.")
    while True:
        user_word = input("Enter word to search: ").strip()
        if user_word.lower() == 'q':
            print("Exiting word search.")
            break
        search_word(user_word, freq1, freq2)

    print("\nThank you for using the Plagiarism Detector!")

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
