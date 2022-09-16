from PPlay.window import*
from PPlay.sprite import*

# Janela
janela = Window(700, 700)
janela.set_background_color(RGB=[0,0,0])

# Bolinha
bola = Sprite("bolinha.png", 1)
bola.x = janela.width/2 - bola.width/2
bola.y = janela.height/2 - bola.height/2
velx = 0.5
vely = 0.5

# Game Loop
while(True):
    janela.update()
    janela.set_background_color(RGB=[0,0,0])
    bola.draw()
    bola.move_x(velx) # bola.x = bola.x + velx
    bola.move_y(vely) # bola.y = bola.y + vely
    
    # Colisões
    if bola.x + bola.width >= janela.width or bola.x <= 0:
        velx = -velx
    elif bola.y + bola.height >= janela.height or bola.y <= 0:
        vely = -vely