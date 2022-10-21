# Задайте число. Составьте список чисел Фибоначчи,
#  в том числе для отрицательных индексов. Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
k = abs(int(input("Введите число, количество чисел Фибоначчи: ")))
rowFibonac = [0, 1]
rowFibonacAnti = [1, 0]
for i in range(2, k+1):
    rowFibonac.append(rowFibonac[i-1]+rowFibonac[i-2])
    rowFibonacAnti.insert(0, rowFibonacAnti[1]-rowFibonacAnti[0])
if k == 0:
    print([0])
else:
    rowFibonacAnti.extend(rowFibonac[1:])
    print(rowFibonacAnti)
