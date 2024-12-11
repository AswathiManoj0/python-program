def replace_first_char(s):
    if not s:  # Check for empty string
        return s
    first_char = s[0]  # Get the first character
    return s[0] + s[1:].replace(first_char, '$')  # Replace subsequent occurrences of first_char with '$'

# Example usage
input_string = input("Enter a string: ")
result = replace_first_char(input_string)
print(result)
