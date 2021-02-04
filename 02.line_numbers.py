with open("text.txt", "r") as file:
    text = [txt.rstrip() for txt in file.readlines()]

punctuation_symbols = ["-", ",", ".", "!", "?", "'"]

for index in range(len(text)):
    symbols_count = 0
    character_count = 0
    for el in text[index]:
        if el in punctuation_symbols:
            symbols_count += 1
        elif el.isalpha():
            character_count += 1
    result = f"Line: {index + 1}: {text[index]} ({character_count})({symbols_count}) \n"
    with open("output.txt", "a") as output_file:
        output_file.write(result)