import pygame, sys
import numpy as np
import time

pygame.init()


#Ancho y Alto de la pantalla
width = 1000
height = 1000

#creacion de la pantalla
screen = pygame.display.set_mode((height, width))
#color de fondo
bg = 25, 25, 25

#pintamos el fondo con el color elejido
screen.fill(bg)


nxC = 25
nyC = 25

dimCW = width / nxC
dimCH = height / nyC

#Estado de las celdas life = 1 death = 0
gameState = np.zeros((nxC, nyC))
 
#automata palo
#gameState[5, 3] = 1
#gameState[5, 4] = 1
#gameState[5, 5] = 1


gameState[21, 21] = 1
gameState[22, 22] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1





pause = True

#bucle de ejcucion


while True:

	newGameState = np.copy(gameState)
	screen.fill(bg)
	time.sleep(0.1)

	ev = pygame.event.get()
	

	for event in ev:

		if event.type ==  pygame.QUIT:
			sys.exit()


		if event.type  == pygame.KEYDOWN:
			pause = not pause
		
		if sum(pygame.mouse.get_pressed()) > 0:
			posx, posy = pygame.mouse.get_pos()
			celx, cely = int(np.floor(posx/dimCW)), int(np.floor(posy/dimCH))
			newGameState[celx, cely] = not pygame.mouse.get_pressed()[2]




	for y in range(0, nxC):
		for x in range(0,nyC):
			if not pause:
				nNeigh = gameState[(x-1) % nxC, (y-1) % nyC] + gameState[(x) % nxC, (y-1) % nyC] + gameState[(x+1) % nxC , (y-1) % nyC] + gameState[(x-1) % nxC, (y) % nyC] + gameState[(x+1) % nxC, (y) % nyC] + gameState[(x-1) % nxC, (y+1) % nyC] + gameState[(x) % nxC, (y+1) % nyC] + gameState[(x+1) % nxC, (y+1) % nyC]

				if gameState[x, y] == 0 and nNeigh == 3:
					newGameState[x, y] = 1
				elif gameState[x, y] == 1 and (nNeigh < 2 or nNeigh > 3):
					newGameState[x, y] = 0
			
			poly = [((x) * dimCW, y * dimCH), ((x+1) * dimCW, y * dimCH) , ((x+1) * dimCW, (y+1) * dimCH), ((x) * dimCW, (y+1) * dimCH)]

			if newGameState[x, y] == 0:
				pygame.draw.polygon(screen,(128, 128, 128), poly, 1)
			else:
				pygame.draw.polygon(screen, (255, 255, 255), poly, 0)



	gameState = np.copy(newGameState)
	pygame.display.flip()
