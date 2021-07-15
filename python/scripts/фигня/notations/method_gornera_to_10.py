num = input("Введите переводимое число >> ")
notation = int(input("Какая система счисления у вашего числа? >> "))

letters = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}

result = int(letters.get(num[0], num[0]))

for k, i in enumerate(num):

    if len(num) - 1 != k:
        result = result * notation + int(letters.get(num[k + 1], num[k + 1]))
    else:
        break

print(result)

# 1234₅ = ((1 * 5 + 2) * 5 + 3) * 5 + 4