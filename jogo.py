# coding: utf-8
import pygame

pygame.init()
tela = pygame.display.set_mode((700,500))
pygame.display.set_caption("Meu game")
relogio = pygame.time.Clock()

img_dragao = pygame.image.load('imagens/dragao.png')
pos_dragao = -200
vel_dragao = 8
rodando = True

while rodando:
    relogio.tick(24)
    # fill recebe uma cor RGB ([vermelho, verde, azul])
    # ou cor em formato html '#112233'
    tela.fill(pygame.Color('#f2f2f2'))
    # blit recebe uma imagem e uma posição (x,y)
    tela.blit(img_dragao, (pos_dragao,30))
    pygame.display.flip()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # movimenta o dragao em x
    pos_dragao = pos_dragao + vel_dragao
