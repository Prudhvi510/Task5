def count_words(input_string):
    # Split the input string into words based on spaces
    words = input_string.split()
    
    # Count the number of words in the list
    word_count = len(words)
    
    return word_count

# Example usage:
input_str = "guvi geek network private limited."
result = count_words(input_str)
print("Number of words:", result)  # Output will be 5