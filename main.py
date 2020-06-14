
########################
#Импорт
import sys
import cv2

import telebot
import time
import requests
from telebot import types

import datetime
import random


########################
#Токен телеграма
tele_token="1275569143:AAFoBoHT6BMNp6iWn65T0aUGy4OgbJY4wbw"
start = 0
bot = telebot.TeleBot(tele_token)#TELEGRAM BOT TOKEN


########################
#Команди
@bot.message_handler(commands=['start'])
def send_welcome(message): #Приветствие
    bot.send_message(message.chat.id,"111")
    time.sleep(2)
    bot.send_message(message.chat.id, "И кстати я знаю как тебя зовут"+"\n"+message.from_user.first_name+", не так ли?"+"\n"+"Впрочем кем бы ты не был, ты красавчик!🤗")

########################
#Фото!
def face_detection():   #Проверка на лица
    import cv2
    imagePath = "image.jpg"
    cascPath = "haarcascade_frontalface_default.xml"

    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)

    )
    return(len(faces))

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
            break
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

def time_wthout_dots(time): #Время без точек
    output = []
    n = ""
    for j in time:
        if j != ".": n+=j
        else : output.append(n); n=""
    output.append(n)
    return output

def time_with_dots(old_time): #Вермя с точками
    main = ''
    for j in range(0,5):
        main+=(str(old_time[j]))
        if j == 4: pass
        else: main+="."
    return main

def time1(name): #Всё, что связанно со временем - а это дохуя чего
    id = user_check(name)[1]
    now_time = time.localtime()
    past_time = time_wthout_dots(users()[id][1])
    left_time = time_wthout_dots(users()[id][2])
    main = []

    time_SI = [0,12,30,24,60]
    for j in range(0,5):
        a = int(left_time[j]) - (int(now_time[j]) - int(past_time[j]))
        if a < 0 :
            if main[j-1] != 0:
                alt= main[j-1] - 1
                main.pop(j-1)
                main.append(alt)


            elif main[j-1] == 0:
                if main[j-2] != 0:
                    alt= main[j-2] - 1
                    main.pop(j-2)
                    main.insert(j-2,alt)
                    alt= time_SI[j-1] - 1
                    main.pop(j-1)
                    main.append(alt)
                else:
                    alt= main[j-3] - 1
                    main.pop(j-3)
                    main.insert(j-3,alt)

                    alt= time_SI[j-2] - 1
                    main.pop(j-2)
                    main.insert(j-2,alt)

                    alt= time_SI[j-1] - 1
                    main.pop(j-1)
                    main.append(alt)
            b= time_SI[j] + a
        else:
            b = a

        main.append(b)


    main1 = time_with_dots(main)
    main2 = time_with_dots(now_time)
    return main2, main1

def inf_change (inf, name):
    id = user_check(name)[1]


    new_inf = [name,time1(name)[0],time1(name)[1]]

    inf.pop(id)
    inf.append(new_inf)

    if user_inf_add(inf) == True:
        pass

    return time1(name)[1]

#(1 часть - скачка на машину)
def new_user_score(name):
    years = random.randrange(15,45); month = random.randrange(0,12); days = random.randrange(0,31); hours = random.randrange(0,24); mins = random.randrange(0,60);

    now_time = time.localtime()

    score = str(years) + "." + str(month) + "." + str(days) + "." + str(hours) + "." + str(mins)

    new_inf = [name,time_with_dots(now_time),score]
    return new_inf

@bot.message_handler(content_types=['photo'])
def photo(message):
    if user_check(message.from_user.first_name)[0] == False:
        bot.send_message(message.chat.id, "Так я тебя знаю!")


        bot.send_message(message.chat.id, inf_change(users(),message.from_user.first_name))


    else:
        fileID = message.photo[-1].file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)

        with open("image.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)

        ########################
        #   Фото! (2 часть - проверка на лицо)
        face = (face_detection())
        if int(face) == 1:
            bot.send_message(message.chat.id,"Мы нашли "+ str(face) +" лицо")

        # Новый Пользователь
        bot.send_message(message.chat.id, "Так ты у нас новый смешарик!")

        inf = users()
        inf.append(new_user_score(message.from_user.first_name))

        if user_inf_add(inf) == True:
            pass



bot.polling()
