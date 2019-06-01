# coding: utf-8
import pygame

pygame.init()
tela = pygame.display.set_mode((700,500))
pygame.display.set_caption("Jogo das Rainhas")
relogio = pygame.time.Clock()

img_dragao = pygame.image.load('imagens/dragao.png')
img_dragao = pygame.transform.scale(img_dragao, (110,60))

img_cenario = pygame.image.load('imagens/cenario.png')

pos_dragao = -200
vel_dragao = 6
rodando = True

while rodando:
    relogio.tick(24)  # fps
    # fill recebe valores RGB ([vermelho, verde, azul])
    # ou cor em formato html: pygame.Color('#112233')
    tela.fill([255,255,255])
    # blit recebe uma imagem e uma posição (x,y)
    tela.blit(img_cenario, (0,0))
    tela.blit(img_dragao, (pos_dragao,30))
    pygame.display.flip()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # movimenta o dragao em x
    pos_dragao = pos_dragao + vel_dragao
