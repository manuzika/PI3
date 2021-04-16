import os
import pygame
from jogo import *

def main():

    pygame.init()

    pygame.display.set_caption("WORD'S MAZE")
    icon = pygame.image.load("imagens/maze.png")
    pygame.display.set_icon(icon)
    personagem = pygame.image.load("imagens/frente.png")
    
    clock = pygame.time.Clock()
    jogador = Personagem() 

    running = True
    while running:
        
        clock.tick()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
        
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_LEFT]:
            personagem = pygame.image.load("imagens/lado_esquerdo.png")
            jogador.move(-2, 0)
        if tecla[pygame.K_RIGHT]:
            personagem = pygame.image.load("imagens/lado_direito.png")
            jogador.move(2, 0)
        if tecla[pygame.K_UP]:
            personagem = pygame.image.load("imagens/trás.png")
            jogador.move(0, -2)
        if tecla[pygame.K_DOWN]:
            personagem = pygame.image.load("imagens/frente.png")
            jogador.move(0, 2)
        if tecla[pygame.K_SPACE]:
            main()
        if tecla[pygame.K_LSHIFT]:
            pygame.quit()
        
        screen.fill((0, 0, 0)) 
        screen.blit(fundo, (0,0))
        
        if jogador.letra1_colisao == False:
            screen.blit(letra1, letras.rect1)
        else:
            pass

        if jogador.letra2_colisao == False:
            screen.blit(letra2, letras.rect2)
        else:
            pass

        if jogador.letra3_colisao == False:
            screen.blit(letra3, letras.rect3)
        else:
            pass

        if jogador.letra4_colisao == False:
            screen.blit(letra4, letras.rect4)
        else:
            pass

        for i in walls:
            screen.blit(parede, i.rect)
        screen.blit(personagem, jogador.rect)

        if jogador.letra1_colisao == True and jogador.letra2_colisao == True and jogador.letra3_colisao == True and jogador.letra4_colisao == True:
            tela_final = pygame.image.load("imagens/tela_final.png")
            screen.blit(tela_final, (0,0))

        pygame.display.flip()

if __name__ == "__main__":
    main()