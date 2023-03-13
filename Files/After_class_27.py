import re

file = open("sample1.txt")

number_words = 0

for line in file:

    words = re.findall(r'\b\w{6,}\b', line)
    number_words += len(words)

print(f"Number of words with at least six letters in the text: {number_words}")

file.close()