from data import *
from time import sleep
from random import randint
from data import player
from data import enemy
from data import magazine


village = []



def stat_player():
    print(f'Игрок наносит {player["atk"]} урона')
    print(f'Игрок поглащает {player["def"]} урона')
    print(f'у игрока {player["xp"]} хп')
    print(f'У игрока {player["sparki"]} спарков')
    print(f'Уровень силы игрока - {player["Сила"]}')
    print(f'Уровень ума игрока - {player["Ум"]}')
    print(f'Уровень ловкости игрока - {player["Ловкость"]}')








def magazin():
    while True:
     print("Итак что вы хотите купить?")
     print("1 - броня")
     print("2 - мечи")
     print("3 - фонтан жизни")
     print("4 - зелья")
     print("Если вы хотите выйти то напишите 5")
     mag = input()
     if mag == "1":
          print("Хорошо давай посмотрим что тут у нас")
          print(f'{magazine["+def"]}')
          print("Что тебе тут понравилось?")
          mech = input()
          if mech == "1" or mech == "броня из подушек":
               print(f'Хорошо она даст тебе +{magazine["+def"]["Броня из подушек"]} def(защиты)')
               print(f'Для её покупки игроку нужно получить 11 уровень силы')
               print("Хочешь её купить за 5 спарков?")
               mechs = input()
               if mechs == "Да" or "да":
                    if player["sparki"] >= 5 and player["Сила"] >= 11:
                         player["def"] += magazine["+def"]["Броня из подушек"]
                         print(f'Покупка совершенна! Теперь ваша защита - {player["def"]}')
                         break
                    elif player["sparki"] <= 4:
                        print("К сожалению у вас не хватает денег")
                    elif player["Сила"] <= 11:
                        print("К сожалению вы недостаточно сильны")
          elif mech == "Броня медная" or mech == "броня медная":
               print(f'Хорошо она даст тебе +{magazine["+def"]["Броня медная"]} def(защиты)')
               print("Хочешь её купить за 20 спарков?")
               mechs = input()
               if mechs == "Да" or "да":
                    if player["sparki"] >= 20 and player["Сила"] >= 14:
                         player["def"] += magazine["+def"]["Броня медная"]
                         print(f'Покупка совершенна! Теперь ваша защита - {player["def"]}')
                         break
                    elif player["sparki"] <= 19:
                        print("К сожалению у вас не хватает денег")
                    elif player["Сила"] <= 14:
                        print("К сожалению вы недостаточно сильны")
          elif mech == "2" or mech == "броня железная":
               print(f'Хорошо она даст тебе +{magazine["+def"]["Броня железная"]} def(защиты)')
               print(f'Для её покупки игроку нужно получить 20 уровень силы')
               print("Хочешь её купить за 100 спарков?")
               mechs = input()
               if mechs == "Да" or "да":
                    if player["sparki"] >= 100 and player["Сила"] >= 20:
                         player["def"] += magazine["+def"]["Броня железная"]
                         print(f'Покупка совершенна! Теперь ваша защита - {player["def"]}')
                         break
                    elif player["sparki"] <= 99:
                        print("К сожалению у вас не хватает денег")
                    elif player["Сила"] <= 19:
                         print("К сожалению вы недостаточно сильны")
          elif mech == "3" or mech == "броня алмазная":
               print(f'Хорошо она даст тебе +{magazine["+def"]["Броня алмазная"]} def(защиты)')
               print(f'Для её покупки игроку нужно получить 27 уровень силы')
               print("Хочешь её купить за 300 спарков?")
               mechs = input()
               if mechs == "Да" or "да":
                    if player["sparki"] >= 300 and player["Сила"] >= 27:
                         player["def"] += magazine["+def"]["Броня алмазная"]
                         print(f'Покупка совершенна! Теперь ваша защита - {player["def"]}')
                         break
                    elif player["sparki"] <= 299:
                        print("К сожалению у вас не хватает денег")
                    elif player["Сила"] <= 26:
                         print("К сожалению вы недостаточно сильны")
          elif mech == "4" or mech == "броня незеритовая":
               print(f'Хорошо она даст тебе +{magazine["+def"]["Броня незеритовая"]} def(защиты)')
               print(f'Для её покупки игроку нужно получить 40 уровень силы')
               print("Хочешь её купить за 1000 спарков?")
               mechs = input()
               if mechs == "Да" or "да":
                    if player["sparki"] >= 1000 and player["Сила"] >= 40:
                         player["def"] += magazine["+def"]["Броня незеритовая"]
                         print(f'Покупка совершенна! Теперь ваша защита - {player["def"]}')
                         break
                    elif player["sparki"] <= 999:
                        print("К сожалению у вас не хватает денег")
                    elif player["Сила"] <= 39:
                         print("К сожалению вы недостаточно сильны")
          elif mech == "5" or mech == "Одежда JDH":
               print(f'Хорошо она даст тебе +{magazine["+def"]["Одежда JDH"]} def(защиты)')
               print(f'Для её покупки игроку нужно получить 60 уровень силы')
               print("Хочешь её купить за 9000 спарков?")
               mechs = input()
               if mechs == "Да" or "да":
                    if player["sparki"] >= 9000 and player["Сила"] >= 60:
                         player["def"] += magazine["+def"]["Одежда JDH"]
                         print(f'Покупка совершенна! Теперь ваша защита - {player["def"]}')
                         break
                    elif player["sparki"] <= 8999:
                        print("К сожалению у вас не хватает денег")
                    elif player["Сила"] <= 59:
                         print("К сожалению вы недостаточно сильны")
          elif mech == "6" or mech == "Очки Джонолошки":
               print(f'Хорошо она даст тебе +{magazine["+def"]["Очки Джонолошки"]} def(защиты)')
               print(f'Для её покупки игроку нужно получить 100 уровень силы')
               print("Хочешь её купить за 500000 спарков?")
               mechs = input()
               if mechs == "Да" or "да":
                    if player["sparki"] >= 500000 and player["Сила"] >= 100:
                         player["def"] += magazine["+def"]["Одежда JDH"]
                         print(f'Покупка совершенна! Теперь ваша защита - {player["def"]}')
                         break
                    elif player["sparki"] <= 499999:
                        print("К сожалению у вас не хватает денег")
                    elif player["Сила"] <= 99:
                         print("Вы недостаточно сильны")
     elif mag == "2":
          print("Хорошо давай посмотрим что тут у нас")
          print(f'{magazine["+atk"]}')
          print("Что тебе тут понравилось?")
          mech = input()
          if mech == "1" or mech == "старый меч":
               print(f'Хорошо она даст тебе +{magazine["+atk"]["Старый меч"]} atk(атаки)')
               print(f'Для её покупки игроку нужно получить 11 уровень силы и 11 уровень ловкости')
               print("Хочешь её купить за 10 спарков?")
               mechs = input()
               if mechs == "Да" or "да":
                    if player["sparki"] >= 10 and player["Сила"] >= 11 and player["Ловкость"] >= 11:
                         player["atk"] += magazine["+atk"]["Старый меч"]
                         print(f'Покупка совершенна! Теперь ваш atk - {player["atk"]}')
                         break
                    elif player["sparki"] <= 9:
                        print("К сожалению у вас не хватает денег")
                    elif player["Сила"] <= 10:
                         print("Вы недостаточно сильны")
                    elif player["Ловкость"] <= 10:
                         print("Вы недостаточно ловки")
          elif mech == "2" or mech == "медный меч":
               print(f'Хорошо она даст тебе +{magazine["+atk"]["Медный меч"]} atk(атаки)')
               print(f'Для её покупки игроку нужно получить 16 уровень силы и 14 уровень ловкости')
               print("Хочешь её купить за 70 спарков?")
               mechs = input()
               if mechs == "Да" or "да":
                    if player["sparki"] >= 70 and player["Сила"] >= 16 and player["Ловкость"] >= 14:
                         player["atk"] += magazine["+atk"]["Медный меч"]
                         print(f'Покупка совершенна! Теперь ваш atk - {player["atk"]}')
                         break
                    elif player["sparki"] <= 69:
                        print("К сожалению у вас не хватает денег")
                    elif player["Сила"] <= 15:
                         print("Вы недостаточно сильны")
                    elif player["Ловкость"] <= 13:
                         print("Вы недостаточно ловки")
          elif mech == "3" or mech == "стальной меч":
               print(f'Хорошо она даст тебе +{magazine["+atk"]["Стальной меч"]} atk(атаки)')
               print(f'Для её покупки игроку нужно получить 25 уровень силы и 20 уровень ловкости')
               print("Хочешь её купить за 150 спарков?")
               mechs = input()
               if mechs == "Да" or "да":
                    if player["sparki"] >= 150 and player["Сила"] >= 25 and player["Ловкость"] >= 20:
                         player["atk"] += magazine["+atk"]["Стальной меч"]
                         print(f'Покупка совершенна! Теперь ваш atk - {player["atk"]}')
                         break
                    elif player["sparki"] <= 149:
                        print("К сожалению у вас не хватает денег")
                    elif player["Сила"] <= 24:
                         print("Вы недостаточно сильны")
                    elif player["Ловкость"] <= 19:
                         print("Вы недостаточно ловки")
          elif mech == "4" or mech == "алмазный меч":
               print(f'Хорошо она даст тебе +{magazine["+atk"]["Алмазный меч"]} atk(атаки)')
               print(f'Для её покупки игроку нужно получить 37 уровень силы и 34 уровень ловкости')
               print("Хочешь её купить за 450 спарков?")
               mechs = input()
               if mechs == "Да" or "да":
                    if player["sparki"] >= 450 and player["Сила"] >= 37 and player["Ловкость"] >= 34:
                         player["atk"] += magazine["+atk"]["Алмазный меч"]
                         print(f'Покупка совершенна! Теперь ваш atk - {player["atk"]}')
                         break
                    elif player["sparki"] <= 449:
                        print("К сожалению у вас не хватает денег")
                    elif player["Сила"] <= 36:
                         print("Вы недостаточно сильны")
                    elif player["Ловкость"] <= 33:
                         print("Вы недостаточно ловки")
          elif mech == "5" or mech == "клинки":
               print(f'Хорошо она даст тебе +{magazine["+atk"]["Клинки Мрклштлакклара"]} atk(атаки)')
               print(f'Для её покупки игроку нужно получить 40 уровень силы и 50 уровень ловкости')
               print("Хочешь её купить за 6500 спарков?")
               mechs = input()
               if mechs == "Да" or "да":
                    if player["sparki"] >= 6500 and player["Сила"] >= 40 and player["Ловкость"] >= 50:
                         player["atk"] += magazine["+atk"]["Клинки Мрклштлакклара"]
                         print(f'Покупка совершенна! Теперь ваш atk - {player["atk"]}')
                         break
                    elif player["sparki"] <= 6499:
                        print("К сожалению у вас не хватает денег")
                    elif player["Сила"] <= 39:
                         print("Вы недостаточно сильны")
                    elif player["Ловкость"] <= 49:
                         print("Вы недостаточно ловки")
          elif mech == "6" or mech == "копьё Отца":
               print(f'Хорошо она даст тебе +{magazine["+atk"]["Копьё Отца"]} atk(атаки)')
               print(f'Для её покупки игроку нужно получить 90 уровень Ума и 80 уровень ловкости')
               print("Хочешь её купить за 52000 спарков?")
               mechs = input()
               if mechs == "Да" or "да":
                    if player["sparki"] >= 52000 and player["Ум"] >= 90 and player["Ловкость"] >= 80:
                         player["atk"] += magazine["+atk"]["Копьё Отца"]
                         print(f'Покупка совершенна! Теперь ваш atk - {player["atk"]}')
                         break
                    elif player["sparki"] <= 51999:
                        print("К сожалению у вас не хватает денег")
                    elif player["Сила"] <= 89:
                         print("Вы недостаточно Умны")
                    elif player["Ловкость"] <= 79:
                         print("Вы недостаточно ловки")
     elif mag == "3":
          print("Хорошо давай посмотрим что тут у нас")
          print(f'{magazine["+xp"]}')
          print("Что тебе тут понравилось?")
          mech = input()
          if mech == "1" or mech == "улучшение фонтана жизни":
               print(f'Хорошо она даст тебе +{magazine["+xp"]["Улучшение фонтана жизни"]} xp(жизней)')
               print("Хочешь её купить за 175 спарков?")
               mechs = input()
               if mechs == "Да" or "да":
                    if player["sparki"] >= 175:
                         player["atk"] += magazine["+xp"]["Улучшение фонтана жизни"]
                         print(f'Покупка совершенна! Теперь ваш xp - {player["xp"]}')
                         break
                    elif player["sparki"] <= 174:
                        print("К сожалению у вас не хватает денег")
               elif mechs == "Нет" or mechs == "нет":
                    print("Хорошо")
          elif mech == "2" or mech == "+улучшение фонтана жизни":
               print(f'Хорошо она даст тебе +{magazine["+xp"]["+Улучшение фонтана жизни"]} xp(жизней)')
               print("Хочешь её купить за 500 парков?")
               mechs = input()
               if mechs == "Да" or "да":
                    if player["sparki"] >= 500:
                         player["atk"] += magazine["+xp"]["+Улучшение фонтана жизни"]
                         print(f'Покупка совершенна! Теперь ваш xp - {player["xp"]}')
                         break
                    elif player["sparki"] <= 499:
                        print("К сожалению у вас не хватает денег")
               elif mechs == "Нет" or mechs == "нет":
                    print("Хорошо")
          elif mech == "3" or mech == "++улучшение фонтана жизни":
               print(f'Хорошо она даст тебе +{magazine["+xp"]["++Улучшение фонтана жизни"]} xp(жизней)')
               print("Хочешь её купить за 1500 парков?")
               mechs = input()
               if mechs == "Да" or "да":
                    if player["sparki"] >= 1500:
                         player["atk"] += magazine["+xp"]["++Улучшение фонтана жизни"]
                         print(f'Покупка совершенна! Теперь ваш xp - {player["xp"]}')
                         break
                    elif player["sparki"] <= 1499:
                        print("К сожалению у вас не хватает денег")
               elif mechs == "Нет" or mechs == "нет":
                    print("Хорошо")
          elif mech == "4" or mech == "+++улучшение фонтана жизни":
               print(f'Хорошо она даст тебе +{magazine["+xp"]["+++Улучшение фонтана жизни"]} xp(жизней)')
               print("Хочешь её купить за 500 парков?")
               mechs = input()
               if mechs == "Да" or "да":
                    if player["sparki"] >= 3500:
                         player["atk"] += magazine["+xp"]["+++Улучшение фонтана жизни"]
                         print(f'Покупка совершенна! Теперь ваш xp - {player["xp"]}')
                         break
                    elif player["sparki"] <= 3499:
                        print("К сожалению у вас не хватает денег")
               elif mechs == "Нет" or mechs == "нет":
                    print("Хорошо")
          elif mech == "5" or mech == "++++улучшение фонтана жизни":
               print(f'Хорошо она даст тебе +{magazine["+xp"]["++++Улучшение фонтана жизни"]} xp(жизней)')
               print("Хочешь её купить за 16000 парков?")
               mechs = input()
               if mechs == "Да" or "да":
                    if player["sparki"] >= 16000:
                         player["atk"] += magazine["+xp"]["++++Улучшение фонтана жизни"]
                         print(f'Покупка совершенна! Теперь ваш xp - {player["xp"]}')
                         break
                    elif player["sparki"] <= 15999:
                        print("К сожалению у вас не хватает денег")
               elif mechs == "Нет" or mechs == "нет":
                    print("Хорошо")
          elif mech == "6" or mech == "+++++улучшение фонтана жизни":
               print(f'Хорошо она даст тебе +{magazine["+xp"]["+++++Улучшение фонтана жизни"]} xp(жизней)')
               print("Хочешь её купить за 500000 парков?")
               mechs = input()
               if mechs == "Да" or "да":
                    if player["sparki"] >= 500000:
                         player["atk"] += magazine["+xp"]["+++++Улучшение фонтана жизни"]
                         print(f'Покупка совершенна! Теперь ваш xp - {player["xp"]}')
                         break
                    elif player["sparki"] <= 499999:
                        print("К сожалению у вас не хватает денег")
               elif mechs == "Нет" or mechs == "нет":
                    print("Хорошо")
     elif mag == "4":
          print("Хорошо давай посмотрим что тут у нас")
          print(f'{magazine["potion"]}')
          print("Что тебе тут понравилось?")
          mech = input()
          if mech == "1" or mech == "зелье силы":
            print(f'Хорошо оно умножит твою силу(atk) на {magazine["potion"]["Зелье силы"]["+lv"]}')
            print(f'Вы хотите купить зелье за {magazine["potion"]["Зелье силы"]["Cost"]} спарков')
            mech = input()
            if mech == "Да" or mech == "да":
                if player["sparki"] >= magazine["potion"]["Зелье силы"]["Cost"]:
                         player["atk"] * magazine["potion"]["Зелье силы"]["+lv"]
                         print(f'Покупка совершенна! Теперь ваш atk - {player["atk"]}')
                         break
                elif player["sparki"] <= 79999:
                        print("К сожалению у вас не хватает денег")
                elif mech == "Нет" or mech == "нет":
                    print("Хорошо")
          elif mech == "2" or mech == "зелье твёрдой кожи":
            print(f'Хорошо оно умножит твою защиту(def) на {magazine["potion"]["Зелье твёрдой кожи"]["+lv"]}')
            print(f'Вы хотите купить зелье за {magazine["potion"]["Зелье твёрдой кожи"]["Cost"]} спарков')
            mech = input()
            if mech == "Да" or mech == "да":
                if player["sparki"] >= magazine["potion"]["Зелье твёрдой кожи"]["Cost"]:
                         player["def"] * magazine["potion"]["Зелье твёрдой кожи"]["+lv"]
                         print(f'Покупка совершенна! Теперь ваш def - {player["def"]}')
                         break
                elif player["sparki"] <= 59999:
                        print("К сожалению у вас не хватает денег")
                elif mech == "Нет" or mech == "нет":
                    print("Хорошо")
          elif mech == "3" or mech == "зелье быстрого кровотока":
            print(f'Хорошо оно умножит твои жизни(xp) на {magazine["potion"]["Зелье быстрого кровотока"]["+lv"]}')
            print(f'Вы хотите купить зелье за {magazine["potion"]["Зелье быстрого кровотока"]["Cost"]} спарков')
            mech = input()
            if mech == "Да" or mech == "да":
                if player["sparki"] >= magazine["potion"]["Зелье быстрого кровотока"]["Cost"]:
                         player["xp"] * magazine["potion"]["Зелье быстрого кровотока"]["+lv"]
                         print(f'Покупка совершенна! Теперь ваш xp - {player["xp"]}')
                         break
                elif player["sparki"] <= 99999:
                        print("К сожалению у вас не хватает денег")
                elif mech == "Нет" or mech == "нет":
                    print("Хорошо")
     elif mag == "5":
          break



