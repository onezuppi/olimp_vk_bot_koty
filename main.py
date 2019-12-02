import requests
import vk_api
import random
import threading
import os
import time
import words
import gamed
from settings import settings
from imagesoup import ImageSoup
from headers import get_headers
from PIL import Image,ImageDraw
from name import name
from data import data


#<meta data>
alp = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
helped = """Каждый день присылаю информацию, а они и спасибо не говорят:(
ЭХХХ...
Вот твои команды:
list(лист) - список всех олимпиад.
today(сегодня) - олимпиады, которые проходят сегодня.
help(помощь) - список всех команд.
splan(расписание) - расписание на неделю.
tom(завтра) - расписание на завтра.
coin(монетка) - подбросить монетку.
game(игра) - начать философскую игру.
end(конец) - выйти из игры.
leaders (лидеры) - таблица лидеров.
joke (шутка) - рандомная тупая шутка."""

help = """Вот твои команды:
list(лист) - список всех олимпиад.
today(сегодня) - олимпиады, которые проходят сегодня.
help(помощь) - список всех команд.
splan(расписание) - расписание на неделю.
tom(завтра) - расписание на завтра.
coin(монетка) - подбросить монетку.
game(игра) - начать философскую игру.
end(конец) - выйти из игры.
leaders (лидеры) - таблица лидеров.
joke (шутка) - рандомная тупая шутка."""

otter = {"Sun":"""Отдых,чилл,Бояра снова кродеться(""",
"Sat":"""-Литература;
-Литература;
-Экономика;
-Экономика;
-Английский язык;
-Астрономия.""",
"Fri": """-Алгебра;
-Алгебра;
-Физ-ра;
-Физ-ра;
-Физика;
-ОБЖ(География).""",
"Thu": """-Биология;
-Информатика;
-Физ-ра;
-История;
-Обществознание;
-Обществознание.""",
"Wed" : """-Алгебра;
-Алгебра;
-Английский язык;
-Английский язык;
-Физика;
-Физика.""",
"Tue" : """-Геометрия;
-Геометрия;
-Русский язык;
-Литература;
-География;
-Химия.""",
"Mon": """-Физика;
-Физика;
-История;
-История;
-Право;
-Право;
-Обществознание."""}
user_data = {}
user_data_image = {}
user_score = {}
#</meta data>

#<load settings>
settings = settings()
info = name()
inf = data()
fut_dat = inf.future()
data = inf.data()
users = ["177337106",settings.owner_id(),"236705719"]
# users = [settings.owner_id()]
#</load settings>

#<create session>
# assert (settings.api().replace(" ","") != "")
assert (settings.mes_api().replace(" ","") != "")
# vk = vk_api.VkApi(token=settings.api())
# vk._auth_token()
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
    m,d = time_today()
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
            day = time.ctime().split()[0]
            for i in users:
                mes_send(i,gen_list(list_today(),False))
                vk_group.method("messages.send", {"peer_id": i, "attachment": "video-188799304_456239017" ,"random_id": random.randint(1, 2147483647)})
                mes_send(i,"\nУ тебя сегодня:" + worked(day))
                os.system("rm img/*")
        l = list_now()
        if l:
            for i in users:
                x,y = time_now()
                if(y == 0):
                    mes_send(i,gen_list(l,False))
        time.sleep(45)

def worked(day = False):
    if day:
        return "\nРасписание:\n\n" + otter[day] + "\n"
    else:
        mes = "Расписание:\n\n"
        for i in list(otter.keys())[::-1]:
            mes += i + ":\n" + otter[i] + "\n\n"
        return mes

def tomorow():
    day = time.ctime().split()[0]
    key = list(otter.keys())
    for i in range(len(key)):
        if day == key[i]:
            return "Завтра у тебя:\n" + otter[key[i-1]]

def spam(id,text):
    for i in users:
        if str(i) == str(id):
            continue
        mes_send(i,text)

def message_send_file(id:int, text:str, local_url:str, type:str, title:str = "undefined"):
    """Sends a text message to the user with the specified id and the local file in the attachment."""

    local_file = open(local_url, 'rb')
    if type == "photo":
        url = vk_group.method("photos.getMessagesUploadServer")['upload_url']
        files = requests.post(url, files={"file": local_file}, headers = get_headers()).json()
        files = vk_group.method('photos.saveMessagesPhoto', {'photo': files['photo'], 'server': files['server'], 'hash': files['hash']})[0]
    else:
        url = vk_group.method("docs.getMessagesUploadServer",{"type": type, "peer_id": id })["upload_url"]
        files = requests.post(url,files={"file": local_file}, headers = get_headers()).json()["file"]
        files = vk_group.method("docs.save",{"file":file, "title": title })["doc"]
    local_file.close()
    message_send(id,text,"{0}{1}_{2}".format(type,files["owner_id"],files["id"]))

