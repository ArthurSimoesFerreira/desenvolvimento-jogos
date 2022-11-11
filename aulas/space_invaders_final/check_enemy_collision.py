def check_enemy_collision(b, matrix_x, matrix_y, enemies, bullets, player):
    """
    Verifica se o projétil colidiu com o inimigo
    :param b: Instância de projétil
    """

    enemies.reverse()
    # Percorre toda a matriz de inimigos
    if b.x < enemies[-1][0].x or b.y < enemies[-1][0].y or b.x > enemies[0][-1].x or b.y > enemies[0][-1].y:
        for row in range(matrix_x):
            for column in range(matrix_y):
                if enemies[row][column] != 0:
                # Se o inimigo ainda estiver vivo (enemies<div class="row"></div><div class=""></div> != 0),
                # verifica se o disparo b colidiu com o mesmo
                    if b.collided(enemies[row][column]) and enemies[row][column].exist != 0:
                    # Caso tenha havido colisão, remove a bala e o
                    # inimigo do jogo

                        bullets.remove(b)
                        enemies[row][column].exist = 0

                        # Atualiza a pontuação do jogador
                        player.score += 50

                        # Interrompe a função, pois o projétil foi destruído
                        # e não poderá colidir com mais nenhum inimigo
                        return