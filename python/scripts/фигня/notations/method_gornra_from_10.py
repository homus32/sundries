num = input("Введите число в десятичной системе счисления >> ")
print("Доступные системы счисления -> " + ", ".join(list(map(str, range(2, 17)))))
notation = int(input("В какую систему вы хотите конвертировать свое число? >> "))

letters = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}

result = ""
last = int(num)

while last != 0:
    mod = last % notation
    result = str(letters.get(mod, mod)) + result
    last = last // notation

print(result)