yr = player["Сила"] + 1

def prokachka(yr,sena,senya,yri,seny,lvlv):
    print(f'''Вот что вы можете прокачать:
1 - Сила, Уровень -  {player["Сила"]}
2 - Ловкость, Уровень - {player["Ловкость"]}
3 - Ум, Уровень - {player["Ум"]}''')
    prok = input()
    if prok == "1":
        print(f'Если вы хотите прокачать Силу до {yr} уровня то заплатите {sena}')
        print("Вы хотите купить новый уровень силы?")
        sen = input()
        if sen == "Да" or sen == "да":
            if sena >= player["sparki"]:
                 player["sparki"] -= sena
                 player["Сила"] += 1
                 sena += 26
                 print(f'Теперь ваша сила - {player["Сила"]}')
            elif player["sparki"] <= sena:
                 print("У вас нехватает спарков")
    elif prok == "2":
        print(f'Если вы хотите прокачать Ловкость до {yri} уровня то заплатите {senya}')
        print("Вы хотите купить новый уровень Ловкости?")
        sen = input()
        if sen == "Да" or sen == "да":
            if senya >= player["sparki"]:
                 player["sparki"] -= senya
                 player["Сила"] += 1
                 senya += 34
                 print(f'Теперь ваша Ловкость - {player["Ловкость"]}')
            elif player["sparki"] <= senya:
                 print("У вас нехватает спарков")
    elif prok == "3":
        print(f'Если вы хотите прокачать Ум до {lvlv} уровня то заплатите {seny}')
        print("Вы хотите купить новый уровень Ума?")
        sen = input()
        if sen == "Да" or sen == "да":
            if seny >= player["sparki"]:
                 player["sparki"] -= seny
                 player["Ум"] += 1
                 seny += 12
                 print(f'Теперь ваш ум - {player["Ум"]}')
            elif player["sparki"] <= seny:
                 print("У вас нехватает спарков")






















