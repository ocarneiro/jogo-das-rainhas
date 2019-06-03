# coding: utf-8
import pygame

pygame.init()
tela = pygame.display.set_mode((700,500))
pygame.display.set_caption("Meu")
relogio = pygame.time.Clock()

# carrega imagens
heroi = pygame.image.load('heroi.png')

pontos = 0
rodando = True

fonte = pygame.font.Font(None, 60)

while rodando:
    relogio.tick(24)  # fps
    tela.fill([255,255,255])
    tela.blit(heroi, (300,300))

    texto = fonte.render(str(pontos), True, (0,0,0))
    tela.blit(texto, (20, 20))

    pygame.display.flip()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            print("Você fez %d pontos" % pontos)
        if evento.type == pygame.KEYDOWN:
            pontos = pontos + 1