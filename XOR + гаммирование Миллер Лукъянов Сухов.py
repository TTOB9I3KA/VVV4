alphabet = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я',' ']
text = list(input("Введите строку, которую хотели бы зашфровать(расшифровать) используя только буквы нижнего регистра русского алфавита:  "))
a = 7
m = 34
Y = [0] * len(text)
Y[0] = 32
for i in range(1, (len(text))):
   Y[i] = (a * Y[i - 1]) % m
lst = []
i = 0
for i in range(len(text)):
    lst.append(alphabet.index(text[i]))

def шифр(key):
    crypt = []
    for i in range(len(text)):
        x = (lst[i] + Y[i]) % 34
        crypt.append(x)

    gotovo = []
    i = 0
    for i in range(len(crypt)):
        z = crypt[i]
        gotovo.append(alphabet[z])

    en_st = ""
    for letter in "".join(gotovo):
        en_st += chr(ord(letter) ^ key)
    return en_st

def расшифр(key):
    en_st = ""
    for letter in "".join(text):
        en_st += chr(ord(letter) ^ key)

    ls = list(en_st)
    ls1 = []
    for i in range(len(text)):
        ls1.append(alphabet.index(ls[i]))

    crypt = []
    for i in range(len(text)):
        x = (ls1[i] - Y[i] + 34) % 34
        crypt.append(x)

    gotovo = []
    i = 0
    for i in range(len(crypt)):
        z = crypt[i]
        gotovo.append(alphabet[z])
    return "".join(gotovo)

def crypt():
    key = int(input("Введите ключ шифрования: "))
    encr_line = шифр(key)
    print("Введенная строка ", "".join(text))
    print("Зашифрованное слово:  ", encr_line)


def recrypt():
    key = int(input("Введите ключ расшифрования: "))
    print("Введенная строка ", "".join(text))
    encr_line = расшифр(key)
    print("Разшифрованное слово:  ", encr_line)

def opt():
    op = int(input("0. Зашифровать строку\n1. Расшифровать строку\nop(0,1): "))
    if op == 0:
        print("_______________ЗАШИФРОВКА")
        crypt()
    elif op == 1:
        print("_______________РАСШИФРОВКА")
        recrypt()
    else:
        print("Вы ввели неверное значение.")
if __name__ == "__main__":
    opt()


