# coding: utf-8
import pygame
pygame.init()
tela = pygame.display.set_mode((700,500))
tela.fill([255,255,255])
pygame.display.set_caption("Meu game")
relogio = pygame.time.Clock()
relogio.tick(60)
img_dragao = pygame.image.load('dragao.png')
area_dragao = pygame.Rect(30, 30, 200, 115)
tela.blit(img_dragao, area_dragao)
pygame.display.flip()
