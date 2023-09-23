def is_anagram(str1, str2):
    # Remove spaces and convert both strings to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if the sorted versions of the strings are equal
    return sorted(str1) == sorted(str2)

# Example usage:
string1 = "listen"
string2 = "silent"
result = is_anagram(string1, string2)
print("Are the strings anagrams?", result)  # Output will be Trues