def is_palindrome(input_string):
    # Remove spaces and convert the string to lowercase for case-insensitive comparison
    clean_string = input_string.replace(" ", "").lower()
    
    # Check if the cleaned string is equal to its reverse
    return clean_string == clean_string[::-1]

# Example usage:
input_str = "guvi geek"
result = is_palindrome(input_str)
if result:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")