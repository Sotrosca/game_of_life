import sys, pygame, time
import GameLogic

pygame.init()

size = width, height = 1200, 600

cellSize = 10

cells_x = width // cellSize
cells_y = height // cellSize

backgroundColor = 25, 25, 25

screen = pygame.display.set_mode(size)

game = GameLogic.GameLogic(cells_y, cells_x)

#game loop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	screen.fill(backgroundColor)

	for i in range(cells_x):

		for j in range(cells_y):

			game.applyGameRule(j, i)

			rect = pygame.Rect((i * cellSize, j * cellSize), (cellSize + 1, cellSize + 1))

			if game.isCellAlive(j, i):
				pygame.draw.rect(screen, (175, 175, 175), rect, 0)
			else:
				pygame.draw.rect(screen, (20, 20, 20), rect, 1)


	pygame.display.flip()

	time.sleep(0.01)
	game.updateBoardState()