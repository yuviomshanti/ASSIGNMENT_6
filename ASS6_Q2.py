def is_palindrome(string):
    # Remove whitespace and convert to lowercase
    string = string.replace(" ", "").lower()
    # Check if the reversed string is equal to the original string
    return string == string[::-1]

word = "madam"  # Example palindrome word
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")

phrase = "nurses run"  # Example palindrome phrase
if is_palindrome(phrase):
    print(f"{phrase} is a palindrome.")
else:
    print(f"{phrase} is not a palindrome.")