def eshxold():
     xpx = player["xp"]
     print("Перемещение в Эшхолд.")
     sleep(0.5)
     print("Перемещение в Эшхолд..")
     sleep(0.5)
     print("Перемещение в Эшхолд...")
     sleep(0.5)
     print("Перемещение в Эшхолд.")
     sleep(0.5)
     print("Перемещение в Эшхолд..")
     sleep(0.5)
     print("Перемещение в Эшхолд...")
     sleep(0.5)
     print("Вы переместились в Эшхолд")
     print("Здесь вы должны отбивать толпы заражённых чтобы спасти город, взамен с них вы можете выбить мечи,броню и тд.")
     print("Вы хотите отбить толпу заражённых?")
     vibor = input()
     if vibor == "Да" or "да":
        number = randint(3,5)
        print(f'В толпе вы насчитали {number} заражённых')
        sleep(0.5)
        print("В этой толпе находяться:")
        if number == 3:
             print("Заражённая мышь (2)")
             print("Заражённый")
             sleep(0.5)
             print("Заражённая мышь прыгнула на вас, бой с 1 противником начался!")
             while True:
                 round = randint(1,2)
                 if round == 1:
                    player["xp"] -= enemy["Заражённая мышь"]["atk"]
                 elif round == 2:
                        enemy["Заражённая мышь"]["xp"] -= player["atk"]
                 sleep(1)
                 print("Произошёл удар! ")
                 sleep(1)
                 print(f'Хп противника - {enemy["Заражённая мышь"]["xp"]}')
                 print(f'Ваше хп - {player["xp"]}')
                 if player["xp"] <= 0:
                    print("Вы проиграли")
                    print("Эшхолд смог отстоять нападение но учтите что однажды они не смогут победить их всех")
                    player["xp"] = xpx
                    break
                 elif enemy["Заражённая мышь"]["xp"] <= 0:
                    spark = randint(1,10)
                    print(f"Вы выйграли! Вы получили - {spark} спарков")
                    rand = randint(1,100)
                    if rand <= 40:
                         print("Вы ничего не получили с неё")
                    elif rand <= 41:
                         print("Поздравляю вы получили клинок Света!")
                         print("Вы получили +9000 урона!")
                         player["Сила"] += 9000
                    elif rand <= 61:
                         print("Вы получили заражённую скинтом плоть (её можно скормить Ваму)")
                    elif rand <= 100:
                          print("Вы ничего не получили")
                    player["sparki"] += spark
                    player["xp"] = xpx
                    sleep(0.7)
                    print("На вас набросилась 2 заражённая мышь!")
                    break
             while  True:
                round = randint(1,2)
                if round == 1:
                    player["xp"] -= enemy["Заражённая мышь"]["atk"]
                elif round == 2:
                        enemy["Заражённая мышь"]["xp"] -= player["atk"]
                sleep(1)
                print("Произошёл удар! ")
                sleep(1)
                print(f'Хп противника - {enemy["Заражённая мышь"]["xp"]}')
                print(f'Ваше хп - {player["xp"]}')
                if player["xp"] <= 0:
                    print("Вы проиграли")
                    print("Эшхолд смог отстоять нападение но учтите что однажды они не смогут победить их всех")
                    player["xp"] = xpx
                    break
                elif enemy["Заражённая мышь"]["xp"] <= 0:
                    spark = randint(1,10)
                    print(f"Вы выйграли! Вы получили - {spark} спарков")
                    rand = randint(1,100)
                    if rand <= 40:
                     print("Вы ничего не получили с неё")
                    elif rand <= 41:
                     print("Поздравляю вы получили клинок Света!")
                     print("Вы получили +9000 урона!")
                     player["Сила"] += 9000
                    elif rand <= 61:
                     print("Вы получили заражённую скинтом плоть (её можно скормить Ваму)")
                    elif rand <= 100:
                     print("Вы ничего не получили")
                    player["sparki"] += spark
                    player["xp"] = xpx
                    sleep(0.7)
                    print("На вас надвигается заражённый, берегитесь!")
                    break
             while True:
                round = randint(1,2)
                if round == 1:
                    player["xp"] -= enemy["Заражённый"]["atk"]
                elif round == 2:
                        enemy["Заражённый"]["xp"] -= player["atk"]
                sleep(1)
                print("Произошёл удар! ")
                sleep(1)
                print(f'Хп противника - {enemy["Заражённый"]["xp"]}')
                print(f'Ваше хп - {player["xp"]}')
                if player["xp"] <= 0:
                    print("Вы проиграли")
                    print("Эшхолд смог отстоять нападение но учтите что однажды они не смогут победить их всех")
                    player["xp"] = xpx
                    break
                elif enemy["Заражённая мышь"]["xp"] <= 0:
                    spark = randint(1,10)
                    print(f"Вы выйграли! Вы получили - {spark} спарков")
                    rand = randint(1,100)
                    if rand <= 40:
                         print("Вы ничего не получили с неё")
                elif rand <= 41:
                     print("Поздравляю вы получили клинок Света!")
                     print("Вы получили +9000 урона!")
                     player["Сила"] += 9000
                elif rand <= 61:
                     print("Вы получили заражённую скинтом плоть (её можно скормить Ваму)")
                elif rand <= 100:
                     print("Вы ничего не получили")
                player["sparki"] += spark
                player["xp"] = xpx
                spirk = randint(100,999)
                print(f"За то что вы защитили Эшхолд жители решили заплатить вам {spirk} спарков")
                player["sparki"] += spirk
                break
        elif number == 4:
             print("Заражённая мышь (2)")
             print("Заражённый (2)")
             sleep(0.5)
             print("Заражённая мышь прыгнула на вас, бой с 1 противником начался!")
             round = randint(1,2)
             if round == 1:
                player["xp"] -= enemy["Заражённая мышь"]["atk"]
             elif round == 2:
                    enemy["Заражённая мышь"]["xp"] -= player["atk"]
             sleep(1)
             print("Произошёл удар! ")
             sleep(1)
             print(f'Хп противника - {enemy["Заражённая мышь"]["xp"]}')
             print(f'Ваше хп - {player["xp"]}')
             if player["xp"] <= 0:
                print("Вы проиграли")
                print("Эшхолд смог отстоять нападение но учтите что однажды они не смогут победить их всех")
                player["xp"] = xpx
             elif enemy["Заражённая мышь"]["xp"] <= 0:
                spark = randint(1,10)
                print(f"Вы выйграли! Вы получили - {spark} спарков")
                rand = randint(1,100)
                if rand <= 40:
                     print("Вы ничего не получили с неё")
                elif rand <= 41:
                     print("Поздравляю вы получили клинок Света!")
                     print("Вы получили +9000 урона!")
                     player["Сила"] += 9000
                elif rand <= 61:
                     print("Вы получили заражённую скинтом плоть (её можно скормить Ваму)")
                elif rand <= 100:
                     print("Вы ничего не получили")
                player["sparki"] += spark
                player["xp"] = xpx
                sleep(0.7)
                print("На вас набросился 2 заражённая мышь!")
                round = randint(1,2)
             if round == 1:
                player["xp"] -= enemy["Заражённая мышь"]["atk"]
             elif round == 2:
                    enemy["Заражённая мышь"]["xp"] -= player["atk"]
             sleep(1)
             print("Произошёл удар! ")
             sleep(1)
             print(f'Хп противника - {enemy["Заражённая мышь"]["xp"]}')
             print(f'Ваше хп - {player["xp"]}')
             if player["xp"] <= 0:
                print("Вы проиграли")
                print("Эшхолд смог отстоять нападение но учтите что однажды они не смогут победить их всех")
                player["xp"] = xpx
             elif enemy["Заражённая мышь"]["xp"] <= 0:
                spark = randint(1,10)
                print(f"Вы выйграли! Вы получили - {spark} спарков")
                rand = randint(1,100)
                if rand <= 40:
                     print("Вы ничего не получили с неё")
                elif rand <= 41:
                     print("Поздравляю вы получили клинок Света!")
                     print("Вы получили +9000 урона!")
                     player["Сила"] += 9000
                elif rand <= 61:
                     print("Вы получили заражённую скинтом плоть (её можно скормить Ваму)")
                elif rand <= 100:
                     print("Вы ничего не получили")
                player["sparki"] += spark
                player["xp"] = xpx
                sleep(0.7)
                print("На вас надвигается заражённый, берегитесь!")
                round = randint(1,2)
             if round == 1:
                player["xp"] -= enemy["Заражённый"]["atk"]
             elif round == 2:
                    enemy["Заражённый"]["xp"] -= player["atk"]
             sleep(1)
             print("Произошёл удар! ")
             sleep(1)
             print(f'Хп противника - {enemy["Заражённый"]["xp"]}')
             print(f'Ваше хп - {player["xp"]}')
             if player["xp"] <= 0:
                print("Вы проиграли")
                print("Эшхолд смог отстоять нападение но учтите что однажды они не смогут победить их всех")
                player["xp"] = xpx
             elif enemy["Заражённая мышь"]["xp"] <= 0:
                spark = randint(1,10)
                print(f"Вы выйграли! Вы получили - {spark} спарков")
                rand = randint(1,100)
                if rand <= 40:
                     print("Вы ничего не получили с неё")
                elif rand <= 41:
                     print("Поздравляю вы получили клинок Света!")
                     print("Вы получили +9000 урона!")
                     player["Сила"] += 9000
                elif rand <= 61:
                     print("Вы получили заражённую скинтом плоть (её можно скормить Ваму)")
                elif rand <= 100:
                     print("Вы ничего не получили")
                player["sparki"] += spark
                player["xp"] = xpx
                print("На вас надвигается второй заражённый, берегитесь!")
                round = randint(1,2)
             if round == 1:
                player["xp"] -= enemy["Заражённый"]["atk"]
             elif round == 2:
                    enemy["Заражённый"]["xp"] -= player["atk"]
             sleep(1)
             print("Произошёл удар! ")
             sleep(1)
             print(f'Хп противника - {enemy["Заражённый"]["xp"]}')
             print(f'Ваше хп - {player["xp"]}')
             if player["xp"] <= 0:
                print("Вы проиграли")
                print("Эшхолд смог отстоять нападение но учтите что однажды они не смогут победить их всех")
                player["xp"] = xpx
             elif enemy["Заражённая мышь"]["xp"] <= 0:
                spark = randint(1,10)
                print(f"Вы выйграли! Вы получили - {spark} спарков")
                rand = randint(1,100)
                if rand <= 40:
                     print("Вы ничего не получили с неё")
                elif rand <= 41:
                     print("Поздравляю вы получили клинок Света!")
                     print("Вы получили +9000 урона!")
                     player["Сила"] += 9000
                elif rand <= 61:
                     print("Вы получили заражённую скинтом плоть (её можно скормить Ваму)")
                elif rand <= 100:
                     print("Вы ничего не получили")
                player["sparki"] += spark
                player["xp"] = xpx
                spirk = randint(100,1100)
                print(f"За то что вы защитили Эшхолд жители решили заплатить вам {spirk} спарков")
                player["sparki"] += spirk
        elif number == 5:
             print("Заражённая мышь (2)")
             print("Червь переросток (2)")
             print("Заражённый (2)")
             sleep(0.5)
             print("Заражённая мышь прыгнула на вас, бой с 1 противником начался!")
             round = randint(1,2)
             if round == 1:
                player["xp"] -= enemy["Заражённая мышь"]["atk"]
             elif round == 2:
                    enemy["Заражённая мышь"]["xp"] -= player["atk"]
             sleep(1)
             print("Произошёл удар! ")
             sleep(1)
             print(f'Хп противника - {enemy["Заражённая мышь"]["xp"]}')
             print(f'Ваше хп - {player["xp"]}')
             if player["xp"] <= 0:
                print("Вы проиграли")
                print("Эшхолд смог отстоять нападение но учтите что однажды они не смогут победить их всех")
                player["xp"] = xpx
             elif enemy["Заражённая мышь"]["xp"] <= 0:
                spark = randint(1,10)
                print(f"Вы выйграли! Вы получили - {spark} спарков")
                rand = randint(1,100)
                if rand <= 40:
                     print("Вы ничего не получили с неё")
                elif rand <= 41:
                     print("Поздравляю вы получили клинок Света!")
                     print("Вы получили +9000 урона!")
                     player["Сила"] += 9000
                elif rand <= 61:
                     print("Вы получили заражённую скинтом плоть (её можно скормить Ваму)")
                elif rand <= 100:
                     print("Вы ничего не получили")
                player["sparki"] += spark
                player["xp"] = xpx
                sleep(0.7)
                print("На вас набросилась 2 заражённая мышь!")
                round = randint(1,2)
             if round == 1:
                player["xp"] -= enemy["Заражённая мышь"]["atk"]
             elif round == 2:
                    enemy["Заражённая мышь"]["xp"] -= player["atk"]
             sleep(1)
             print("Произошёл удар! ")
             sleep(1)
             print(f'Хп противника - {enemy["Заражённая мышь"]["xp"]}')
             print(f'Ваше хп - {player["xp"]}')
             if player["xp"] <= 0:
                print("Вы проиграли")
                print("Эшхолд смог отстоять нападение но учтите что однажды они не смогут победить их всех")
                player["xp"] = xpx
             elif enemy["Заражённая мышь"]["xp"] <= 0:
                spark = randint(1,10)
                print(f"Вы выйграли! Вы получили - {spark} спарков")
                rand = randint(1,100)
                if rand <= 40:
                     print("Вы ничего не получили с неё")
                elif rand <= 41:
                     print("Поздравляю вы получили клинок Света!")
                     print("Вы получили +9000 урона!")
                     player["Сила"] += 9000
                elif rand <= 61:
                     print("Вы получили заражённую скинтом плоть (её можно скормить Ваму)")
                elif rand <= 100:
                     print("Вы ничего не получили")
                player["sparki"] += spark
                player["xp"] = xpx
                sleep(0.7)
                print("Земля под вами наччинает трястись, на вас надвигается червь переросток берегитесь!")
             round = randint(1,2)
             if round == 1:
                player["xp"] -= enemy["Червь переросток"]["atk"]
             elif round == 2:
                    enemy["Червь переросток"]["xp"] -= player["atk"]
             sleep(1)
             print("Произошёл удар! ")
             sleep(1)
             print(f'Хп противника - {enemy["Червь переросток"]["xp"]}')
             print(f'Ваше хп - {player["xp"]}')
             if player["xp"] <= 0:
                print("Вы проиграли")
                print("Эшхолд смог отстоять нападение но учтите что однажды они не смогут победить их всех")
                player["xp"] = xpx
             elif enemy["Заражённая мышь"]["xp"] <= 0:
                spark = randint(1,10)
                print(f"Вы выйграли! Вы получили - {spark} спарков")
                rand = randint(1,100)
                if rand <= 40:
                     print("Вы ничего не получили с неё")
                elif rand <= 41:
                     print("Поздравляю вы получили клинок Света!")
                     print("Вы получили +9000 урона!")
                     player["Сила"] += 9000
                elif rand <= 61:
                     print("Вы получили заражённую скинтом плоть (её можно скормить Ваму)")
                elif rand <= 100:
                     print("Вы ничего не получили")
                player["sparki"] += spark
                player["xp"] = xpx
                print("Земля под вами наччинает ломаться, на вас надвигается второй червь переросток берегитесь!")
             round = randint(1,2)
             if round == 1:
                player["xp"] -= enemy["Червь переросток"]["atk"]
             elif round == 2:
                    enemy["Червь переросток"]["xp"] -= player["atk"]
             sleep(1)
             print("Произошёл удар! ")
             sleep(1)
             print(f'Хп противника - {enemy["Червь переросток"]["xp"]}')
             print(f'Ваше хп - {player["xp"]}')
             if player["xp"] <= 0:
                print("Вы проиграли")
                print("Эшхолд смог отстоять нападение но учтите что однажды они не смогут победить их всех")
                player["xp"] = xpx
             elif enemy["Заражённая мышь"]["xp"] <= 0:
                spark = randint(1,10)
                print(f"Вы выйграли! Вы получили - {spark} спарков")
                rand = randint(1,100)
                if rand <= 40:
                     print("Вы ничего не получили с неё")
                elif rand <= 41:
                     print("Поздравляю вы получили клинок Света!")
                     print("Вы получили +9000 урона!")
                     player["Сила"] += 9000
                elif rand <= 61:
                     print("Вы получили заражённую скинтом плоть (её можно скормить Ваму)")
                elif rand <= 100:
                     print("Вы ничего не получили")
                player["sparki"] += spark
                player["xp"] = xpx
                sleep(0.7)
                print("На вас набросился 2 заражённая мышь!")
                round = randint(1,2)
             if round == 1:
                player["xp"] -= enemy["Заражённый"]["atk"]
             elif round == 2:
                    enemy["Заражённый"]["xp"] -= player["atk"]
             sleep(1)
             print("Произошёл удар! ")
             sleep(1)
             print(f'Хп противника - {enemy["Заражённый"]["xp"]}')
             print(f'Ваше хп - {player["xp"]}')
             if player["xp"] <= 0:
                print("Вы проиграли")
                print("Эшхолд смог отстоять нападение но учтите что однажды они не смогут победить их всех")
                player["xp"] = xpx
             elif enemy["Заражённая мышь"]["xp"] <= 0:
                spark = randint(1,10)
                print(f"Вы выйграли! Вы получили - {spark} спарков")
                rand = randint(1,100)
                if rand <= 40:
                     print("Вы ничего не получили с неё")
                elif rand <= 41:
                     print("Поздравляю вы получили клинок Света!")
                     print("Вы получили +9000 урона!")
                     player["Сила"] += 9000
                elif rand <= 61:
                     print("Вы получили заражённую скинтом плоть (её можно скормить Ваму)")
                elif rand <= 100:
                     print("Вы ничего не получили")
                player["sparki"] += spark
                player["xp"] = xpx
                print("На вас надвигается второй заражённый, берегитесь!")
                round = randint(1,2)
             if round == 1:
                player["xp"] -= enemy["Заражённый"]["atk"]
             elif round == 2:
                    enemy["Заражённый"]["xp"] -= player["atk"]
             sleep(1)
             print("Произошёл удар! ")
             sleep(1)
             print(f'Хп противника - {enemy["Заражённый"]["xp"]}')
             print(f'Ваше хп - {player["xp"]}')
             if player["xp"] <= 0:
                print("Вы проиграли")
                print("Эшхолд смог отстоять нападение но учтите что однажды они не смогут победить их всех")
                player["xp"] = xpx
             elif enemy["Заражённая мышь"]["xp"] <= 0:
                spark = randint(1,10)
                print(f"Вы выйграли! Вы получили - {spark} спарков")
                rand = randint(1,100)
                if rand <= 40:
                     print("Вы ничего не получили с неё")
                elif rand <= 41:
                     print("Поздравляю вы получили клинок Света!")
                     print("Вы получили +9000 урона!")
                     player["Сила"] += 9000
                elif rand <= 61:
                     print("Вы получили заражённую скинтом плоть (её можно скормить Ваму)")
                elif rand <= 100:
                     print("Вы ничего не получили")
                player["sparki"] += spark
                player["xp"] = xpx
                spirk = randint(100,1100)
                print(f"За то что вы защитили Эшхолд жители решили заплатить вам {spirk} спарков")
                player["sparki"] += spirk
             









