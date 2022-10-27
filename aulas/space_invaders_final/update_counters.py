def update_counters(player, matrix_x, matrix_y, enemies, window):
    """
    Atualiza contadores do jogo
    """
 
    # Atualiza o contador de controle de tiro do jogador
    player.shoot_tick += window.delta_time()
 
    # Atualiza o contador de controle de tiro de cada inimigo
    # presente na matriz de inimigos
    for row in range(matrix_x):
        for column in range(matrix_y):
            if enemies[row][column] != 0:
                enemies[row][column].shoot_tick += window.delta_time()
