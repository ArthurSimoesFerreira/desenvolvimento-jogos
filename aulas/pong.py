from PPlay.window import*
from PPlay.sprite import*
from PPlay.keyboard import*
from PPlay.collision import*


# Variáveis Numéricas e Booleanas
rpontos = 0
lpontos = 0
colisoesComPad = 0
comecarJogo = False
bola1ColidiuEsq = False
bola2ColidiuEsq = False
duasBolinhas = False
bola1Dentro = True
bola2Dentro = False

# Fonte 
fonte = pygame.font.SysFont('arial', 40, True, False)

# Janela
janela = Window(900, 600)
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
velyPad = 0.35

# Bola 1
bola1 = Sprite("bolinha.png", 1)
bola1.x = janela.width/2 - bola1.width/2
bola1.y = janela.height/2 - bola1.height/2
velxBola1 = 450
velyBola1 = 450

# Bola 2
bola2 = Sprite("bolinha.png", 1)
bola2.x = janela.width/2 - bola2.width/2
bola2.y = janela.height/2 - bola2.height/2
velxBola2 = 450
velyBola2 = 450

# Teclado
teclado = Window.get_keyboard()


# Game Loop
while(True):
    janela.update()
    janela.set_background_color(RGB=[0,0,0])
    
    # Começar Jogo
    if comecarJogo == False:
        janela.draw_text(
            "Aperte ENTER para começar",
            30, 
            janela.height/2, 
            60, (255,255,255), 
            "Arial", 
            True, 
            False
        ) # janela.draw_text
        if teclado.key_pressed("ENTER"):
            comecarJogo = True
    else:
        if (colisoesComPad == 3) and not(duasBolinhas):
            colisoesComPad = 0
            bola2Dentro = True
            duasBolinhas = True

        ######################################## Bola 1 #####################################################

        if bola1Dentro:
            bola1.draw()
            bola1.move_x(velxBola1 * janela.delta_time()) # bola1.x = bola1.x + velxBola1
            bola1.move_y(velyBola1 * janela.delta_time()) # bola1.y = bola1.y + velyBola1
            
            # Colisões da Bola1 com Pads
            if Collision.collided(bola1, rpad) and bola1.x + bola1.width/1.5 + velxBola1 * janela.delta_time() < janela.width:
                bola1.x -= 2
                velxBola1 = -velxBola1
                if not(duasBolinhas):
                    colisoesComPad += 1
            elif Collision.collided(bola1, lpad) and bola1.x + bola1.width/2.5 + velxBola1 * janela.delta_time() > 0:
                bola1.x += 2
                velxBola1 = -velxBola1
                if not(duasBolinhas):
                    colisoesComPad += 1
            
            # Colisão bola1 com lado direito
            if bola1.x + velxBola1 * janela.delta_time() >= janela.width:
                bola1.x = janela.width/2 - bola1.width/2
                bola1.y = janela.height/2 - bola1.height/2
                lpontos += 1
                colisoesComPad = 0
                if bola2Dentro:
                    bola1Dentro = False
                else:
                    duasBolinhas = False

            # Colisão bola1 com lado esquerdo    
            elif bola1.x + bola1.width + velxBola1 * janela.delta_time() <= 0:  
                bola1.x = janela.width/2 - bola1.width/2
                bola1.y = janela.height/2 - bola1.height/2
                rpontos += 1
                colisoesComPad = 0
                if bola2Dentro:
                    bola1Dentro = False
                else:
                    duasBolinhas = False

            # Colisão bola1 com lados de cima e de baixo
            elif bola1.y + bola1.height + velyBola1 * janela.delta_time() >= janela.height or bola1.y + velyBola1 * janela.delta_time() <= 0:
                velyBola1 = -velyBola1

        ####################################### Bola 2 ##############################################

        if bola2Dentro:
            bola2.draw()
            bola2.move_x(velxBola2 * janela.delta_time()) # bola2.x = bola2.x + velxBola2
            bola2.move_y(velyBola2 * janela.delta_time()) # bola2.y = bola2.y + velyBola2
            
            # Colisões da Bola2 com Pads
            if Collision.collided(bola2, rpad) and bola2.x + bola2.width/2 + velxBola2 * janela.delta_time() < janela.width:
                bola2.x -= 2
                velxBola2 = -velxBola2
            elif Collision.collided(bola2, lpad) and bola2.x + bola2.width/2 + velxBola2 * janela.delta_time() > 0:
                bola2.x += 2
                velxBola2 = -velxBola2
            
            # Colisão bola2 com lado direito
            if bola2.x + velxBola2 * janela.delta_time() >= janela.width:
                bola2.x = janela.width/2 - bola2.width/2
                bola2.y = janela.height/2 - bola2.height/2
                lpontos += 1
                bola2Dentro = False
                colisoesComPad = 0
                if not(bola1Dentro):
                    duasBolinhas = False
                    bola1Dentro = True

            # Colisão bola2 com lado esquerdo    
            elif bola2.x + bola2.width + velxBola2 * janela.delta_time() <= 0:  
                bola2.x = janela.width/2 - bola2.width/2
                bola2.y = janela.height/2 - bola2.height/2
                rpontos += 1
                bola2Dentro = False
                colisoesComPad = 0
                if not(bola1Dentro):
                    duasBolinhas = False
                    bola1Dentro = True

            # Colisão bola2 com lados de cima e de baixo
            elif bola2.y + bola2.height + velyBola2 * janela.delta_time() >= janela.height or bola2.y + velyBola2 * janela.delta_time() <= 0:
                velyBola2 = -velyBola2

        ####################################### PADS ################################################

        # Colisão dos pads com as paredes
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

        ############################################ IA ##############################################
        
        if rpad.x - bola1.x < rpad.x - bola2.x or not(bola2Dentro):
            if velxBola1 > 0:
                if velyBola1 > 0:
                    rpad.move_y(velyPad)
                else:
                    rpad.move_y(-velyPad)
        else:
            if velxBola2 > 0:
                if velyBola2 > 0:
                    rpad.move_y(velyPad)
                else:
                    rpad.move_y(-velyPad)  

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

        