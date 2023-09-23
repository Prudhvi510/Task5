def most_frequent_character(input_string):
    # Create an empty dictionary to store character frequencies
    char_count = {}

    # Iterate through the characters in the input string
    for char in input_string:
        # Update the count for the current character in the dictionary
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Find the character with the highest frequency
    most_frequent = max(char_count, key=char_count.get)

    return most_frequent

# Example usage:
input_str = "Guvi geek network private limited"
result = most_frequent_character(input_str)
print("Most frequent character:", result)  # Output will depend on the input string