def mechanic():
     print("Итак какие механизмы вы хотите купить?")
     print(magazine["Механизмы"])
     print("Что вам тут понравилось?")
     near = input()
     if near == "авто":
        print("Она в разработке")
     elif near == "Перемотка времени":
          print("Хорошо она стоит 25к спарков")
          mon = input()
          if mon == "Да" or mon == "да":
               if player["sparki"] >= 25000:
                    print("Спасибо что купили перемотку времени!")
                    player["time"] += 1
               elif player["sparki"] <= 24999:
                    print("Вам не хватает спарков")
     else:
          print("Пока не хочу это делать")
             






def mouse():
    xpx = player["xp"]
    print(f'статистика заражённой мыши {enemy["Заражённая мышь"]}') 
    print("Хоршо давайте начнём")
    print(f'Ваше хп - {player["xp"]}')
    print(f'Ваша защита - {player["def"]}')
    print(f'Ваша атака- {player["atk"]}')
    print()
    while True:
        round = randint(1,2)
        if round == 1:
            player["xp"] -= enemy["Заражённая мышь"]["atk"]
        elif round == 2:
            enemy["Заражённая мышь"]["xp"] -= player["atk"]
        sleep(1)
        print("Произошёл удар! ")
        print(f'Хп противника - {enemy["Заражённая мышь"]["xp"]}')
        print(f'Ваше хп - {player["xp"]}')
        if player["xp"] <= 0:
            print("Вы проиграли")
            player["xp"] = xpx
            enemy["Заражённая мышь"]["xp"] = 10
            break
        elif enemy["Заражённая мышь"]["xp"] <= 0:
            spark = randint(1,10)
            print(f"Вы выйграли! Вы получили - {spark} спарков")
            player["sparki"] += spark
            if player["lvl"] == 1:
                player["lvl"] += 1
            player["xp"] = xpx
            enemy["Заражённая мышь"]["xp"] = 10
            break

