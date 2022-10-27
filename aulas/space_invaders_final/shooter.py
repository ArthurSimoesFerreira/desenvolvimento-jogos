from PPlay.sprite import *
from adjust_bullet import *

def shoot(shooter, bullets):
    """
    Cria um bullet, associando-o a um ator
    :param shooter: Ator responsável pelo disparo (jogador ou inimigo)
    """
 
    # Reproduz o som do disparo
    # bullet_sound.play()
 
    # Zera o contador de último disparo
    shooter.shoot_tick = 0
 
    # Cria uma nova bullet, dependendo de quem for que atirou
    if shooter.direction == -1:
        b = Sprite("space_invaders_final\\assets\\shot.png")
    elif shooter.direction == 1:
        b = Sprite("space_invaders_final\\assets\\shot_monster.png")
         
    # Ajusta a posição inicial e a direção do projétil
    adjust_bullet(shooter, b)
 
    # Adiciona o novo projétil que criamos para ser desenhado na tela
    bullets.append(b)