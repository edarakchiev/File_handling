def replace_special_char(txt_list):
    special_char = ["-", ",", ".", "!", "?"]
    for index in range(len(txt_list)):
        for index_el in range(len(txt_list[index])):
            if txt_list[index][index_el] in special_char:
                to_replace = txt_list[index][index_el]
                txt_list[index] = txt_list[index].replace(to_replace, "@")
    return txt_list


with open("text.txt", "r") as file:
    text_list = [el.rstrip() for el in file.readlines()]

text_list = replace_special_char(text_list)

for i in range(len(text_list)):
    text_list[i] = text_list[i].split()
    text_list[i].reverse()

for text in text_list:
    print(" ".join(text))
