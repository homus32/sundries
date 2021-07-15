#1337 Encoder | Decoder.
#Это только декодер 1337. Мне лень допиливать декодер. Программа изи, пишешь - отвечает. 
chars = {
    "eng": {
        "A": "/-|",
        "B": "8",
        "C": "(",
        "D": "|)",
        "E": "3",
        "F": "|=",
        "G": "6",
        "H": "|-|",
        "I": "|",
        "J": ")",
        "K": "|<",
        "L": "|_",
        "M": "|\/|",
        "N": "|\|",
        "O": "0",
        "P": "|>",
        "Q": "9",
        "R": "|2",
        "S": "$",
        "T": "+",
        "U": "|_|",
        "V": "\/",
        "W": "\X/",
        "X": "*",
        "Y": "'/",
        "Z": "2"
    },
    "word":{
        "AT": "8",
        "AND": "&",
        "FOR": "4",
        "MATE": "M8",
        "YOU": "U",
    },
    "rus":{
        "А": "/-|",
        "Б": "6",
        "В": "8",
        "Г": "r",
        "Д": "|)",
        "Е": "3",
        "Ё": "3",
        "Ж": ">|<",
        "З": "2",
        "И": "|/|",
        "Й": "|/|",
        "К": "|<",
        "Л": "J|",
        "М": "|\/|",
        "Н": "|-|",
        "О": "0",
        "П": "||",
        "Р": "|>",
        "С": "(",
        "Т": "7",
        "У": "'/",
        "Ф": "qp",
        "Х": "*",
        "Ц": "LL",
        "Ч": "'-|",
        "Ш": "LL|",
        "Щ": "LLL",
        "Ъ": "'b",
        "Ы": "b|",
        "Ь": "b",
        "Э": "€",
        "Ю": "|-0",
        "Я": "9|"
    }
}

mean = {
    'eng': "".join([key for key in chars["eng"]]),
    'rus': "".join([key for key in chars["rus"]])
}

def del_items_in_list(l,item):
    for _ in range(len(l)):
        for i in range(len(l)):
            ar = l[i]
            if not item != ar:
                del l[i]
                break
    return l

skip = 0

word = input(">>> ")
result = ""
mode = 1

if mode == 1:
    for i in range(len(word)):

        if skip != 0:
            skip -= 1
            continue

        for key in chars["word"]:
            if word[i:len(key)+i].upper() == key:
                result+=chars["word"][key]
                skip = len(key)-1
                break
        else:
            for key in mean:
                if word[i].upper() in mean[key]:
                    result+=chars[key][word[i].upper()]
                    break
            else:
                result+=word[i]

elif mode == 2: # |||>|/|837, |\/||/||>!
    options = []

    all_chars = {}

    all_chars.update(chars["eng"])
    all_chars.update(chars["rus"])
    all_chars.update(chars["word"])
    all_chars.update({" ":" "})

    while len(word) != 0:
        options.append([])
        for key in all_chars:
            pass
print(result)

