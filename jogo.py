# coding: utf-8
import pygame

pygame.init()
tela = pygame.display.set_mode((700,500))
pygame.display.set_caption("Meu game")
relogio = pygame.time.Clock()

img_dragao = pygame.image.load('imagens/dragao.png')
pos_dragao = -200
rodando = True

while rodando:
    relogio.tick(24)
    tela.fill([255,255,255])
    area_dragao = pygame.Rect(pos_dragao, 30, 200, 112)
    tela.blit(img_dragao, area_dragao)
    pygame.display.flip()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    pos_dragao = pos_dragao + 2
