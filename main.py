import requests
import vk_api
import random
import threading
import os
import time
from settings import settings
from name import name
from data import data

#<meta data>
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
helped = """Каждый день присылаю информацию, а они и спасибо не говорят:(
ЭХХХ...
Вот твои команды:
!list - список всех олимпиад.
!today - олимпиады, которые проходят сегодня."""

help = """Вот твои команды:
!list - список всех олимпиад.
!today - олимпиады, которые проходят сегодня."""
#</meta data>

#<load settings>
settings = settings()
info = name()
inf = data()
fut_dat = inf.future()
data = inf.data()
users = ["177337106",settings.owner_id()]
"236705719"
#</load settings>

#<create session>
assert (settings.api().replace(" ","") != "")
assert (settings.mes_api().replace(" ","") != "")
vk = vk_api.VkApi(token=settings.api())
vk._auth_token()
vk_group = vk_api.VkApi(token=settings.mes_api())
vk_group._auth_token()
#</create session>

#<def>
def mes_send(id,text):
    vk_group.method("messages.send", {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647)})


def futy(text):
    list = ""
    for i in fut_dat.keys():
        list += "Название: {0}.\nДата: {1}.\nURl:{2}.\n\n".format(i.replace("_"," "),fut_dat[i]["Date"],fut_dat[i]["url"])
    return text + "-------------\nНЕОПРЕДЕЛЕННЫЙ СТАТУС:\n\n" + list

def time_today():
    s = time.localtime()
    m,d = s.tm_mon,s.tm_mday
    return m,d

def time_now():
    s = time.localtime()
    h,m = s.tm_hour,s.tm_min
    return h,m

def list_today():
    m,d = time_today()
    return_list = {}
    for i in data.keys():
        a = data[i]["Date"]
        a = a.split("-")
        b = []
        for j in range(len(a)):
            b += a[j].split(":")
        a = b
        if(a[1][0] == "0"): a[1] = "2"+a[1][1:]
        if(a[3][0] == "0"): a[3]= "2"+a[3][1:]
        if(m < 10): m += 20
        if(int(a[1]) < m < int(a[3])):
            return_list[i] = data[i]
            continue
        if(int(a[1]) == m != int(a[3]) and int(a[0]) <= d):
            return_list[i] = data[i]
        if(int(a[3]) == m != int(a[1]) and d <= int(a[2])):
            return_list[i] = data[i]
        if(int(a[3]) == m == int(a[1]) and int(a[0]) <= d <= int(a[2])):
            return_list[i] = data[i]

    return return_list

def gen_list(dic,a = True):
    list = ""
    for i in dic.keys():
        try:
            list += "Название: {0}.\nДата: {1}.\nURl:{2}.\nTime:{3}\n\n".format(i.replace("_"," "),data[i]["Date"],data[i]["url"],data[i]["time"])
        except:
            list += "Название: {0}.\nДата: {1}.\nURl:{2}.\n\n".format(i.replace("_"," "),data[i]["Date"],data[i]["url"])
    if a:
        return futy(list)
    else:
        return list

def list_now():
    d,m = time_today()
    return_list = {}
    for i in data.keys():
        a = data[i]["Date"]
        a = a.split("-")
        b = []
        for j in range(len(a)):
            b += a[j].split(":")
        a = b
        if(d == int(a[2]) and m == int(a[3])):
            return_list[i] = data[i]
    return return_list

def tha(id):
    vk_group.method("messages.send", {"peer_id": id, "message": "Позязя)", "attachment": "photo-188799304_457239019","random_id": random.randint(1, 2147483647)})

def main():
    while True:
        if time_now() == (7,30):
            for i in users:
                mes_send(i,gen_list(list_today(),False))
        l = list_now()
        if l:
            for i in users:
                x,y = time_now()
                if(y == 0):
                    mes_send(i,gen_list(l,False))
        time.sleep(35)

#</def>

#<code>
threading.Thread(target=main).start()
while True:
    try:
        messages = vk_group.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "!list":
                mes_send(id,gen_list(data))
            elif body.lower() == "!today":
                mes_send(id,gen_list(list_today(),False))
            elif "спасибо" in body.lower():
                tha(id)
            elif body.lower() == "!help":
                mes_send(id,help)
            else:
                mes_send(id,helped)

    except Exception as E:
        time.sleep(1)

#</code>
