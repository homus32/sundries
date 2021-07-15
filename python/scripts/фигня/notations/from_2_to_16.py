num = input("Введите число в двоичной системе счисления >> ")

table = {
    '0000': '0',
    '0001': '1',
    '0010': '2',
    '0011': '3',
    '0100': '4',
    '0101': '5',
    '0110': '6',
    '1000': '8',
    '1001': '9',
    '1010': 'A',
    '1011': 'B',
    '1100': 'C',
    '1101': 'D',
    '1110': 'E',
    '1111': 'F'
}


def split_by_quarters(num_str):
    return [num_str[::-1][n:n + 4][::-1] for n in range(0, len(num_str), 4)][::-1]


def add_zero(number_str):
    return ("0" * (4 - len(number_str))) + number_str


result = ""

for i in split_by_quarters(num):
    if result == "":
        i = add_zero(i)

    result += table[i]

print(result)