def message_send(id:int, text:str, attachment:str = False):
    """Sends a text message to the user with the specified id..You can send text with an attachment of the form: <type><owner_id>_<media_id>,<type><owner_id>_<media_id>"""

    if attachment:
        vk_group.method("messages.send", {"peer_id": id, "message": text, "attachment": attachment, "random_id": random.randint(1, 2147483647)})
    else:
        vk_group.method("messages.send", {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647)})

def get_and_send_img(title,id):
    def get_and_send_img_2(title,id):
        soup = ImageSoup()
        images = soup.search('{0}'.format(title), n_images=random.randint(10,50))
        img = random.choice(images)
        name = "".join(random.choices(alp,k=12)) + ".jpg"
        img.to_file('img/{0}'.format(name))
        message_send_file(id,"Ваш запрос:","img/{0}".format(name),"photo")
    try:
        threading.Thread(target=get_and_send_img_2,args=[title,id]).start()
    except:
        mes_send(id,"ERROR")


def resize_image(input,output):
    image = Image.open(input)
    width, height = image.size
    draw = ImageDraw.Draw(image)
    pix = image.load()
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = (a + b + c) // 3
            draw.point((i, j), (S, S, S))
    resize = image.resize((int(width*0.05),int(height*0.05)))
    resize = resize.resize((int(width),int(height)))
    resize.save(output)

def game(id,body):
    if(user_data[id] != True):
        if(body == user_data[id].lower()):
            message_send_file(id,"Пральна",user_data_image[id],"photo")
            gamed.score_pLus(id)
            mes_send(id,"Ваш счет: {0}.".format(gamed.get(id)))
        else:
            message_send_file(id,"Мимо! Это " + user_data[id],user_data_image[id],"photo")
        user_data[id] = True
    word = words.get_word()
    soup = ImageSoup()
    try:
        images = soup.search('{0}'.format(word), n_images=random.randint(10,50))
        img = random.choice(images)
        name = "".join(random.choices(alp,k=12)) + ".png"
        img.to_file('img/{0}'.format(name))
        new_name = "img/new_" + name
        resize_image('img/{0}'.format(name),new_name)
        message_send_file(id,"",new_name,"photo")
        user_data[id] = word
        user_data_image[id] = f"img/{name}"
    except:
        game(id,body)

def joke(id):
    st = "Шутка:\n"
    f = requests.post("http://freegenerator.ru/shutok",data={"type":"shutok"}).json()["text"]
    mes_send(id,st + f)


#</def>

#<code>
threading.Thread(target=main).start()
while True:
    try:
        messages = vk_group.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "end" or body.lower() == "конец":
                user_data[id] = False
                mes_send(id,"Игра завершена.")
            elif body.lower() == "leaders" or body.lower() == "лидеры":
                mes_send(id,gamed.get_leaderboard())
            elif user_data.get(id):
                game(id,body.lower())
            elif body.lower() == "list" or body.lower() == "лист":
                mes_send(id,gen_list(data))
            elif body.lower() == "today" or body.lower() == "сегодня":
                mes_send(id,gen_list(list_today(),False))
            elif "спасибо" in body.lower() or "cgfcb,j" in body.lower():
                tha(id)
            elif body.lower() == "help" or body.lower() == "помощь":
                mes_send(id,help)
            elif body.lower() == "splan" or body.lower() == "расписание":
                mes_send(id,worked())
            elif body.lower() == "tom" or body.lower() == "завтра":
                mes_send(id,tomorow())
            elif body.lower() == "coin" or body.lower() == "монетка":
                mes_send(id,"Орел" if random.randint(0,1) == 0 else "Решка")
            elif body.lower()[0] == "!" and (str(id) == str(settings.owner_id()) or str(id) == "177337106"):
                mes_send(id,"Completed!")
                spam(id,body[1:])
            elif body.lower()[0] == "?":
                get_and_send_img(body.lower()[1:],id)
                mes_send(id,"Поиск...")
            elif body.lower() == "game" or body.lower() == "игра":
                if gamed.get(id) == None:
                    gamed.new_player(id)
                user_data[id] = True
                mes_send(id,"Введите 'end', для выхода из игры.\nВаши очки: {0}.\nНачинаем!".format(gamed.get(id)))
                game(id,body.lower())
            elif body.lower() == "joke" or body.lower() == "шутка":
                joke(id)
            else:
                mes_send(id,helped)
    except:
        pass
#</code>
# update
