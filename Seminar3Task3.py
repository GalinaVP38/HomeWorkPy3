# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

num = int(input("Введите количество чисел в списке: "))
listA = []
newList = []
for i in range(num):
    listA.append(float(input(f'Введите вещественное число - {i+1} элемент:')))
print(listA)
for j in range(len(listA)):
    newList.append(listA[j]-int(listA[j]))
print(newList)
maxN = max(newList)
minN = min(newList)
print(maxN-minN)