def cherv():
    xpx = player["xp"]
    print(f'статистика червя переростка {enemy["Червь переросток"]}') 
    print("Хоршо давайте начнём")
    print(f'Ваше хп - {player["xp"]}')
    print(f'Ваша защита - {player["def"]}')
    print(f'Ваша атака- {player["atk"]}')
    print()
    while True:
        round = randint(1,2)
        if round == 1:
            player["xp"] -= enemy["Червь переросток"]["atk"]
        elif round == 2:
            enemy["Червь переросток"]["xp"] -= player["atk"]
        sleep(1)
        print("Произошёл удар! ")
        print(f'Хп противника - {enemy["Червь переросток"]["xp"]}')
        print(f'Ваше хп - {player["xp"]}')
        if player["xp"] <= 0:
            print("Вы проиграли")
            player["xp"] = xpx
            enemy["Червь переросток"]["xp"] = 110
            break
        elif enemy["Червь переросток"]["xp"] <= 0:
            spark = randint(1,10)
            print(f"Вы выйграли! Вы получили - {spark} спарков")
            player["sparki"] += spark
            if player["lvl"] == 2:
                player["lvl"] += 1
            player["xp"] = xpx
            enemy["Червь переросток"]["xp"] = 110
            break



def zarachen():
    xpx = player["xp"] 
    print(f'статистика заражённого {enemy["Заражённый"]}')
    print("Хоршо давайте начнём")
    print(f'Ваше хп - {player["xp"]}')
    print(f'Ваша защита - {player["def"]}')
    print(f'Ваша атака- {player["atk"]}')
    print()
    while True:
        round = randint(1,2)
        if round == 1:
            player["xp"] -= enemy["Заражённый"]["atk"]
        elif round == 2:
            enemy["Заражённый"]["xp"] -= player["atk"]
        sleep(1)
        print("Произошёл удар! ")
        print(f'Хп противника - {enemy["Заражённый"]["xp"]}')
        print(f'Ваше хп - {player["xp"]}')
        if player["xp"] <= 0:
            print("Вы проиграли")
            player["xp"] = xpx
            enemy["Заражённый"]["xp"] = 250
            break
        elif enemy["Заражённый"]["xp"] <= 0:
            spark = randint(1,10)
            print(f"Вы выйграли! Вы получили - {spark} спарков")
            player["sparki"] += spark
            if player["lvl"] == 2:
                player["lvl"] += 1
            player["xp"] = xpx
            enemy["Заражённый"]["xp"] = 250
            break


