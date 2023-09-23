def longest_common_substring(str1, str2):
    # Initialize a table to store the lengths of common substrings
    # Initialize variables to keep track of the longest substring and its length
    m = len(str1)
    n = len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0
    end_index = 0

    # Populate the table while comparing characters in the strings
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i

    # Extract the longest common substring
    longest_common = str1[end_index - max_length:end_index]

    return longest_common

# Example usage:
string1 = "Guvi Geek "
string2 = " Geek guvi"
result = longest_common_substring(string1, string2)
print("Longest common substring:", result)  # Output will be "bcdefg"
