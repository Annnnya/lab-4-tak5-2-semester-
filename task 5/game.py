from numpy import character

class Room:
    def __init__(self, name) -> None:
        self.name = name
        self.linked_room = {}
        self.character = None
        self.item = None
    def set_description(self, text:str):
        self.text = text
    def link_room(self, room, direction):
        self.linked_room[direction]=room
    def set_character(self, char):
        self.character = char
    def set_item(self, item):
        self.item = item
    def get_details(self):
        print(self.name)
        print('--------------------')
        print(self.text)
        for link in self.linked_room:
            print(f'{self.linked_room[link].name} is {link}')
    def get_character(self):
        return self.character
    def get_item(self):
        return self.item
    def move(self, where):
        if where in self.linked_room:
            return self.linked_room[where]
        else:
            return self

class Enemy:
    defeats=0
    def __init__(self, name, descr) -> None:
        self.name = name
        self.description = descr
    def set_conversation(self, text):
        self.text=text
    def talk(self):
        print(f'[{self.name} says]: ', self.text)
    def set_weakness(self, weakness):
        self.weakness = weakness
    def describe(self):
        print(f'{self.name} is here!')
        print(self.description)
    def fight(self, fight_wi):
        if self.weakness==fight_wi:
            Enemy.defeats+=1
            return True
        return False
    def get_defeated(self):
        return Enemy.defeats

class Item:
    def __init__(self, name) -> None:
        self.name = name
    def set_description(self, descr):
        self.description = descr
    def describe(self):
        print(f'The [{self.name}] is here - ', self.description)
    def get_name(self):
        return self.name
