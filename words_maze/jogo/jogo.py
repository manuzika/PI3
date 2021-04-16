import os 
import pygame

class Personagem(object):
    
    def __init__(self):
        self.rect = pygame.Rect(32, 32, 32, 32)
        self.letra1_colisao = False
        self.letra2_colisao = False
        self.letra3_colisao = False
        self.letra4_colisao = False

    def move(self, pos_x, pos_y):
        if pos_x != 0:
            self.move_eixo(pos_x, 0)
        if pos_y != 0:
            self.move_eixo(0, pos_y)
    
    def move_eixo(self, pos_x, pos_y):
        self.rect.x += pos_x
        self.rect.y += pos_y

        #Colisão, com base na velocidade
        for i in walls:
            if self.rect.colliderect(i.rect):
                if pos_x > 0: 
                    self.personagem = pygame.image.load("imagens/lado_esquerdo.png")
                    self.rect.right = i.rect.left
                if pos_x < 0: 
                    self.personagem = pygame.image.load("imagens/lado_direito.png")
                    self.rect.left = i.rect.right
                if pos_y > 0: 
                    self.personagem = pygame.image.load("imagens/trás.png")
                    self.rect.bottom = i.rect.top
                if pos_y < 0: 
                    self.personagem = pygame.image.load("imagens/frente.png")
                    self.rect.top = i.rect.bottom

        if self.rect.colliderect(letras.rect1):
            self.letra1_colisao = True
        elif self.rect.colliderect(letras.rect2):
            self.letra2_colisao = True
        elif self.rect.colliderect(letras.rect3):
            self.letra3_colisao = True
        elif self.rect.colliderect(letras.rect4):
            self.letra4_colisao = True


class Labirinto (object):
    
    def __init__(self, pos):
        self.parede = pygame.image.load("imagens/muro.png").convert_alpha()
        self.rect = parede.get_rect()
        screen.blit(parede, self.rect)

        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)

class Letra(object):

    def __init__(self):
        super().__init__()
        self.letra1 = pygame.image.load("imagens/i.png").convert_alpha()
        self.rect = letra1.get_rect()
        self.rect1 = pygame.Rect(736, 32, 32, 32)
        screen.blit(letra1, self.rect)

        self.letra2 = pygame.image.load("imagens/n.png").convert_alpha()
        self.rect = letra2.get_rect()
        self.rect2 = pygame.Rect(32, 544, 32, 32)
        screen.blit(letra2, self.rect)

        self.letra3 = pygame.image.load("imagens/f.png").convert_alpha()
        self.rect = letra3.get_rect()
        self.rect3 = pygame.Rect(352, 256, 32, 32)
        screen.blit(letra3, self.rect)

        self.letra4 = pygame.image.load("imagens/o.png").convert_alpha()
        self.rect = letra4.get_rect()
        self.rect4 = pygame.Rect(736, 512, 32, 32)
        screen.blit(letra4, self.rect)
        
fundo = pygame.image.load("imagens/fundo.png")
parede = pygame.image.load("imagens/muro.png")
letra1 = pygame.image.load("imagens/i.png")
letra2 = pygame.image.load("imagens/n.png")
letra3 = pygame.image.load("imagens/f.png")
letra4 = pygame.image.load("imagens/o.png")
screen = pygame.display.set_mode((800, 608))
letras = Letra()
walls = [] 
moldura = [
            ["i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i"],
            ["i", "g", "i", "g", "g", "g", "g", "i", "i", "i", "i", "g", "g", "g", "g", "g", "g", "i", "g", "g", "g", "g", "g", "g", "i"],
            ["i", "g", "i", "g", "g", "i", "g", "g", "g", "g", "i", "g", "i", "i", "i", "i", "g", "i", "g", "g", "i", "i", "g", "i", "i"],
            ["i", "g", "i", "i", "g", "i", "g", "i", "i", "i", "i", "g", "i", "g", "g", "i", "g", "i", "i", "g", "i", "g", "g", "g", "i"],
            ["i", "g", "g", "g", "g", "i", "g", "i", "g", "g", "g", "g", "i", "g", "i", "i", "g", "g", "g", "g", "i", "g", "i", "g", "i"],
            ["i", "g", "i", "i", "g", "i", "g", "g", "g", "i", "i", "i", "i", "g", "i", "g", "g", "i", "i", "g", "i", "g", "i", "g", "i"],
            ["i", "g", "g", "i", "g", "g", "g", "i", "g", "g", "g", "g", "g", "g", "i", "g", "i", "i", "g", "g", "g", "g", "i", "g", "i"],
            ["i", "g", "i", "i", "i", "i", "i", "i", "i", "i", "i", "g", "i", "i", "i", "g", "i", "g", "g", "g", "i", "g", "i", "g", "i"],
            ["i", "g", "g", "g", "g", "g", "g", "g", "g", "i", "g", "g", "i", "g", "g", "g", "i", "i", "i", "i", "i", "i", "i", "g", "i"],
            ["i", "i", "i", "g", "i", "i", "i", "i", "g", "i", "g", "i", "i", "g", "i", "i", "i", "g", "g", "g", "g", "g", "i", "g", "i"],
            ["i", "g", "g", "g", "g", "g", "g", "i", "g", "i", "g", "i", "g", "g", "g", "g", "g", "g", "i", "g", "g", "g", "i", "g", "i"],
            ["i", "g", "i", "i", "i", "i", "g", "i", "g", "i", "g", "i", "g", "i", "i", "g", "g", "i", "i", "g", "g", "g", "i", "g", "i"],
            ["i", "g", "i", "g", "g", "i", "g", "i", "g", "g", "g", "i", "g", "i", "g", "g", "i", "g", "g", "g", "f", "g", "i", "g", "i"],
            ["i", "g", "g", "g", "g", "i", "g", "i", "i", "i", "i", "i", "g", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "g", "i"],
            ["i", "g", "i", "g", "g", "i", "g", "g", "g", "g", "g", "i", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "i", "g", "i"],
            ["i", "i", "i", "g", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "g", "i", "i", "i"],
            ["i", "i", "g", "g", "g", "g", "g", "g", "g", "g", "i", "g", "g", "g", "i", "g", "g", "g", "i", "g", "g", "g", "i", "g", "i"],
            ["i", "g", "g", "i", "i", "i", "i", "i", "i", "g", "i", "g", "i", "g", "g", "g", "i", "g", "g", "g", "i", "g", "g", "g", "i"],
            ["i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "i"]
        ]

x = y = 0
for row in moldura:
    for col in row:
        if col == "i":
            Labirinto((x, y))
        x += 32
    y += 32
    x = 0