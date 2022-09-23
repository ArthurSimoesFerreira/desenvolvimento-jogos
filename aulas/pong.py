from PPlay.window import*
from PPlay.sprite import*
from PPlay.keyboard import*
from PPlay.collision import*


# Variáveis Numéricas e Booleanas
rpontos = 0
lpontos = 0
colisoesComPad = 0
duasBolinhas = False

# Fonte 
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

# Bola 1
bola1 = Sprite("bolinha.png", 1)
bola1.x = janela.width/2 - bola1.width/2
bola1.y = janela.height/2 - bola1.height/2
velxBola = 300  
velyBola = 300 

# Bola 2
bola2 = Sprite("bolinha.png", 1)
bola2.x = janela.width/2 - bola2.width/2
bola2.y = janela.height/2 - bola2.height/2
velxBola2 = 300  
velyBola2 = 300 

# Teclado
teclado = Window.get_keyboard()


# Game Loop
while(True):
    janela.update()
    janela.set_background_color(RGB=[0,0,0])
    bola1.draw()
    bola1.move_x(velxBola * janela.delta_time()) # bola1.x = bola1.x + velxBola
    bola1.move_y(velyBola * janela.delta_time()) # bola1.y = bola1.y + velyBola
    
    # Colisões da Bola1 com Pads
    if Collision.collided(bola1, rpad):
        bola1.x -= 1
        velxBola = -velxBola
        if not(duasBolinhas):
            colisoesComPad += 1
    elif Collision.collided(bola1, lpad):
        bola1.x += 1
        velxBola = -velxBola
        if not(duasBolinhas):
            colisoesComPad += 1
    
    # Aparição da nova Bolinha
        if colisoesComPad == 3:
            duasBolinhas = True

    

    # Colisão bola1 com lado direito
    if bola1.x + velxBola * janela.delta_time() >= janela.width:
        bola1.x = janela.width/2 - bola1.width/2
        bola1.y = janela.height/2 - bola1.height/2
        lpontos += 1

    # Colisão bola1 com lado esquerdo    
    elif bola1.x + bola1.width + velxBola * janela.delta_time() <= 0:  
        bola1.x = janela.width/2 - bola1.width/2
        bola1.y = janela.height/2 - bola1.height/2
        rpontos += 1

    # Colisão bola1 com lados de cima e de baixo
    elif bola1.y + bola1.height + velyBola * janela.delta_time() >= janela.height or bola1.y + velyBola * janela.delta_time() <= 0:
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
    
    # Teclado
    if teclado.key_pressed("W"):
        lpad.move_y(-velyPad)
    elif teclado.key_pressed("S"):
        lpad.move_y(velyPad)

    # Placar de pontos
    mensagemPontos = f"{lpontos}    {rpontos}"
    agrupamentoPontos = fonte.render(mensagemPontos, False, (255,255,255))
    textoPontos = agrupamentoPontos.get_rect()
    textoPontos.center = (janela.width/2, janela.height/2)
    tela.blit(agrupamentoPontos, (janela.width/2 - textoPontos.width/2 ,50))

    