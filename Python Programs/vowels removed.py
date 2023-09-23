def remove_vowels(input_string):
    # Define a string containing all vowels in both uppercase and lowercase
    vowels = "aeiouAEIOU"
    
    # Initialize an empty string to store the result
    result_string = ""
    
    # Iterate through each character in the input string
    for char in input_string:
        # If the character is not a vowel, add it to the result string
        if char not in vowels:
            result_string += char
    
    return result_string

# Example usage:
input_str = "Guvi  geeks network private limited"
output_str = remove_vowels(input_str)
print(output_str)  # Output will be " Gv gks ntwrk prvt lmtd"