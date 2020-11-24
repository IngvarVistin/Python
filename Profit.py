rev=int(input('Введите выручку фирмы '))
cost=int(input('Введите издержки фирмы '))
if rev>cost:
    prof=(rev - cost) / rev
    print('Фирма работает с прибылью. Рентабельность составила ',round(prof,2))
    empl=int(input("Сколько сотрудников работают на предприятии? "))
    print('Прибыль в расчете на 1 сотрудника составляет ',round((prof/empl),2))
elif rev==cost:
    print('Фирма отработала в ноль')
else:
    print('Фирма отработала в убылок!')
