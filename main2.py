import pygame
from random import randint

# Inicializar o pygame
pygame.init()

# Configurar a janela do jogo
janela = pygame.display.set_mode([1920, 1080])
pygame.display.set_caption('Jogo do Gabriel')

# Carregar imagens
imagem_fundo = pygame.image.load('img/Ednaldo game.jpg')
goku_ssj = pygame.image.load('C:/Users/Upinfinitoo/Documents/primeiro arquivo1/img/goku ssj.png')
naruto = pygame.image.load('img/naruto.png')
esfera_energia = pygame.image.load('img/Esfera energia.png')  # Poder do Goku
kunai = pygame.image.load('img/Kunai.png')  # Poder do Naruto

# Escalar os poderes
esfera_energia = pygame.transform.scale(esfera_energia, (40, 40))
kunai = pygame.transform.scale(kunai, (40, 40))

# Posição do Goku (Player 1)
pos_y_goku = 600
pos_x_goku = 600
vel_goku = 15

# Posição do Naruto (Player 2)
pos_y_naruto = 50
pos_x_naruto = randint(0, 1500)
vel_naruto = 10

# Variáveis para os poderes
esfera_ativa = False
pos_x_esfera = pos_x_goku
pos_y_esfera = pos_y_goku

kunai_ativa = False
pos_x_kunai = pos_x_naruto
pos_y_kunai = pos_y_naruto

# Variável de controle do loop
loop = True

# Loop principal do jogo
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False