def dragon():
    xpx = player["xp"] 
    print(f'статистика заражённого дракона {enemy["Заражённый дракон"]}')
    print("Хоршо давайте начнём")
    print(f'Ваше хп - {player["xp"]}')
    print(f'Ваша защита - {player["def"]}')
    print(f'Ваша атака- {player["atk"]}')
    print()
    while True:
        round = randint(1,2)
        if round == 1:
            player["xp"] -= enemy["Заражённый дракон"]["atk"]
        elif round == 2:
            enemy["Заражённый дракон"]["xp"] -= player["atk"]
        sleep(1)
        print("Произошёл удар! ")
        print(f'Хп противника - {enemy["Заражённый дракон"]["xp"]}')
        print(f'Ваше хп - {player["xp"]}')
        if player["xp"] <= 0:
            print("Вы проиграли")
            player["xp"] = xpx
            enemy["Заражённый дракон"]["xp"] = 700
            break
        elif enemy["Заражённый дракон"]["xp"] <= 0:
            spark = randint(1,10)
            print(f"Вы выйграли! Вы получили - {spark} спарков")
            player["sparki"] += spark
            if player["lvl"] == 3:
                player["lvl"] += 1
            player["xp"] = xpx
            enemy["Заражённый дракон"]["xp"] = 700
            break


def mark():
            xpx = player["xp"]
            if player["time"] == 1:
                print(f'Статистика Шандр’гралла’дтрин: {enemy["Шандр’гралла’дтрин"]}')
                sleep(2)
                print("Хоршо давайте начнём")
                print(f'Ваше хп - {player["xp"]}')
                print(f'Ваша защита - {player["def"]}')
                print(f'Ваша атака- {player["atk"]}')
                print()
                while True:
                        round = randint(1,2)
                        if round == 1:
                            player["xp"] -= enemy["Шандр’гралла’дтрин"]["atk"]
                        elif round == 2:
                            enemy["Шандр’гралла’дтрин"]["xp"] -= player["atk"]
                        sleep(1)
                        print("Произошёл удар! ")
                        sleep(1)
                        print(f'Хп противника - {enemy["Шандр’гралла’дтрин"]["xp"]}')
                        print(f'Ваше хп - {player["xp"]}')
                        if player["xp"] <= 0:
                            print("Вы проиграли")
                            player["xp"] = xpx
                            enemy["Шандр’гралла’дтрин"]["xp"] = 1000
                            break
                        elif enemy["Шандр’гралла’дтрин"]["xp"] <= 0:
                            spark = randint(178,500)
                            print(f"Вы выйграли! Вы получили - {spark} спарков")
                            player["sparki"] += spark
                            player["xp"] = xpx
                            if player["lvl"] == 4:
                                 player["lvl"] += 1
                            enemy["Шандр’гралла’дтрин"]["xp"] = 1000
                            player["spa"] += 1
                            break
            elif player["lmt"] == 0:
                print(f'Статистика Шандр’гралла’дтрин: {enemy["Шандр’гралла’дтрин"]}')
                sleep(2)
                print("Хоршо давайте начнём")
                print(f'Ваше хп - {player["xp"]}')
                print(f'Ваша защита - {player["def"]}')
                print(f'Ваша атака- {player["atk"]}')
                print()
                while True:
                        round = randint(1,2)
                        if round == 1:
                            player["xp"] -= enemy["Шандр’гралла’дтрин"]["atk"]
                        elif round == 2:
                            enemy["Шандр’гралла’дтрин"]["xp"] -= player["atk"]
                        sleep(1)
                        print("Произошёл удар! ")
                        sleep(1)
                        print(f'Хп противника - {enemy["Шандр’гралла’дтрин"]["xp"]}')
                        print(f'Ваше хп - {player["xp"]}')
                        if player["xp"] <= 0:
                            print("Вы проиграли")
                            player["xp"] = xpx
                            enemy["Шандр’гралла’дтрин"]["xp"] = 1000
                            break
                        elif enemy["Шандр’гралла’дтрин"]["xp"] <= 0:
                            spark = randint(178,500)
                            print(f"Вы выйграли! Вы получили - {spark} спарков")
                            player["sparki"] += spark
                            player["xp"] = xpx
                            if player["lvl"] == 4:
                                 player["lvl"] += 1
                            enemy["Шандр’гралла’дтрин"]["xp"] = 1000
                            player["spa"] += 1
                            break
            elif player["lmt"] == 1:
                 print("К сожалению вы уже убили босса, если вы хотите убить его ещё раз то купите перемотку времени!")




