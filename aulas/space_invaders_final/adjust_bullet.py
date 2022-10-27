def adjust_bullet(actor, bullet):
    """
    Recebe o atirador e a bala, e ajusta sua posição
    :param actor: Instancia do jogador ou inimigo
    :param bullet: Instancia do projétil
    """
 
    # Calcula posição X da bala, utilizando como referência o 
    # centro do ator e armazena em x_fire
    x_fire = actor.x + (actor.width / 2) - (bullet.width / 2)
 
    # Calcula posição Y do projétil, utilizando como referência
    # a direção de movimento e o tamanho do jogador, salvando
    # o resultado na variável y_fire
    if actor.direction == -1:
        y_fire = actor.y
    elif actor.direction == 1:
        y_fire = actor.y + actor.height - bullet.height
 
    # Transfere o valor das variáveis auxiliares x_fire e y_fire
    # para o projétil
    bullet.x = x_fire
    bullet.y = y_fire
     
    # Define direção do projétil
    bullet.direction = actor.direction