# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример: - 45 -> 101101; - 3 -> 11; - 2 -> 10
binary = ''
n = int(input("Введите число для преобразования в двоичное: "))
while n > 0:
    binary = str(n%2) + binary
    n //= 2
print(binary)