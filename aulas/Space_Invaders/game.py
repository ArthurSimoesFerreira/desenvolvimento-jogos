from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.mouse import*
from PPlay.keyboard import*

def game():

    window = Window(900,600)
    keyboard = window.get_keyboard()

    spaceShip = Sprite("spaceship.png",1)
    spaceShip.x = window.width/2 - spaceShip.width/2
    spaceShip.y = window.height - spaceShip.height
    velxSpaceShip = 0.2

    shot = Sprite("shot.png",1)
    velyShot = -0.3
    shotsFired = False

    while(True):
        window.update()
        window.set_background_color([0,0,0])
        spaceShip.draw()

        if keyboard.key_pressed("ESC"):
            break

        # SpaceShip
        spaceShip.move_x(velxSpaceShip)
        if (spaceShip.x + velxSpaceShip * window.delta_time()) <= 0:
            velxSpaceShip = -velxSpaceShip
        elif (spaceShip.x + spaceShip.width + velxSpaceShip * window.delta_time()) >= window.width:
            velxSpaceShip = -velxSpaceShip
        # Shot
        if not(shotsFired):
            if keyboard.key_pressed("SPACE"):
                shot.x = (spaceShip.x + velxSpaceShip * window.delta_time()) + shot.width
                shot.y = spaceShip.y
                shotsFired = True
        if shotsFired:
            shot.draw()
            shot.move_y(velyShot)
            if (shot.y + velyShot * window.delta_time()) < 0:
                shotsFired = False
                shot.y = spaceShip.y
            

