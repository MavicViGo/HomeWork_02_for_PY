'''
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
'''
#Если я правильно понял условие ), первое решение через квадратное уровнение
'''
a+b = 9 s
a*b = 20 p
'''

#s = int(input('введите сумму чисел: '))
#p = int(input('введите произведение чисел: '))
#
# from math import sqrt
#sqDiscr = sqrt(s*s - 4*p)
#a = (s-sqDiscr)/2
#b = (s+sqDiscr)/2
#
#print(a, b)

#Второе решение через подбор и циклы
max_a = 1000
max_b = 1000
s = int(input('введите сумму чисел: '))
p = int(input('введите произведение чисел: '))

for a in range(max_a):
    for b in range(max_b):
        if a+b==s and a*b==p:
            print(a, b)