def lukiu():
            xpx = player["xp"]
            if player["time"] == 1:
                print(f'Статистика Лукия: {enemy["Лукий"]}')
                sleep(2)
                print("Хоршо давайте начнём")
                print(f'Ваше хп - {player["xp"]}')
                print(f'Ваша защита - {player["def"]}')
                print(f'Ваша атака- {player["atk"]}')
                print()
                while True:
                        round = randint(1,2)
                        if round == 1:
                            player["xp"] -= enemy["Лукий"]["atk"]
                        elif round == 2:
                            enemy["Лукий"]["xp"] -= player["atk"]
                        sleep(1)
                        print("Произошёл удар! ")
                        sleep(1)
                        print(f'Хп противника - {enemy["Лукий"]["xp"]}')
                        print(f'Ваше хп - {player["xp"]}')
                        if player["xp"] <= 0:
                            print("Вы проиграли")
                            player["xp"] = xpx
                            enemy["Лукий"]["xp"] = 10000
                            break
                        elif enemy["Лукий"]["xp"] <= 0:
                            spark = randint(478,900)
                            print(f"Вы выйграли! Вы получили - {spark} спарков")
                            player["sparki"] += spark
                            if player["lvl"] == 5:
                                player["lvl"] += 1
                            player["xp"] = xpx
                            enemy["Лукий"]["xp"] = 10000
                            break
            elif player["lmt+"] == 0:
                print(f'Статистика Лукия: {enemy["Лукий"]}')
                sleep(2)
                print("Хоршо давайте начнём")
                print(f'Ваше хп - {player["xp"]}')
                print(f'Ваша защита - {player["def"]}')
                print(f'Ваша атака- {player["atk"]}')
                print()
                while True:
                        round = randint(1,2)
                        if round == 1:
                            player["xp"] -= enemy["Лукий"]["atk"]
                        elif round == 2:
                            enemy["Лукий"]["xp"] -= player["atk"]
                        sleep(1)
                        print("Произошёл удар! ")
                        sleep(1)
                        print(f'Хп противника - {enemy["Лукий"]["xp"]}')
                        print(f'Ваше хп - {player["xp"]}')
                        if player["xp"] <= 0:
                            print("Вы проиграли")
                            player["xp"] = xpx
                            enemy["Лукий"]["xp"] = 10000
                            break
                        elif enemy["Лукий"]["xp"] <= 0:
                            spark = randint(478,900)
                            print(f"Вы выйграли! Вы получили - {spark} спарков")
                            player["sparki"] += spark
                            if player["lvl"] == 5:
                                player["lvl"] += 1
                            player["lmt+"] += 1
                            player["xp"] = xpx
                            enemy["Лукий"]["xp"] = 10000
                            break
            else:
                 print("К сожалению вы уже убили босса, если вы хотите убить его ещё раз то купите перемотку времени!")



def otes():
            xpx = player["xp"]
            if player["time"] == 1:
                print(f'Статистика Отца: {enemy["Отец"]}')
                sleep(2)
                print("Хоршо давайте начнём")
                print(f'Ваше хп - {player["xp"]}')
                print(f'Ваша защита - {player["def"]}')
                print(f'Ваша атака- {player["atk"]}')
                print()
                while True:
                        round = randint(1,2)
                        if round == 1:
                            player["xp"] -= enemy["Отец"]["atk"]
                        elif round == 2:
                            enemy["Отец"]["xp"] -= player["atk"]
                        sleep(1)
                        print("Произошёл удар! ")
                        sleep(1)
                        print(f'Хп противника - {enemy["Отец"]["xp"]}')
                        print(f'Ваше хп - {player["xp"]}')
                        if player["xp"] <= 0:
                            print("Вы проиграли")
                            player["xp"] = xpx
                            enemy["Отец"]["xp"] = 500000
                            break
                        elif enemy["Отец"]["xp"] <= 0:
                            spark = randint(1000,5000)
                            print(f"Вы выйграли! Вы получили - {spark} спарков")
                            player["sparki"] += spark
                            player["lmt++"] += 1
                            player["xp"] = xpx
                            enemy["Отец"]["xp"] = 500000
                            player["spa"] += 1
                            break 
            elif player["lmt++"] == 0:
                print(f'Статистика Отца: {enemy["Отец"]}')
                sleep(2)
                print("Хоршо давайте начнём")
                print(f'Ваше хп - {player["xp"]}')
                print(f'Ваша защита - {player["def"]}')
                print(f'Ваша атака- {player["atk"]}')
                print()
                while True:
                        round = randint(1,2)
                        if round == 1:
                            player["xp"] -= enemy["Отец"]["atk"]
                        elif round == 2:
                            enemy["Отец"]["xp"] -= player["atk"]
                        sleep(1)
                        print("Произошёл удар! ")
                        sleep(1)
                        print(f'Хп противника - {enemy["Отец"]["xp"]}')
                        print(f'Ваше хп - {player["xp"]}')
                        if player["xp"] <= 0:
                            print("Вы проиграли")
                            player["xp"] = xpx
                            enemy["Отец"]["xp"] = 500000
                            break
                        elif enemy["Отец"]["xp"] <= 0:
                            spark = randint(1000,5000)
                            print(f"Вы выйграли! Вы получили - {spark} спарков")
                            player["sparki"] += spark
                            player["lmt++"] += 1
                            player["xp"] = xpx
                            enemy["Отец"]["xp"] = 500000
                            player["spa"] += 1
                            break
            else:
                 print("К сожалению вы уже убили босса, если вы хотите убить его ещё раз то купите перемотку времени!")
























def fight():
    xpx = player["xp"] 
    if player["lvl"] == 1:
         print("Пока что тебе доступен только 1 монстр это заражённая мышь")
         print("Вы хотите сражаться с ней?")
         print("(да/нет)")
         vib = input()
         if vib == "да" or vib == "Да":
            mouse()
         else:
              print("Хорошо")
    elif player["lvl"] == 2:
         print("Вам доступно 2 противников это: 1 - заражённая мышь, 2 - червь переросток")
         print("С кем вы хотите сражаться?")
         vib = input()
         if vib == '1':
              mouse()
         elif vib == '2':
              cherv()
         else:
              print("Хорошо")
    elif player["lvl"] == 3:
         print("Вам доступно 3 противника это: 1 - заражённая мышь, 2 - червь переросток и 3 - заражённый")
         print("С кем вы хотите сражаться?")
         vib = input()
         if vib == '1':
              mouse()
         elif vib == '2':
              cherv()
         elif vib == '3':
              zarachen()
         else:
              print("Хорошо")
    elif player["lvl"] == 4:
         print("Вам доступно 4 противника это: 1 - заражённая мышь, 2 - червь переросток, 3 - заражённый, 4 - заражённый дракон")
         print("С кем вы хотите сражаться?")
         vib = input()
         if vib == '1':
              mouse()
         elif vib == '2':
              cherv()
         elif vib == '3':
              zarachen()
         elif vib == '4':
              dragon()
         else:
              print("Хорошо")
    elif player["lvl"] == 5:
         print("Вам доступно 4 противника и 1 босс это: 1 - заражённая мышь, 2 - червь переросток, 3 - заражённый, 4 - заражённый дракон, 5 - Шангрин")
         print("С кем вы хотите сражаться?")
         vib = input()
         if vib == '1':
              mouse()
         elif vib == '2':
              cherv()
         elif vib == '3':
              zarachen()
         elif vib == '4':
              dragon()
         elif vib == '5':
              mark()
         else:
              print("Хорошо")
    elif player["lvl"] == 6:
         print("Вам доступно 4 противника и 2 босса это: 1 - заражённая мышь, 2 - червь переросток, 3 - заражённый, 4 - заражённый дракон, 5 - Шангрин, 6 - Лукий")
         print("С кем вы хотите сражаться?")
         vib = input()
         if vib == '1':
              mouse()
         elif vib == '2':
              cherv()
         elif vib == '3':
              zarachen()
         elif vib == '4':
              dragon()
         elif vib == '5':
              mark()
         elif vib == '6':
              lukiu()
         else:
              print("Хорошо")
    elif player["lvl"] == 7:
         print("Вам доступно 4 противника и 3 босса это: 1 - заражённая мышь, 2 - червь переросток, 3 - заражённый, 4 - заражённый дракон, 5 - Шангрин, 6 - Лукий, 7 - Отец ")
         print("С кем вы хотите сражаться?")
         vib = input()
         if vib == '1':
              mouse()
         elif vib == '2':
              cherv()
         elif vib == '3':
              zarachen()
         elif vib == '4':
              dragon()
         elif vib == '5':
              mark()
         elif vib == '6':
              lukiu()
         elif vib == '7':
              otes()
         else:
              print("Хорошо")
        






