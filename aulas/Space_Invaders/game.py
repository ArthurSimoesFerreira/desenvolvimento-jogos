from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.mouse import*
from PPlay.keyboard import*
from monsters import *

def game(difficulty):

    window = Window(900,600)
    keyboard = window.get_keyboard()

    spaceShip = Sprite("spaceship.png",1)
    spaceShip.x = window.width/2 - spaceShip.width/2
    spaceShip.y = window.height - spaceShip.height
    velxSpaceShip = 200

    shotList = []
    velyShot = 300
    crono = difficulty

    monsterList = []

    cronoFPS = 0
    textFPS = ""

    while(True):
        window.update()
        window.set_background_color([0,0,0])

        if keyboard.key_pressed("ESC"):
            break

        # SpaceShip
        spaceShip.move_x(velxSpaceShip * window.delta_time())
        if (spaceShip.x + velxSpaceShip * window.delta_time()) <= 0:
            velxSpaceShip = -velxSpaceShip
        elif (spaceShip.x + spaceShip.width + velxSpaceShip * window.delta_time()) >= window.width:
            velxSpaceShip = -velxSpaceShip

        # Shot
        if keyboard.key_pressed("SPACE") and crono >= difficulty:
            shot = Sprite("shot.png")
            shot.x = spaceShip.x + 10
            shot.y = spaceShip.y 
            shotList.append(shot)
            crono = 0
        
        if shotList != [] and (shotList[0].y + shotList[0].height) <= 0:
            shotList.pop(0)

        for i in range(len(shotList)):
            shotList[i].move_y(-velyShot * window.delta_time())
            shotList[i].draw()
        
        crono += window.delta_time()
        spaceShip.draw()

        # Monster
        if monsterList == []:
            monsterList = showMonsters(window, monsterList)
        
        for monsterSubList in monsterList:
            for indMonster in monsterSubList:
                indMonster.draw()

        # FPS
        cronoFPS += window.delta_time()
        if cronoFPS > 1:
            textFPS = f"FPS: {1/cronoFPS}"
            cronoFPS = 0
        
        window.draw_text(textFPS, window.width - 60, 20, 12, (255,255,255))

        

