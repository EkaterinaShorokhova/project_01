# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
import random
from random import sample
r_song = sample(my_favorite_songs,3)

print('Выбраны песни:', r_song)
Total = r_song [0][1] + r_song[1][1] + r_song[2][1]
print('Три песни звучат ', round(Total,1),'минут')

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
Songs = []
for key in my_favorite_songs_dict:
    value = my_favorite_songs_dict[key]
    myTuple = (key, value)
    Songs.append(myTuple)

r_song2 = sample(Songs,3)
print('Выбраны песни:', r_song2)
Total2 = r_song2 [0][1] + r_song2[1][1] + r_song2[2][1]
print('Три песни звучат ', round(Total2,1),'минут')
