from PPlay.window import*
from PPlay.sprite import*
from PPlay.keyboard import*
from PPlay.collision import*

# Janela
janela = Window(600, 600)
janela.set_background_color(RGB=[0,0,0])

# Pad
rpad = Sprite("pad.png", 1)
rpad.x = janela.width - rpad.width - 1
rpad.y = janela.height/2 - rpad.height/2

lpad = Sprite("pad.png", 1)
lpad.x = 1
lpad.y = janela.height/2 - lpad.height/2

velxPad = 400
velyPad = 400

# Bolinha
bola = Sprite("bolinha.png", 1)
bola.x = janela.width/2 - bola.width/2
bola.y = janela.height/2 - bola.height/2
velxBola = 300  # 0.5 pixels/frame
velyBola = 300 

# Teclado
teclado = Window.get_keyboard()

# Game Loop
while(True):
    janela.update()
    janela.set_background_color(RGB=[0,0,0])
    bola.draw()
    bola.move_x(velxBola * janela.delta_time()) # bola.x = bola.x + velxBola
    bola.move_y(velyBola * janela.delta_time()) # bola.y = bola.y + velyBola
    
    # Colisões
    if Collision.collided(bola, rpad) or Collision.collided(bola, lpad):
        velxBola = -velxBola
    if bola.x + velxBola * janela.delta_time() >= janela.width or bola.x + bola.width + velxBola * janela.delta_time() <= 0:
        bola.x = janela.width/2 - bola.width/2
        bola.y = janela.height/2 - bola.height/2
    elif bola.y + bola.height + velyBola * janela.delta_time() >= janela.height or bola.y + velyBola * janela.delta_time() <= 0:
        velyBola = -velyBola
    
    # Pad
    lpad.draw()
    rpad.draw()

    if teclado.key_pressed("UP"):
        rpad.move_y(-velyPad * janela.delta_time())
    elif teclado.key_pressed("DOWN"):
        rpad.move_y(velyPad * janela.delta_time())

    if teclado.key_pressed("W"):
        lpad.move_y(-velyPad * janela.delta_time())
    elif teclado.key_pressed("S"):
        lpad.move_y(velyPad * janela.delta_time())