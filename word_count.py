str = "This is an awesome occasion. This has never happened before."

char_occur = {}

for char in str:
    char_occur[char] = char_occur.get(char, 0) + 1

print(char_occur)

word_occur = {}

for word in str.split():
    word_occur[word] = word_occur.get(word, 0) + 1

print(word_occur)