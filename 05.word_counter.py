import re


def get_word():
    with open("words.txt", "r") as file:
        return [line.split() for line in file.readlines()][0]


def get_text():
    with open("text.txt", "r") as file:
        text = "".join(file.readlines())
        pattern = r"[a-z']+"
        return re.findall(pattern, text.lower())


words = get_word()
text = get_text()

result = {}
for word in words:
    if word in text:
        result[word] = text.count(word)


for key, value in sorted(result.items(), key=lambda x: -x[1]):
    print(f"{key} - {value}")
