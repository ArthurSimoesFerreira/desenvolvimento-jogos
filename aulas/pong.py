from PPlay.window import*
from PPlay.sprite import*
from PPlay.keyboard import*
from PPlay.collision import*


#Pontos
rpontos = 0
lpontos = 0

#Fonte 
fonte = pygame.font.SysFont('arial', 40, True, False)

# Janela
janela = Window(900, 650)
janela.set_background_color(RGB=[0,0,0])

# Tela
tela = Window.screen

# Pad
rpad = Sprite("pad.png", 1)
rpad.x = janela.width - rpad.width - 1
rpad.y = janela.height/2 - rpad.height/2

lpad = Sprite("pad.png", 1)
lpad.x = 1
lpad.y = janela.height/2 - lpad.height/2

velyPad = 0.2

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
    if Collision.collided(bola, rpad):
        bola.x -= 1
        velxBola = -velxBola
    elif Collision.collided(bola, lpad):
        bola.x += 1
        velxBola = -velxBola

    # colisão bola com lado direito
    if bola.x + velxBola * janela.delta_time() >= janela.width:
        bola.x = janela.width/2 - bola.width/2
        bola.y = janela.height/2 - bola.height/2
        lpontos += 1

    # colisão bola com lado esquerdo    
    elif bola.x + bola.width + velxBola * janela.delta_time() <= 0:  
        bola.x = janela.width/2 - bola.width/2
        bola.y = janela.height/2 - bola.height/2
        rpontos += 1

    # colisão bola com lados de cima e de baixo
    elif bola.y + bola.height + velyBola * janela.delta_time() >= janela.height or bola.y + velyBola * janela.delta_time() <= 0:
        velyBola = -velyBola
    
    if rpad.y + velyPad * janela.delta_time() < 0:
        rpad.y = 0
    elif rpad.y + rpad.height + velyPad * janela.delta_time() > janela.height:
        rpad.y = janela.height - rpad.height

    if lpad.y + velyPad * janela.delta_time() < 0:
        lpad.y = 0
    elif lpad.y + lpad.height + velyPad * janela.delta_time() > janela.height:
        lpad.y = janela.height - lpad.height
 
    # Pad draw
    lpad.draw()
    rpad.draw()

    # IA
    if velxBola > 0:
        if velyBola < 0:
            rpad.move_y(-velyPad)
        else:
            rpad.move_y(velyPad)
    else:
        if velyBola < 0:
            lpad.move_y(-velyPad)
        else:
            lpad.move_y(velyPad)


    # Placar de pontos
    mensagemPontos = f"{lpontos}    {rpontos}"
    agrupamentoPontos = fonte.render(mensagemPontos, False, (255,255,255))
    textoPontos = agrupamentoPontos.get_rect()
    textoPontos.center = (janela.width/2, janela.height/2)
    tela.blit(agrupamentoPontos, (janela.width/2 - textoPontos.width/2 ,50))

    