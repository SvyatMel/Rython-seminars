# 2.2[12]: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
import math
s=int(input('Введите сумму чисел X и Y: '))
p=int(input('Введите произведение чисел X и Y: '))
D=(pow(s,2))-4*p
Z=math.sqrt(D)
if D<0:
    print('К сожалению ,подходящих чисел нет!')
elif D==0:
    x=(2*p)/(s+Z)
    print(f"число х = {x} , число y = {x}")
else:
    x=(2*p)/(s+Z)
    y=(2*p)/(s-Z)
    print(f"число х = {x} , число y = {y}")




