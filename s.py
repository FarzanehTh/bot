import urllib.request
import json
import urllib.parse
import ser


# url = "https://en.wikipedia.org/wiki/Flower"
url1 = "https://api.telegram.org/bot664436075:AAHVj-PcUpu1nQb37fh-ii6fKYITr1v7EFI/METHOD_NAME"
tel_url = "https://api.telegram.org/bot664436075:AAHVj-PcUpu1nQb37fh-ii6fKYITr1v7EFI/getUpdates"
my_msg = "https://api.telegram.org/bot664436075:AAHVj-PcUpu1nQb37fh-ii6fKYITr1v7EFI/sendMessage"
#


class InlineKeyboardButton(ser.Serializable):

    def __init__(self, text, url, callback_data=None, switch_inline_query=None, switch_inline_query_current_chat=None,
                 callback_game=None, pay=None):

        self.text = text
        self.url = url
        self.callback_data = callback_data
        self.switch_inline_query = switch_inline_query
        self.switch_inline_query_current_chat = switch_inline_query_current_chat
        self.callback_game = callback_game
        self.pay = pay



class InlineKeyboardMarkup(ser.Serializable):

    def __init__(self, inline_keyboard):

        self.inline_keyboard = inline_keyboard




def send_msg(url):
    req_obj = urllib.request.Request(url)

    opened_url = urllib.request.urlopen(req_obj)
    text = opened_url.read()
    str_text = text.decode("utf-8")
    json_obj = json.loads(str_text)

    return json_obj




obj_json = send_msg(tel_url)


# web = "<b>bold</b>, <strong>bold</strong><i>italic</i>, <em>italic</em><a href={0} title={1} >inline URL</a><code>inline fixed-width code</code><pre>pre-formatted fixed-width code block</pre>".format("http://www.google.com", "see")
# w = 'https://www.google.com/html'

# some_web = "[some]({})".format(w)

# some_web = "<a href='https://www.google.com'> something to </a>"
some_web = "https://www.google.com"

# web = "<a href={0}>Visit our HTML Tutorial</a>".format("https://www.w3schools.com/html")



#"parse_mode": "HTML"

chat_id = obj_json["result"][1]["message"]["chat"]["id"]

key = InlineKeyboardButton(text="salam how are ?", url=some_web)

arr1 = []
arr1.append(key)
arr2 = []
arr2.append(arr1)
arr3 = InlineKeyboardMarkup(arr2)


ser = json.dumps(arr3)
print(ser)


# dic_data1 = {"chat_id": chat_id, "text": some_web, "disable_web_page_preview": True, "parse_mode": "HTML"}


dic_data1 = {"chat_id": chat_id, "text": "clik ...", "reply_markup": ser}


value_data = urllib.parse.urlencode(dic_data1)

full_url = my_msg + "?" + value_data

print(full_url)
print(send_msg(full_url))








# print(str_text)
print(chat_id)
