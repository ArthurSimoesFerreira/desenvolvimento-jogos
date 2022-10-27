from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import random
from adjust_bullet import *
from bullet_bullet_collision import *
from check_enemy_collision import *
from draw import *
from shooter import *
from update_counters import *

random.seed()

SPEED = 1
GAME_STATE = 0 
"""
Controla em que estágio o jogo se encontra:
0 - Menu Inicial
1 - Dificuldade
2 - Ranking
3 - Jogo
4 - Finalização do jogo (Pontuação)
"""

# Largura da janela
width = 900
# Altura da janela
height = 650
# Cor de fundo
background_color = [0, 0, 0]
# Titulo da janela
title = "Space Invaders"

window = Window(width, height)
window.set_title(title)
window.set_background_color(background_color)

#Background Images
background_01 = GameImage("space_invaders_final\\assets\\background_space_invaders.png")
background_02 = GameImage("space_invaders_final\\assets\\background_space.png")
# Respectivas posições iniciais
background_01.y = 0
background_02.y = 0
# Velocidade de rolagem
background_roll_speed = 50

# Teclado e Mouse
keyboard = window.get_keyboard()
mouse = window.get_mouse()

# Efeito Sonoro
# bullet_sound = Sound("bullet_sound.ogg")

# Sprite da nave do jogador
player = Sprite("space_invaders_final\\assets\\spaceship.png")
 
# Posição inicial
player.set_position((window.width - player.width)/2, (window.height - player.height))
# Velocidade do jogador
player.speed = 200
# Direção do jogador
player.direction = -1  # [cima]
# Pontuação
player.score = 0

# Sprite dos inimigos
enemy_image = "space_invaders_final\\assets\\monster.png"
# Velocidade dos inimigos
enemy_speed = 200  
# Direção dos inimigos
enemy_direction = 1  # [baixo] 
# Numero de linhas da matriz
matrix_x = 6
# Numero de coluna da matriz
matrix_y = 6

# Sprite dos botões
button_back = Sprite("space_invaders_final\\assets\\button_back.png")
button_difficulty = Sprite("space_invaders_final\\assets\\button_difficulty.png")
button_easy = Sprite("space_invaders_final\\assets\\button_easy.png")
button_exit = Sprite("space_invaders_final\\assets\\button_exit.png")
button_hard = Sprite("space_invaders_final\\assets\\button_hard.png")
button_medium = Sprite("space_invaders_final\\assets\\button_medium.png")
button_play = Sprite("space_invaders_final\\assets\\button_play.png")
button_ranking = Sprite("space_invaders_final\\assets\\button_ranking.png")
# Posição dos botões
button_back.x = 30
button_back.y = 30
button_easy.x = window.width/2 - button_easy.width/2
button_easy.y = window.height/4 - button_easy.height/2
button_medium.x = window.width/2 - button_medium.width/2
button_medium.y = window.height*2/4 - button_medium.height/2
button_hard.x = window.width/2 - button_hard.width/2
button_hard.y = window.height*3/4 - button_hard.height/2
button_play.x = window.width/5 - button_play.width/2
button_play.y = 500 - button_play.height
button_ranking.x = window.width*2/5 - button_ranking.width/2
button_ranking.y = 500 - button_ranking.height
button_difficulty.x = window.width*3/5 - button_difficulty.width/2
button_difficulty.y = 500 - button_difficulty.height
button_exit.x = window.width*4/5 - button_exit.width/2
button_exit.y = 500 - button_exit.height

# Lista de Tiros e Matriz de Inimigos
bullets = []
enemies = [[0 for _ in range(10)] for _ in range(10)]

enemy_shoot_delay = 1/SPEED 
player.shoot_delay = 1/SPEED * 0.5
player.shoot_tick = player.shoot_delay

def win():
    """
    Função para verificar se o jogador ganhou
    Caso afirmativo, reinicia o jogo
    """
 
    # Criamos o acesso às variáveis globais
    global GAME_STATE
    global enemies

    # Criamos uma variável de controle, para sabermos se o jogador ganhou o jogo
    won = True
 
    # Verifica em todas as linhas se ainda existe algum inimigo vivo
    for row in range(matrix_x):
        if won:
            for column in range(matrix_y):
                if enemies[row][column] != 0:
                    # Se ele encontrar algum inimigo vivo, seta a variável
                    # won como False e quebra a cadeia de repetições
                    won = False
                    break
 
    if won:
        # Se o jogo percorrer toda a matriz e não encontrar 
        # nenhum inimigo vivo, reinicia o jogo
        GAME_STATE = 4