def malus():
    print("Перемещение в карманное измерение")
    sleep(3)
    if player["izmer"] == 0:
        print('''Вот тебе инструкция по тому что тут делать:
            Здесь тут ты можешь добывать кристаллы скинта а из каждого можно добыть от 10 до 100000 спарков''')
        player["izmer"] += 1
    while True:
        print("Что ты хочешь сдесь делать:")
        print("1 - Добыча спарков")
        print("2 - выйти")
        spar = input()
        if spar == '1':
            cristal = randint(1,5)
            spakl = randint(10,10000)
            if cristal == 1:
                  print(f"Вы нашли 1 кристал скинта из него вы добыли {spakl} спарков")
                  player["sparki"] += spakl



            elif cristal == 2:
                 print(f'Вы нашли 2 кристала скинта в 1 вы нашли {spakl} спарков')
                 player["sparki"] += spakl
                 spakl = randint(10,100000)
                 print(f'Во 2 кристале вы нашли {spakl} спарков')
                 player["sparki"] += spakl




            elif cristal == 3:
                 print(f'Вы нашли 3 кристалла скинта в 1 вы нашли {spakl} спарков')
                 player["sparki"] += spakl
                 spakl = randint(10,100000)
                 print(f'Во 2 кристале вы нашли {spakl} спарков')
                 player["sparki"] += spakl
                 spakl = randint(10,100000)
                 print(f'В 3 кристале скинта вы нашли {spakl} спарков')
                 player["sparki"] += spakl




            elif cristal == 4:
                 print(f'Вы нашли 4 кристалла скинта в 1 вы нашли {spakl} спарков')
                 player["sparki"] += spakl
                 spakl = randint(10,100000)
                 print(f'Во 2 кристале вы нашли {spakl} спарков')
                 player["sparki"] += spakl
                 spakl = randint(10,100000)
                 print(f'В 3 кристале скинта вы нашли {spakl} спарков')
                 player["sparki"] += spakl
                 spakl = randint(10,100000)
                 print(f'В 4 кристале вы нашли {spakl} спарков')
                 player["sparki"] += spakl


            elif cristal == 5:
                 print(f'Вы нашли 5 кристаллов скинта в 1 вы нашли {spakl} спарков')
                 player["sparki"] += spakl
                 spakl = randint(10,100000)
                 print(f'Во 2 кристале вы нашли {spakl} спарков')
                 player["sparki"] += spakl
                 spakl = randint(10,100000)
                 print(f'В 3 кристале скинта вы нашли {spakl} спарков')
                 player["sparki"] += spakl
                 spakl = randint(10,100000)
                 print(f'В 4 кристале вы нашли {spakl} спарков')
                 player["sparki"] += spakl
                 spakl = randint(10,100000)
                 print(f'В 5 кристале скинта вы нашли {spakl} спарков')
                 player["sparki"] += spakl
        elif spar == "2":
             break
                
             
def pyt():
    print("Куда вы хотите телепортироваться?")
    if player["son"] <= 2:
        print("Пока что вы можете телепортироваться в 1 - разрушенный замок")
        print("Вы хотите переместиться в разрушенный (Да/нет)")
        vibor = input()
        if vibor == "Да" or vibor == "да":
             print("Перемещение в разрушенный замок")
             ych = randint(1,3)
             if ych == 1:
                print("Вы не смогли никого развоплотить")
             elif ych == 2 and limit["never"] == 0:
                  print("Вы встретили заражённую гигансткую ворону, вы смогли развоплотить его. Его зовут Невер. Невер из Мора")
                  player["son"] += 1
                  village.append("Невер") 
                  limit["never"] += 1
             elif ych == 3 and limit["mark"] == 0:
                  print("Здесь вы нашли маленкого багрянника. Его зовут Мркл'штлак'лар или же просто Марк")
                  player["son"] += 1
                  village.append("Марк")
                  limit["mark"] += 1
        else:
             print("Хорошо")
    elif player["son"] >= 3:
         print("Теперь вы можете терепортироваться в Эшхолд (не тот Эшхолд с толпами монстров)")
         print("Вы хотите переместиться? (да/нет)")
         vibor = input()
         if vibor == "Да" or vibor == "да":
            print("Перемещение в Эшхолд")
            sleep(2)
            esh = randint(1,4)
            if esh == 1 or esh == 2:
               print("Вы никого не нашли в Эшхолде кого могли бы забрать к себе")
            elif esh == 3 and limit["alfred"] == 0:
                 print("В Эшхолде вы смогли найти охотника под названием Альфред. Он хороший парень")
                 player["son"] += 1
                 village.append("Альфред")
                 limit["alfred"] += 1
            elif esh == 4:
                 print("На площади вы увидели как Кардинал хочет казнить старика. Вы смогли спасти его. Его завут Беренгарий. САМЫЙ ЛУЧШИЙ ДЕД:)")
                 player["son"] += 1
                 village.append("Беренгарий")
                 limit["berengarii"] += 1
         if vibor == "нет":
              print("Хорошо")
            





def son():
    print("Перемещение в сонное измерение")
    sleep(3)
    print("Что вы хотите сделать?")
    print("1 - путешествие")
    print("2 - посмотреть сколько жителей находится в сонном измерении")
    varib = input()
    if varib == "2":
          if player["son"] == 0:
               print("Здесь очень одиноко. Сходите в путешествие и найдите себе жителей")
          elif player["son"] == 1:
               print("Здесь уже есть один житель но кажется ему здесь скучно")
               print(village)
          elif player["son"] == 2:
               print("Здесь уже есть 2 жителя, поздравляю!")
               print(village)
          elif player["son"] == 3:
               print("в вашем сонном измерении 3 жителя им тут хорошо")
               print(village)
          elif player["son"] == 4:
               print("У вас теперь 4 жителя вы молодец!")
               print(village)
    elif varib == "1":
         pyt()
         




    
def end():
     print("ВНИМАНИЕ!!!!")
     print("Вы уверенны что хотите закончить игру выйдя на 1 из 3 концовок?")
     a = input()
     if a == "Нет" or a == "нет":
          print("Хорошо")
     elif a == "да":
          if player["son"] == 4:
               print("Вы вышли на хорошую концовку некоторые жители Архея живы и находятся в безопастности а вы же смогли победить отца и заражёние пало...")
          elif player["time"] == 1:
               print("Взгляд смотрящего выражает недовольство тем что вы играли со временем.. запомни НЕ ИГРАЙСЯ СО ВРЕМЕНЕМ... плохая концовка")
          else:
               print("Вы прошли на ... Стоп.. А что это за концовка?...")