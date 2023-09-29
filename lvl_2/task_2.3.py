# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

def number (n):
    num = {
        0: 'Ноль',
        1: 'Один',
        2: 'Два',
        3: 'Три',
        4: 'Четыре',
        5: 'Пять',
        6: 'Шесть',
        7: 'Семь',
        8: 'Восемь',
        9: 'Девять'
    }
    try: return num[n]
    except KeyError: return 'None'

print(number(0))
print(number(100))
print(number(5))