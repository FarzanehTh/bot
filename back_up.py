import urllib.request
import json
import urllib.parse
import emoji
import calsses

file_address = "/Users/amir/Desktop/Tel.txt"

valid_commands = ["/link", "/registration", "/status", "/name"]

ID_of_last_read_updte = 0



#
#
# class ID():
#     def __init__(self, update_ID, ID_of_last_read_updte):
#         self.update_ID = update_ID
#         self.ID_of_last_read_updte = ID_of_last_read_updte
#

def set_last_id():
    try:
        open_file = open(file_address)
        read = open_file.read()
        last = calsses.ID(0, int(read))
    except:
        last = calsses.ID(0, 0)
    return last


last_ID = set_last_id()

lst_of_people = ["Farzaneh"]
# dict of user_id : name
lst_of_registered_users = {}
url1 = "https://api.telegram.org/bot664436075:AAHVj-PcUpu1nQb37fh-ii6fKYITr1v7EFI/METHOD_NAME"
tel_url = "https://api.telegram.org/bot664436075:AAHVj-PcUpu1nQb37fh-ii6fKYITr1v7EFI/getUpdates?offset={}".format(
    last_ID.ID_of_last_read_updte + 1)


# my_msg = "https://api.telegram.org/bot664436075:AAHVj-PcUpu1nQb37fh-ii6fKYITr1v7EFI/sendMessage"
#

#
# def set_all():
#
#     def set_last_id():
#         try:
#             open_file = open(file_address)
#             read = open_file.read()
#             last = ID(0, int(read))
#         except:
#             last = ID(0, 0)
#         return last
#





# classes........

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class InlineKeyboardButton():
    def __init__(self, txt, s_url, callback_data=None, switch_inline_query=None,
                 switch_inline_query_current_chat=None,
                 callback_game=None, pay=None):
        self.text = txt
        self.url = s_url
        self.callback_data = callback_data
        self.switch_inline_query = switch_inline_query
        self.switch_inline_query_current_chat = switch_inline_query_current_chat
        self.callback_game = callback_game
        self.pay = pay

    def to_json(self):
        return self.__dict__


class InlineKeyboardMarkup():
    def __init__(self, inline_keyboard):
        self.inline_keyboard = inline_keyboard

    def to_json(self):
        return self.__dict__


#
# class ID():
#     def __init__(self, update_ID):
#
#         self.update_ID = update_ID
#
# last_ID = ID(0)
################################


# helpers

def serialize(obj):
    """JSON serializer for objects not serializable by default json code"""

    # if isinstance(obj, date):
    #     serial = obj.isoformat()
    #     return serial
    #
    # if isinstance(obj, time):
    #     serial = obj.isoformat()
    #     return serial

    return obj.to_json()


def update_update(obj):

    last = obj["result"]
    for i in range(len(last)):
        id_of_update = last[i]["update_id"]
        if id_of_update > last_ID.update_ID:
            last_ID.update_ID = id_of_update



def get_update(url):

    req_obj = urllib.request.Request(url)
    opened_url = urllib.request.urlopen(req_obj)
    text = opened_url.read()
    str_text = text.decode("utf-8")
    json_obj = json.loads(str_text)
    update_update(json_obj)
    return json_obj


def send_msg(url):

    req_obj = urllib.request.Request(url)
    opened_url = urllib.request.urlopen(req_obj)
    text = opened_url.read()
    str_text = text.decode("utf-8")
    json_obj = json.loads(str_text)
    return json_obj


def make_url(id_of_chat, text, mark_up=None, parse=None):

    my_msg = "https://api.telegram.org/bot664436075:AAHVj-PcUpu1nQb37fh-ii6fKYITr1v7EFI/sendMessage"

    if mark_up is not None and parse is not None:
        dic_data1 = {"chat_id": id_of_chat, "text": text, "parse_mode": parse,
                     "disable_web_page_preview": True, "reply_markup": mark_up}
    elif mark_up is not None and parse is None:
        dic_data1 = {"chat_id": id_of_chat, "text": text,
                     "disable_web_page_preview": True, "reply_markup": mark_up}

    elif mark_up is None and parse is not None:
        dic_data1 = {"chat_id": id_of_chat, "text": text,
                     "disable_web_page_preview": True, "reply_markup": mark_up}

    else:

        dic_data1 = {"chat_id": id_of_chat, "text": text, "disable_web_page_preview": True}

    value_data = urllib.parse.urlencode(dic_data1)

    full_url = my_msg + "?" + value_data
    return full_url


