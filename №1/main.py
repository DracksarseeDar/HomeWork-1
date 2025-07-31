# Расход каждого дня недели

print('Введите суммы затрат за неделю')
Monday = float(input('Затраты за Понедельник ='))
Tuesday = float(input("Затраты за Вторник  ="))
Wednesday = float(input("Затраты за Среду ="))
Thursday = float(input("Затраты за Четверг ="))
Friday = float(input("Затраты за Пятницу ="))
Saturday = float(input("Затраты за Субботу ="))
Sunday = float(input("Затраты за Воскресенье ="))

# Подсчёт общей суммы расходов
money_summ = Monday + Tuesday  + Wednesday + Thursday + Friday + Saturday + Sunday
print(f'Сумма ваших затрат за неделю {money_summ} сом')

# Подсчет среднего расхода

money_mid_summ = round(money_summ /7, 1)
print(f'средний расход за неделю {money_mid_summ} сом')

# Статусы

if money_mid_summ <= 500:
    print('Ваш статус - БРОНЗА')
elif money_mid_summ <= 1500:
    print('Ваш статус - СЕРЕБРО')
elif money_mid_summ <= 3500:
    print('Ваш статус - ЗОЛОТО')
else:
    print('Ваш статус - ПЛАТИНА')
