# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'
print(my_favorite_songs [:14])
print(my_favorite_songs [-13:])
print(my_favorite_songs [16:30])
print(my_favorite_songs [-26:-15])

x = my_favorite_songs.split(',')
print(x[0] + x[-1] + x[1] + x[-2])