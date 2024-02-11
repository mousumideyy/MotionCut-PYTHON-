# Function to count the number of words in a sentence or paragraph
def count_words(sentence):
    """
    Count the number of words in the input sentence.
    Returns:
    int: The number of words in the input.
    """
    if not sentence:  # Check if the input is empty
        return 0
    else:
        # Split the sentence by spaces to count words
        words = sentence.split()
        return len(words)

# User-friendly interface
def main():
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Please enter a sentence or paragraph: ")
    
    # Call the function to count words
    word_count = count_words(user_input)
    
    # Print the word count
    print("The number of words in the input:", word_count)

# Call the main function
if __name__ == "__main__":
    main()
