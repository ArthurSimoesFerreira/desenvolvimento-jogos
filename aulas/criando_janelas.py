from PPlay.window import*
from PPlay.sprite import*

## 1.1 - Creating a Window using (X, Y) as dimensions, where X is the ##
## width and Y the height ##
## Construtor da classe Window
janela = Window(700, 700)
janela.set_background_color(RGB=[100,100,100])

bola = Sprite("bolinha.png", 1)
bola.x = 300
bola.y = 312
# Game Loop
while(True):
    janela.update()
    bola.draw()