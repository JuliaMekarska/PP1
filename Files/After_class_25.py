import re

text = "To be, or not to be, that is the question"

vowels = re.findall('[aeiou]', text)

print(f"Number of vowels in the text: {len(vowels)}")
