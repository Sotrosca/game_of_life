import sys, pygame
import GameLogic

print("Commands:")
print("--- p -> Pause ---")
print("--- s -> One step ---")
print("--- Click cells to edit them and press p or s to continue---")
print("--- Enjoy !! ---")

pygame.init()

size = width, height = 900, 600

cellSize = 15

cells_x = width // cellSize
cells_y = height // cellSize

backgroundColor = 25, 25, 25

title = pygame.display.set_caption("Game of Life")
screen = pygame.display.set_mode(size)

game = GameLogic.GameLogic(cells_x, cells_y)


paused = True
oneStep = False
lastCellClicked = (-1, -1)


#game loop
while True:

	if oneStep:
		paused = True
		oneStep = False

	for event in pygame.event.get():

		if event.type == pygame.QUIT: sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_p:
				paused = not paused
				print("The game is paused, press p to continue") if paused else print("Game running")
			if event.key == pygame.K_s:
				print("One step")
				oneStep = True
				paused = False
		if event.type == pygame.MOUSEBUTTONUP:
			lastCellClicked = (-1, -1)

	mouseClick = pygame.mouse.get_pressed()
		
	if mouseClick[0] == 1:

		mousePosition = pygame.mouse.get_pos()

		mouseCellX = mousePosition[0] // cellSize
		mouseCellY = mousePosition[1] // cellSize

		if lastCellClicked[0] != mouseCellX or lastCellClicked[1] != mouseCellY:

			game.changeCellState(mouseCellX, mouseCellY)

			lastCellClicked = (mouseCellX, mouseCellY)

	screen.fill(backgroundColor)

	# Render game and calculate new state if the game is not paused
	for i in range(cells_x):

		for j in range(cells_y):
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