# coding: utf-8
import pygame

pygame.init()
tela = pygame.display.set_mode((700,500))
pygame.display.set_caption("Jogo das Rainhas")
relogio = pygame.time.Clock()

# carrega imagens
dragao = pygame.image.load('imagens/dragao.png')
# reduz tamanho do dragão
dragao = pygame.transform.scale(dragao, (110,60))
cenario = pygame.image.load('imagens/cenario.png')
seta = pygame.image.load('imagens/seta.png')

pos_dragao_x = -200
vel_dragao = 6
pos_seta_y = 378
vel_seta = 0

pontos = 0
rodando = True

while rodando:
    relogio.tick(24)  # fps
    # fill recebe valores RGB ([vermelho, verde, azul])
    # ou cor em formato html: pygame.Color('#112233')
    tela.fill([255,255,255])
    # blit recebe uma imagem e uma posição (x,y)
    tela.blit(cenario, (0,0))
    tela.blit(seta, (344,pos_seta_y))
    tela.blit(dragao, (pos_dragao_x,30))
    pygame.display.flip()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            vel_seta = 10

    # movimenta o dragao em x
    pos_dragao_x = pos_dragao_x + vel_dragao
    if pos_dragao_x > 800:
        pos_dragao_x = -200

    # disparo
    if vel_seta > 0:
        pos_seta_y = pos_seta_y - vel_seta
        if pos_seta_y < -120:
            pos_seta_y = 378
            vel_seta = 0

    if pos_seta_y <= 100      \
       and pos_dragao_x > 280 \
       and pos_dragao_x < 400:
        pontos = pontos + 10
        pos_dragao_x = -200