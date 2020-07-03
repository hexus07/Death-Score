
########################
#Импорт
import sys

import telebot
import time
import requests
from telebot import types

import datetime
import random

import module1
import module2
import module3
########################
#Токен телеграма
tele_token="1275569143:AAFoBoHT6BMNp6iWn65T0aUGy4OgbJY4wbw"
start = 0
bot = telebot.TeleBot(tele_token)#TELEGRAM BOT TOKEN



########################
#Die reasons

die_reasons = ["Туберкулёза","Половой болезни (исключая ВИЧ)","ВИЧ/СПИД",
"От инфекционной или паразитной болезни","Кори","Бешенства"
,"Недоедания","Рака","Сахарного Диабета","Шизофрении (Беда с Башкой)"
,"Инсульта","Бронхиальной Астмы","Язвы Желудка","Утопления"
,"Нападения холодным оружием","ДТП","Падения с высоты","Самоубийства","Авио-катастрофы"
,"Самоповреждения","Несчастного случая","Пожара","Востанния машин против человечества","Удара Молнии"
]

#Команди


@bot.message_handler(commands=['start'])
def send_welcome(message): #Приветствие
    bot.send_message(message.chat.id,"111")
    time.sleep(2)
    bot.send_message(message.chat.id, "И кстати я знаю как тебя зовут"+"\n"+message.from_user.first_name+", не так ли?"+"\n"+"Впрочем кем бы ты не был, ты красавчик!🤗")




def users(): #Ифнормация о юзерах
    i=open("input.txt", "r")
    main=[]
    users_num=int(i.readline())
    for j in range(int(users_num)):
        main.append(i.readline().split())
    i.close()
    return main


def user_check(user_name): #Проверка пользователей

    user_id  = 0
    for check in users():
        if check[0] == user_name:
            return False, user_id
        user_id += 1
    return True, user_id


def user_inf_add(new_inf): # Добление информации
    outp=open("input.txt", "w")
    outp.write(str(len(new_inf))+"\n")
    for j in new_inf:
        for al in j:
            outp.write(al+" ")
        outp.write("\n")
    outp.close()
    return True



def inf_change (inf, name):
    id = user_check(name)[1]


    new_inf = [name,module1.time1(name,id)[0],module1.time1(name,id)[1]]

    inf.pop(id)
    inf.append(new_inf)

    if user_inf_add(inf) == True:
        pass

    return module1.time1(name,id)[2]


#(1 часть - скачка на машину)


@bot.message_handler(content_types=['photo'])
def photo(message):
    if user_check(message.from_user.first_name)[0] == False:
        #bot.send_message(message.chat.id, "Так я тебя знаю!")

        a = inf_change(users(),message.from_user.first_name)

        bot.send_message(message.chat.id,"Тебе осталось жить - "+ str(a[0])+" Years " + str(a[1])+" Months "+ str(a[2])+" Days " + str(a[3])+" Hours "+ str(a[4])+" Min")


    else:
        fileID = message.photo[-1].file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)

        with open("image.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)

        face = (module2.face_detection())

        #bot.send_message(message.chat.id,"Мы нашли "+ str(face) +" лицо")

        # Новый Пользователь
        #bot.send_message(message.chat.id, "Так ты у нас новый смешарик!")


        a = module3.new_user_score()
        bot.send_message(message.chat.id,"Тебе осталось жить - "+ str(a[0])+" Years " + str(a[1])+" Months "+ str(a[2])+" Days " + str(a[3])+" Hours "+ str(a[4])+" Min")


        b = random.randint(0,23)
        bot.send_message(message.chat.id,"Причина смерти: от "+ die_reasons[b])


        inf = users()
        new_inf = [message.from_user.first_name,module1.time_with_dots(time.localtime()),module1.time_with_dots(a)]
        inf.append(new_inf)

        if user_inf_add(inf) == True:
            pass



bot.polling()
