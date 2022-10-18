from random import randint
import random
import requests
import json


def disorderWord(word):
    listName = list(word)
    random.shuffle(listName)
    return ' '.join(listName)


def guessPokemon(name):
    listResult = []
    listName = name.split('-')
    if len(listName) == 1:
        return disorderWord(name)
    else:
        for x in listName:
            listResult.append(disorderWord(x))
        return ' - '.join(listResult)


while(True):
    ndex = randint(1, 898)
    url = "https://pokeapi.co/api/v2/pokemon/{0}".format(ndex)
    r = requests.get(url=url)
    jsonPoke = r.json()
    name = jsonPoke["name"]
    disorderName = guessPokemon(name)
    text = ''
    while(name != text):
        text = input('\nAdivina el pokemon: {0}\n'.format(disorderName))
        if text == 'giveup':
            print(name)
            break
    if name == text:
        print('El pokemon era {0}'.format(name))
