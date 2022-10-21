from this import d
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.mouse import*
from game import *

def menu(difficulty):
    
    window = Window(900,600)
    mouse = window.get_mouse()

    backgroundMenu = GameImage("Space_Invaders\\assets\\background_space_invaders.png")
    backgroundMenu.set_position(0, 0)

    buttonPlay = Sprite("Space_Invaders\\assets\\button_play.png",1)
    buttonPlay.x = window.width/5 - buttonPlay.width/2
    buttonPlay.y = 500 - buttonPlay.height

    buttonRanking = Sprite("Space_Invaders\\assets\\button_ranking.png",1) 
    buttonRanking.x = window.width*2/5 - buttonRanking.width/2
    buttonRanking.y = 500 - buttonRanking.height

    buttonDifficulty = Sprite("Space_Invaders\\assets\\button_difficulty.png",1) 
    buttonDifficulty.x = window.width*3/5 - buttonDifficulty.width/2
    buttonDifficulty.y = 500 - buttonDifficulty.height

    buttonExit = Sprite("Space_Invaders\\assets\\button_exit.png",1)
    buttonExit.x = window.width*4/5 - buttonExit.width/2
    buttonExit.y = 500 - buttonExit.height

    while(True):
        window.update()
        window.set_background_color([0,0,0])

        buttonPlay.draw()
        buttonRanking.draw()
        buttonDifficulty.draw()
        buttonExit.draw()
        backgroundMenu.draw()

        
        if mouse.is_button_pressed(1):
            if mouse.is_over_object(buttonPlay):
                game(difficulty)
            
            if mouse.is_over_object(buttonRanking):
                pass
            if mouse.is_over_object(buttonDifficulty):
                difficulty = menuDifficulty()
                
            if mouse.is_over_object(buttonExit):
                window.close()      


def menuDifficulty():
    window = Window(900,600)
    keyboard = window.get_keyboard()
    mouse = window.get_mouse()

    buttonEasy = Sprite("button_easy.png",1)
    buttonEasy.x = window.width/2 - buttonEasy.width/2
    buttonEasy.y = window.height/4 - buttonEasy.height/2

    buttonMedium = Sprite("button_medium.png",1)
    buttonMedium.x = window.width/2 - buttonMedium.width/2
    buttonMedium.y = window.height*2/4 - buttonMedium.height/2

    buttonHard = Sprite("button_hard.png",1)
    buttonHard.x = window.width/2 - buttonHard.width/2
    buttonHard.y = window.height*3/4 - buttonHard.height/2

    buttonBack = Sprite("button_back.png",1)
    buttonBack.x = 30
    buttonBack.y = 30

    while(True):
        window.update()
        window.set_background_color([0,0,0])

        buttonEasy.draw()
        buttonMedium.draw()
        buttonHard.draw()
        buttonBack.draw()
        
        if mouse.is_over_object(buttonEasy) and mouse.is_button_pressed(1):
            menu(0.2)
        if mouse.is_over_object(buttonMedium) and mouse.is_button_pressed(1):
            menu(0.5)
        if mouse.is_over_object(buttonHard) and mouse.is_button_pressed(1):
            menu(0.7)
        

        if keyboard.key_pressed("ESC") or (mouse.is_button_pressed(1) and mouse.is_over_object(buttonBack)):
            menu(0.5)
