try:
    a, b = list(map(int, input('Введите два числа через пробел ' '\n').split()))
    print('Результат деления 1-го на 2-й ', a/b )
except ZeroDivisionError:
    print ('На ноль делить нельзя')
