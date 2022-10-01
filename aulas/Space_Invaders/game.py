from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.mouse import*
from PPlay.keyboard import*

def game():

    window = Window(900,600)
    keyboard = window.get_keyboard()

    while(True):
        window.update()
        window.set_background_color([0,0,0])
        if keyboard.key_pressed("ESC"):
            break