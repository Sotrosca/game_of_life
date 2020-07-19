import sys, pygame, time
import GameLogic

pygame.init()

size = width, height = 800, 800

cellSize = 20

cells_x = width // cellSize
cells_y = height // cellSize
 
backgroundColor = 25, 25, 25

screen = pygame.display.set_mode(size)

game = GameLogic.GameLogic(cells_x, cells_y)


paused = False
#game loop
while True:
	for event in pygame.event.get():

		if event.type == pygame.QUIT: sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_p:
				paused = not paused


		mouseClick = pygame.mouse.get_pressed()
			
		if mouseClick[0] == 1:

			mousePosition = pygame.mouse.get_pos()

			mouseCellX = mousePosition[0] // cellSize
			mouseCelly = mousePosition[1] // cellSize

			game.changeCellState(mouseCellX, mouseCelly)



	screen.fill(backgroundColor)

	# Render game and calculate new state if the game is not paused
	for i in range(cells_y):

		for j in range(cells_x):
			if not paused:
				game.applyGameRule(i, j)

			rect = pygame.Rect((i * cellSize, j * cellSize), (cellSize + 1, cellSize + 1))

			if game.isCellAlive(i, j):
				pygame.draw.rect(screen, (175, 175, 175), rect, 0)
			else:
				pygame.draw.rect(screen, (20, 20, 20), rect, 1)


	pygame.display.flip()

	pygame.time.delay(10)

	if not paused: 
		game.updateBoardState()