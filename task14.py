'''
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
'''

n = int(input('введите n: '))
i = 0
list = []
while 2**i < n:
    list.append(2**i)
    i=i+1
print(list)
