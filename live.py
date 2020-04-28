# live

import pygame
pygame.init()

tamanho = (700, 500)

tela = pygame.display.set_mode(tamanho)
dragao = pygame.image.load("imagens/dragao.png")
cenario = pygame.image.load("imagens/cenario.png")
seta = pygame.image.load("imagens/seta.png")

executando = True

x = -220

y_dragao = 50

y = 360
velocidade = 0

relogio = pygame.time.Clock()

while executando:
	relogio.tick(25)
	tela.fill((255, 255, 255))
	tela.blit(cenario, (0,0))
	tela.blit(seta, (342,y))
	tela.blit(dragao, (x,y_dragao))
	x = x + 10
	y = y - velocidade
	
	if x > 700:
		x = -220
		y_dragao = y_dragao + 100
	
	if y < 0:
		y = 360
		velocidade = 0
		
	if y == 100:
		if x >= 160 and x <= 400:
			print("Matou!")
			x = -220
			y_dragao = 50

	if y_dragao > 350:
		print("Morri!")
		print("Game over!!")
		executando = False
	
	pygame.display.flip()
	
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			executando = False
		if evento.type == pygame.KEYDOWN:
			velocidade = 10
		# print(evento)
	

