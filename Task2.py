# Найдите сумму трехзначного числа
print('Введите число: ')
x=int(input())
summ=0
while x>0:
    n=x%10
    summ+=n
    x=x//10

print(summ)