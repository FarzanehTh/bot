import urllib.request
import json
import urllib.parse







def send_msg(url):
    req_obj = urllib.request.Request(url)

    opened_url = urllib.request.urlopen(req_obj)
    text = opened_url.read()
    str_text = text.decode("utf-8")
    json_obj = json.loads(str_text)

    return json_obj


# url = "https://en.wikipedia.org/wiki/Flower"
url1 = "https://api.telegram.org/bot664436075:AAHVj-PcUpu1nQb37fh-ii6fKYITr1v7EFI/METHOD_NAME"
tel_url = "https://api.telegram.org/bot664436075:AAHVj-PcUpu1nQb37fh-ii6fKYITr1v7EFI/getUpdates"
my_msg = "https://api.telegram.org/bot664436075:AAHVj-PcUpu1nQb37fh-ii6fKYITr1v7EFI/sendMessage"

obj_json = send_msg(tel_url)


# web = "<b>bold</b>, <strong>bold</strong><i>italic</i>, <em>italic</em><a href={0} title={1} >inline URL</a><code>inline fixed-width code</code><pre>pre-formatted fixed-width code block</pre>".format("http://www.google.com", "see")
# w = 'https://www.google.com/html'

# some_web = "[some]({})".format(w)

some_web = 'https://www.google.com'

# web = "<a href={0}>Visit our HTML Tutorial</a>".format("https://www.w3schools.com/html")

key = {}
key["text"] = "hi hi"
key["url"] = some_web

s_msg = json.dumps(key)

arr = []
arr.append([key])
arr2 = json.dumps(arr)

#"parse_mode": "HTML"

chat_id = obj_json["result"][0]["message"]["chat"]["id"]

dic_data = {"chat_id": chat_id, "text": some_web, "reply_markup": s_msg}


value_data = urllib.parse.urlencode(dic_data)

full_url = my_msg + "?" + value_data

print(full_url)


print(send_msg(full_url))





# print(str_text)
print(chat_id)
