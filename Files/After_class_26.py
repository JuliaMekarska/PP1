import re

text = "To be or not to be, that is the question"

words = re.findall(r'\w+', text)

print(f"Number of words in the text: {len(words)}")
