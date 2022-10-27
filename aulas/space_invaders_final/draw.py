def draw(bullets, matrix_x, matrix_y, enemies, player):
    """
    Desenha todos os elementos na tela
    """
 
    # Desenha todas as instâncias de projétil
    for b in bullets:
        b.draw()
 
    # Percorre todo a matriz de inimigos
    for row in range(matrix_x):
        for column in range(matrix_y):
            # Se o inimigo estiver vivo (!=0), desenha o inimigo
            if enemies[row][column] != 0:
                enemies[row][column].draw()
 
    # Desenha a nave do jogador
    player.draw()