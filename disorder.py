import random


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


name = 'rojo-alpino-decreciente-luna-menguante'
print(guessPokemon(name))
