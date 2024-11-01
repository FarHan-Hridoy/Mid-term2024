def longest_word(sentence):
    words = sentence.split()  # Split the sentence into words
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

# Example usage
sentence = "Find the longest word in this sentence"
print(longest_word(sentence))  # Output should be "longest"