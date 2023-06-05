import string

def is_pangram(sentence):
    # Create a set of lowercase alphabets
    alphabets = set(string.ascii_lowercase)
    # Remove whitespace and convert to lowercase
    sentence = sentence.replace(" ", "").lower()
    # Check if all alphabets are present in the sentence
    return set(sentence) >= alphabets

sentence = "The quick brown fox jumps over the lazy dog"  # Example pangram sentence
if is_pangram(sentence):
    print(f"{sentence} is a pangram.")
else:
    print(f"{sentence} is not a pangram.")
