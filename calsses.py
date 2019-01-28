

class ID():
    def __init__(self, update_ID, ID_of_last_read_updte):
        self.update_ID = update_ID
        self.ID_of_last_read_updte = ID_of_last_read_updte


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
