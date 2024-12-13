
from actions import *
from data import *


village = []

yr = player["Сила"] + 1
sena = 10
senya = 25
seny = 15
yri = player["Ловкость"] + 1
lvlv = player["Ум"] + 1




while True:
    if player["spa"] <= 0:
        print('''Здравствуй путник что ты хочешь сделать?
        1 - Бой
        2 - Магазин
        3 - Прокачка
        4 - Эшхолд
        5 - Посмотреть статистику игрока
        6 - Механизмы
        7 - Сонное измерение''')
        variable = input()
        if variable == "1":
            fight()
        elif variable == "2":
            magazin()
        elif variable == "3":
            prokachka(yr,sena,senya,yri,seny,lvlv)
        elif variable == "4":
            eshxold()
        elif variable == "5":
            stat_player()
        elif variable == "6":
            mechanic()
        elif variable == "7":
            son()
    elif player["spa"] >= 1:
        print('''Здравствуй путник что ты хочешь сделать?
        1 - Бой
        2 - Магазин
        3 - Прокачка
        4 - Эшхолд
        5 - Посмотреть статистику игрока
        6 - Механизмы
        7 - Сонное измерение
        8 - Карманное измерение''')
        variable = input()
        if variable == "1":
            fight()
        elif variable == "2":
            magazin()
        elif variable == "3":
            prokachka(yr,sena,senya,yri,seny,lvlv)
        elif variable == "4":
            eshxold()
        elif variable == "5":
            stat_player()
        elif variable == "6":
            mechanic()
        elif variable == "7":
            son()
        elif variable == "8":
            malus()
    elif player["spa"] >= 2:
        print('''Здравствуй путник что ты хочешь сделать?
        1 - Бой
        2 - Магазин
        3 - Прокачка
        4 - Эшхолд
        5 - Посмотреть статистику игрока
        6 - Механизмы
        7 - Сонное измерение
        8 - Карманное измерение
        9 - Закончить прохождение''')
        variable = input()
        if variable == "1":
            fight()
        elif variable == "2":
            magazin()
        elif variable == "3":
            prokachka(yr,sena,senya,yri,seny,lvlv)
        elif variable == "4":
            eshxold()
        elif variable == "5":
            stat_player()
        elif variable == "6":
            mechanic()
        elif variable == "7":
            son()
        elif variable == "8":
            malus()
        elif variable == "9":
            end()

