#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     time management
#
# Author:      Даниил Чугай
#
# Created:     20.06.2020
# Copyright:   (c) Даниил Чугай 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import time
def users(): #Ифнормация о юзерах
    i=open("input.txt", "r")
    main=[]
    users_num=int(i.readline())
    for j in range(int(users_num)):
        main.append(i.readline().split())
    i.close()
    return main


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

def time1(name,id): #Всё, что связанно со временем - а это дохуя чего
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
    return main2, main1, main