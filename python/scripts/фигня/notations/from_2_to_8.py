num = int(input("Введите число в двоичной системе счисления >> "))

table = {
    '000': '0',
    '001': '1',
    '010': '2',
    '011': '3',
    '100': '4',
    '101': '5',
    '110': '6',
    '111': '7'
}


def add_zero(number_str):
    return ("0" * (3 - len(number_str))) + number_str


result = ""

for i in "{:,}".format(num).split(","):
    if result == "":
        i = add_zero(i)

    result += table[i]

print(result)