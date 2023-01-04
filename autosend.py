import pywhatkit
import datetime
import json
from classes import Person

f = open('config.json')
data = json.load(f)

today = datetime.date.today()
this_year = today.year

raffaela = Person(datetime.date(this_year, 1, 31),data['raffaela_number'], 'Hey Raffaela! Alles Gute zum Geburtstag :D')
david_pie = Person(datetime.date(this_year, 8, 2), data['david_number'], 'Yo fuckface, happy birthday!')


people = []
people.append(raffaela)
people.append(david_pie)

for x in people:
    if today == x.birthday:
        pywhatkit.sendwhatmsg_instantly(x.number, x.message, 15, True)
