def bullet_bullet_collision(bullets):
   """
   Verifica se o projétil colidiu com alguma outro projétil
   """
 
   # Para cada instância de projétil
   for b1 in bullets:
       # Se for projétil do jogador
       if b1.direction == -1:
           # Verifica em todas as instâncias se ele colidiu com outro
           for b2 in bullets:
               # Verifica se o projétil atual é inimigo
               if b2.direction == 1:
                   # Se for inimigo, verifica se existiu colisão
                   if b1.collided(b2):
                       # Se houver colisão, remove os dois projéteis 
                       bullets.remove(b1)
                       bullets.remove(b2)
                         
                       break