def enemy_movement():
    """
    Realiza a movimentação de cada inimigo
    """

    global enemy_direction

    # Cria variável de controle
    inverted = False

    # Calcula a nova posição da matriz de inimigos
    new_position = enemy_speed * enemy_direction * window.delta_time() * SPEED

    # Percorre toda a matriz de inimigos
    for row in range(matrix_x):
        for column in range(matrix_y):
            # Caso a posição esteja preenchida, isto é, o inimigo
            # ainda esteja vivo, efetua as ações em seguida
            if enemies[row][column] != 0:
                # Move o inimigo para sua nova posição
                enemies[row][column].move_x(new_position)

                # Caso já tenha alcançado o intervalo de disparo,
                # efetua um novo disparo
                if enemies[row][column].shoot_tick > enemies[row][column].shoot_delay:
                    shoot(enemies[row][column], bullets)
                    enemies[row][column].shoot_tick = 0

                    # Gera um novo intervalo de disparo aleatório
                    enemies[row][column].shoot_delay = random.uniform(0,15)/ SPEED

                # Verifica se nenhuma extremidade da matriz bateu na parede
                if not inverted:
                    # Se bateu na parede, então inverte a direção da matriz
                    # Altera direção para direita
                    if enemies[row][column].x <= 0:                         
                        enemy_direction = 1                         
                        inverted = True                     
                        # Altera direção para esquerda                     
                    elif enemies[row][column].x + Sprite(enemy_image).width >= window.width:
                        enemy_direction = -1
                        inverted = True
                    


def spawn_enemy():
    """
    Gera a matriz de inimigos
    :param i: numero de linhas na matriz
    :param j: numero de colunas na matriz
    :param enemy_matrix: matriz de inimigos
    """
    global enemies

    enemies = [[0 for _ in range(matrix_y)] for _ in range(matrix_x)]

    # for x e for y percorrem cada elemento da matriz
    for x in range(matrix_x):
        for y in range(matrix_y):
            # Cria o Sprite do inimigo
            enemy = Sprite(enemy_image)
            # Define a posição
            enemy.set_position(x * enemy.width, y * enemy.height)
            # Define a direção do movimento, no caso para baixo
            enemy.direction = 1  # 1 = para baixo
            # Define randomicamente o intervalo entre os disparos
            enemy.shoot_delay = random.uniform(0,15)/SPEED
            # Zera a variável de controle de disparos
            enemy.shoot_tick = 0
            # Coloca o inimigo recém criado na matriz
            enemies[x][y] = enemy


def restart():
    """
    Função para (re)iniciar o jogo.
    :param player: jogador
    :param enemies: matriz de inimigos
    :param bullets: lista de instancias de balas
    """
 
    # Gera o acesso às variáveis globais
    global matrix_x
    global matrix_y

    # Deleta todos os objetos enemies e bullets
    enemies.clear()
    bullets.clear()
 
    # Retorna o jogador à posição e pontuação inicial do jogo
    player.score = 0
    player.set_position((window.width - player.width)/2,
                        (window.height - player.height))
 
    # Reinicia os contadores de disparos
    player.shoot_tick = player.shoot_delay
 
    spawn_enemy()


def restart_window():
    """
    Reinicia o jogo
    """

    # Desenha os botões (play para jogar de novo) (back para voltar ao menu)
    button_back.draw()
    button_play.draw()
    # Acessando variável global
    global GAME_STATE
 
    # Escreve na tela a pontuação do jogador
    window.draw_text("Sua pontuação foi:" +
            str(player.score), 5,5, 25, (255,255,255), "Calibri", True)
 
    if mouse.is_button_pressed(1):
        # Clicou em "BACK"
        if mouse.is_over_object(button_back):
            GAME_STATE = 0
        # Clicou em "Play"
        if mouse.is_over_object(button_play):
            # A partida fica ativa
            GAME_STATE = 3
            # Reinicia o jogador, os inimigos e os disparos
            restart()


def player_movement():
    """
    Ação de movimento da nave do jogador
    """

    # Atualiza a posição do jogador
    player.move_key_x(player.speed * window.delta_time() * SPEED)
 
    # Não permite que a lateral esquerda da nave ultrapasse a
    # lateral esquerda da tela, onde x = 0
    if player.x <= 0:         
        player.x = 0     # Não permite que a lateral esquerda da nave ultrapasse a     # lateral direita da tela, onde x = largura da tela.     
    if player.x + player.width >= window.width:
        player.x = window.width - player.width


