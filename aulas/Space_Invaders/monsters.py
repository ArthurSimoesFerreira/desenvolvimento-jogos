from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import*
from PPlay.keyboard import*

def showMonsters(window, monsterList):
    
    monster = Sprite("monster.png")
    monsterSubList = []
    x = window.width/2 - 2 * monster.width
    y = 0 

    for i in range(4):
        for j in range(4):
            monster = Sprite("monster.png")
            monsterSubList.append(monster)
            monsterSubList[j].x = x
            monsterSubList[j].y = y
            x = x + monster.width
        monsterList.append(monsterSubList)
        monsterSubList = []
        x = window.width/2 - 2 * monster.width
        y = y + monster.width/2

    return monsterList
    
    
    