def send_link(id_of_chat):
    some_web = "https://t.me/joinchat/AAAAAEsJPhgcKL-14m2Q9Q"

    key = InlineKeyboardButton("Please join our channel !{}".format(emoji.emojize(":tulip:")), some_web)

    arr1 = []
    arr1.append(key)
    arr2 = []
    arr2.append(arr1)
    arr3 = InlineKeyboardMarkup(arr2)
    # print(arr2)

    seri = json.dumps(arr3, default=serialize)

    print(seri)
    full_url = make_url(id_of_chat=id_of_chat, text="Hi There, Please click on the Link Below To Join !!",
                        mark_up=seri)
    send_msg(full_url)


def send_info(id_of_chat):
    web = "<a href={0}>bank </a>".format("https://www.w3schools.com/html")
    full_url = make_url(id_of_chat, "Hi There, Please click on the Link Below To Join {}!!".format(web), parse="HTML")
    send_msg(full_url)


def send_user_status(id_of_chat):
    pass


#
# def update_chat(id, msg):
#     # msg = get_update(tel_url)["result"]
#     for i in range(len(msg)):
#         this_msg = msg[i]["message"]
#         if this_msg["chat"]["id"] == id:
#             if this_msg["text"].startswith("/name"):
#                 return this_msg
#     else:
#         return None

def go_over():
    obj_json = get_update(tel_url)

    queue1 = Queue()

    # quque the users
    lst_counts = []
    chat_members = obj_json["result"]
    for i in range(len(chat_members)):
        this_date = obj_json["result"][i]["message"]["date"]
        chat_id = obj_json["result"][i]["message"]["chat"]["id"]
        msg = obj_json["result"][i]["message"]["text"]
        user_id = obj_json["result"][i]["message"]["from"]["id"]
        if msg in valid_commands or msg.startswith("/name"):
            queue1.enqueue({chat_id: [msg, user_id]})
            lst_counts.append(i)

    return queue1


#################
#
# def switch(arq):
#
#     switcher = {
#         "/link": case1,
#         "/registration info": case2,
#         "/check status": case3
#
#     }
#
#

########*****


def check_name(msg, id_of_c):
    # name = update_msg["text"]
    name = msg[6:]
    if name in lst_of_people:
        send_link(id_of_c)
        # if lst_of_registered_users.get(u_id) is None:
        #     send_link(user_to_serve)
    else:
        send_msg(make_url(id_of_c, "you have to pay"))


if __name__ == "__main__":

    # get the updates
    queue = go_over()
    while last_ID.ID_of_last_read_updte < last_ID.update_ID:
        print(last_ID.ID_of_last_read_updte)
        print(last_ID.update_ID)

        while queue.size() != 0:

            print(queue.size())

            user = queue.dequeue()
            user_to_serve = user.popitem()

            chat_i = user_to_serve[0]

            txt = user_to_serve[1][0]
            u_id = user_to_serve[1][1]

            if txt == "/link":
                # check if that person with user_id is already registred
                # 1. get thier name
                message = send_msg(make_url(id_of_chat=chat_i, text="what is your name ?"))

            if txt == "/registration":
                send_info(chat_i)
            elif txt == "/status":
                send_user_status(chat_i)
            elif txt.startswith("/name"):
                # update_msg = update_chat(chat_i, txt)
                check_name(txt, chat_i)
            else:
                pass

        last_ID.ID_of_last_read_updte = last_ID.update_ID

        queue = go_over()

    open_write = open(file_address, "w")
    open_write.write(str(last_ID.ID_of_last_read_updte))
    open_write.close()

    # web = "<b>bold</b>, <strong>bold</strong><i>italic</i>, <em>italic</em><a href={0} title={1} >inline URL</a><code>inline fixed-width code</code><pre>pre-formatted fixed-width code block</pre>".format("http://www.google.com", "see")
    # w = 'https://www.google.com/html'

    # some_web = "[some]({})".format(w)

    # some_web = "<a href='https://www.google.com'> something to </a>"
# some_web = "https://t.me/joinchat/AAAAAEsJPhgcKL-14m2Q9Q"
# web = "<a href={0}>Visit our HTML Tutorial</a>".format("https://www.w3schools.com/html")



# "parse_mode": "HTML"
