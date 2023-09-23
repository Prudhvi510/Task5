def count_unique_characters(input_string):
    # Initialize an empty set to store unique characters
    unique_chars = set()
    
    # Iterate through each character in the input string
    for char in input_string:
        # Add the character to the set
        unique_chars.add(char)
    
    # Return the number of unique characters (size of the set)
    return len(unique_chars)

# Example usage:
input_str = "Guvi geek network private limited"
unique_count = count_unique_characters(input_str)
print("Number of unique characters:", unique_count)  # Output will be 18