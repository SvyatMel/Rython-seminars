total=int(input('Введите число: '))
if total%2==0:
    x1=total/6
    x2=x1*4
    print(f"{x1} - {x2} - {x1}")
else:
    print('Введите четное число!')