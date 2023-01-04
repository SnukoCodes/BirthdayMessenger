import pywhatkit
import datetime
import json
import pytest
from classes import person

f = open('config.json')
data = json.load(f)

today = datetime.date.today()
thisyear = today.year

raffaela = person(datetime.date(thisyear, 1, 31),data['raffaelanumber'], 'Hey Raffaela! Alles Gute zum Geburtstag :D')
davidP = person(datetime.date(thisyear, 8, 2), data['davidnumber'], 'Yo fuckface, happy birthday!')


people = []
people.append(raffaela)
people.append(davidP)

for x in people:
    if today == x.birthday:
        pywhatkit.sendwhatmsg_instantly(x.number, x.message, 15, True)