def bullet_movement():
    """
    Realiza a movimentação de cada bala em jogo
    """

    # Para cada bala instanciada no jogo
    for b in bullets:
 
        # Atualiza a sua posição, baseado em sua direção
        b.move_y(200 * b.direction * window.delta_time() * SPEED)
 
        # Verifica se saiu da tela e, caso tenha saído, destrói o projétil
        if b.y < -b.height or b.y > window.height + b.height:
            bullets.remove(b)


def player_shoot():
    """
    Ação de atirar
    """
    
    # Verifica se o jogador apertou o botão de disparar
    if keyboard.key_pressed("space"):
        # Verifica se já pode disparar
        if player.shoot_tick > player.shoot_delay:
            # Chama a função shoot(), para que ela efetue do disparo
            shoot(player, bullets)


def bullet_ship_collision():
   """
   Verifica se os disparos colidiram com alguma nave
   """
 
   # Acessando variável global
   global GAME_STATE
 
   # Para cada instância dos disparos
   for b in bullets:
       # Se for disparo do jogador
       if b.direction == -1:
           # Verifica se bateu em algum inimigo
           check_enemy_collision(b, matrix_x, matrix_y, enemies, bullets, player)
 
       # Se for disparo do inimigo
       elif b.direction == 1:
           # Verifica se bateu no jogador
           if b.collided(player):
               # Se bateu no jogador, define o fim de jogo
               GAME_STATE = 4

def menu_window():
    global GAME_STATE

    button_play.draw()
    button_ranking.draw()
    button_difficulty.draw()
    button_exit.draw()
    if mouse.is_button_pressed(1):
        if mouse.is_over_object(button_play):
            GAME_STATE = 3
            restart()
        if mouse.is_over_object(button_ranking):
            pass
        if mouse.is_over_object(button_difficulty):
            GAME_STATE = 1
        if mouse.is_over_object(button_exit):
            window.close()   

def difficulty_window():
    global GAME_STATE
    global SPEED
    global matrix_x
    global matrix_y


    button_back.draw()
    button_easy.draw()
    button_medium.draw()
    button_hard.draw()

    if mouse.is_button_pressed(1):
        if mouse.is_over_object(button_back):
            GAME_STATE = 0
        if mouse.is_over_object(button_easy):
            SPEED = 1
            matrix_x = 6
            matrix_y = 6
            GAME_STATE = 0
        if mouse.is_over_object(button_medium):
            SPEED = 1.3
            matrix_x = 8
            matrix_y = 7
            GAME_STATE = 0
        if mouse.is_over_object(button_hard):
            SPEED = 1.5
            matrix_x = 10
            matrix_y = 9
            GAME_STATE = 0



while True:
    # Apaga a tela completamente
    window.set_background_color(background_color)
 
    # Se o estado de jogo for = 0, quer dizer que é a primeira
    # vez que o game loop é acionado. Logo, ele cria a janela do
    # jogo.
    if GAME_STATE == 0:
        background_01.draw()
        menu_window()
        
    if GAME_STATE == 1:
        background_02.draw()
        difficulty_window()

    # Se não for a primeira vez, quer dizer que a partida ainda
    # está acontecendo. 
    elif GAME_STATE == 3:
        background_02.draw()
 
        # Verifica se o jogador venceu a partida
        win()
 
        # Atualiza os contadores
        update_counters(player, matrix_x, matrix_y, enemies, window)
 
        # Atualiza a movimentação do jogador
        player_movement()
 
        # Controle os tiros a cada intervalo
        player_shoot()
 
        # Atualiza o movimento dos disparos
        bullet_movement()
 
        # Atualiza o movimento dos inimigos
        enemy_movement()
 
        # Verifica a colisão de projéteis contra naves
        bullet_ship_collision()
 
        # Verifica colisões entre projéteis
        bullet_bullet_collision(bullets)
 
        ## Renderiza todos os dados na tela ##
        draw(bullets, matrix_x, matrix_y, enemies, player)
 
    # Caso o jogo tenha terminado (GAME_STATE = 2), reinicia
    # a partida do jogo.
    elif GAME_STATE == 4:
        restart_window()
 
    # Atualiza a janela de jogo cada vez que o game loop roda
    window.update()