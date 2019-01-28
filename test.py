import urllib.request
import json
import urllib.parse
# import emoji
import calsses
import cgi
from django.urls import path
# import web
from django.http import HttpResponse
# urls = ('/.*', 'hooks')
#
# app = web.application(urls, globals())
# #
# class hooks:
#     def POST(self):
#         data = web.data()
#         # print
#         # print 'DATA RECEIVED:'
#         # print data
#         # print
#         return 'OK'
# def webhook(req):
#     return req
#     # return HttpResponse('pong')
#
#
# # from flask import
#
# urlpatterns = [
#
#     path("/", webhook, name='hello'),
# ]

# from flask import Flask,request
# from flask.ext.webhook import WebHook
#
# app = Flask(__name__)
#
# #create webhook object (name and app are optional)
# #if app is not passed in in the constructor, my_webhook.init_app(app) is needed.
# my_webhook = WebHook(name='optional_webhook_name', url_prefix='/webhooks' app=app)
# my_webhook.add_route('/something', methods=['GET', 'POST'])
#
# #define a function handler to be called by the webhook
# def some_function(hookrequest):
#
# #attach your function handler to the webhook.
# #you can attach as many as you want and they all are going to be called
# # () should not be included
# my_webhook.handlers['some_name_for_your_handler'] = some_function
#

## Factory Example
#
# # a
# web_num = "https://thisbot.herokuapp.com"
# #"thisbot.herokuapp.com"
#
from flask import Flask, request, abort,jsonify

app = Flask(__name__)
application = app

@app.route('/' , methods=['GET', 'POST'])

def webhook():
    # print(request.method)
    if request.method == 'POST':
        # data = request.json
        # print(data.get("result"))
        json_data = request.get_json()
        # print(json.loads(req))
        # return '', 200
        # data = json.loads(request.args)
        data = request.get_json(force=True)
        return jsonify(data)
        # return "ssss"

    else:
        print("no;;;;")
        abort(400)
        return "sala"
    # return jsonify(request.json)

    # return "salam"

# from flask import Flask, request
# import json
#
# app = Flask(__name__)
#
# @app.route('/',methods=['POST'])
# def foo():
#    data = json.loads(request.data)
#    # print ("New commit by: {}".format(data['result']))
#    return data
#
# # we need to save these in a file for every run to use lst_of_people = ["Farzaneh"], lst_of_registered_users = []
# # and update file
#
web_num = "https://thisbot.herokuapp.com"
# bank_info = "<b>Sman Bank</b> {}: <i> \n Bank account Number : </i> \n" \
#             "<i> Card Number: </i>".format(emoji.emojize(":dolphin:"))
# # bank_info = "bank"

    # w = 'https://www.google.com/html'


def set_last_id():
    try:
        open_file = open(file_address)
        read = open_file.read()
        last = calsses.ID(0, int(read))
    except:
        last = calsses.ID(0, 0)
    return last


file_address = "/Users/amir/Desktop/Tel.txt"

valid_commands = ["/link", "/registration", "/status", "/name", "/start"]
last_ID = set_last_id()

lst_of_people = ["Farzaneh"]
# dict of user_id : name
lst_of_registered_users = []
url1 = "https://api.telegram.org/bot664436075:AAHVj-PcUpu1nQb37fh-ii6fKYITr1v7EFI/METHOD_NAME"
tel_url = "https://api.telegram.org/bot664436075:AAHVj-PcUpu1nQb37fh-ii6fKYITr1v7EFI/setWebhook?url={}".format(
    web_num)

# my_msg = "https://api.telegram.org/bot664436075:AAHVj-PcUpu1nQb37fh-ii6fKYITr1v7EFI/sendMessage"







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



def get_update(url):
    req_obj = urllib.request.Request(url)
    opened_url = urllib.request.urlopen(req_obj)
    text = opened_url.read()
    str_text = text.decode("utf-8")
    json_obj = json.loads(str_text)
    print(json_obj)
    # obj = cgi.FieldStorage()

    # app = Flask(__name__)
    #
    # @app.route('/', methods=['POST'])
    # def foo():
    #     data = json.loads(request.data)
    #     # print("New commit by: {}".format(data['result']))
    #     return data
    #
    # return data


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
                     "disable_web_page_preview": True, "parse_mode": parse}

    else:

        dic_data1 = {"chat_id": id_of_chat, "text": text, "disable_web_page_preview": True}

    value_data = urllib.parse.urlencode(dic_data1)

    full_url = my_msg + "?" + value_data
    return full_url

#
# def send_link(id_of_chat):
#     some_web = "https://t.me/joinchat/AAAAAEsJPhgcKL-14m2Q9Q"
#
#     key = calsses.InlineKeyboardButton("Please join our channel !{}".format(emoji.emojize(":tulip:")), some_web)
#
#     arr1 = []
#     arr1.append(key)
#     arr2 = []
#     arr2.append(arr1)
#     arr3 = calsses.InlineKeyboardMarkup(arr2)
#     # print(arr2)
#
#     seri = json.dumps(arr3, default=serialize)
#
#     print(seri)
#     full_url = make_url(id_of_chat=id_of_chat, text="Hi There, Please click on the Link Below To Join !!",
#                         mark_up=seri)
#     send_msg(full_url)


# def send_info(id_of_chat):
#     # web = "<a href={0}>bank </a>".format("https://www.w3schools.com/html")
#     full_url = make_url(id_of_chat, bank_info, parse="HTML")
#     send_msg(full_url)


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


def check_name(msg, id_of_c, id_of_u):
    # name = update_msg["text"]
    name = msg[6:]
    if lst_of_registered_users.__contains__(id_of_u) is False:

        if name in lst_of_people:
                # send_link(id_of_c)
                lst_of_registered_users.append(id_of_u)

        else:
            send_msg(make_url(id_of_c, "you have to pay"))
    else:
        send_msg(make_url(id_of_c, "You are already in"))


# if __name__ == "__main__":

    # get the updates
    # last_ID = set_last_id()
    # get_update("")
    app.debug = True
    app.run()


