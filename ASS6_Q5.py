def sort_hyphen_separated_sequence(sequence):
    words = sequence.split("-")
    sorted_words = sorted(words)
    sorted_sequence = "-".join(sorted_words)
    print(sorted_sequence)

sequence = "green-red-yellow-black-white"  # Example hyphen-separated sequence
sort_hyphen_separated_sequence(sequence)
