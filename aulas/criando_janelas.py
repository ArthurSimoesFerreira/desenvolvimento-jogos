from PPlay.window import*

## 1.1 - Creating a Window using (X, Y) as dimensions, where X is the ##
## width and Y the height ##
## Construtor da classe Window
janela = Window(1000, 400)
janela.set_background_color(RGB=[0,128,0])
# Game Loop
while(True):
    janela.update()