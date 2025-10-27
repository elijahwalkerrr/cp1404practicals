"""
CP1404/CP5632 Practical
Word occurrences in a string
"""


get_text = input("Enter Text To Count Unique Word: ")
clean_text = get_text.replace(",", "").replace(".", "")
clean_text = clean_text.lower()
word_to_count = {}
for word in clean_text.split(" "):
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
print(word_to_count)
