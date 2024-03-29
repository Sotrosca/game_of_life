import numpy as np
import copy

class GameLogic():
	def __init__(self, width, heigth):
		self.width = width
		self.heigth = heigth
#		self.boardState = np.random.randint(2, size=(heigth, width))
		self.boardState = np.zeros((heigth, width), dtype=int)

		self.newBoardState = copy.deepcopy(self.boardState)

	def isCellAlive(self, x, y):
		return self.boardState[y, x] == 1

	def changeCellState(self, x, y):
		self.boardState[y, x] = int(not self.boardState[y, x])

	def computeNeighboursAmount(self, y, x):
		neighbours = 0

		for i in range(-1, 2):
			for j in range(-1, 2):
				neighbours += self.boardState[(y + i) % self.heigth,
											  (x + j) % self.width]

		neighbours -= self.boardState[y, x]

		return neighbours

	def applyGameRule(self, x, y):
		neighboursAmount = self.computeNeighboursAmount(y, x)
		if neighboursAmount == 3:
			self.newBoardState[y, x] = 1
		elif self.isCellAlive(x, y) and neighboursAmount == 2:
			self.newBoardState[y, x] = 1
		else:
			self.newBoardState[y, x] = 0

	def updateBoardState(self):

		self.boardState = copy.deepcopy(self.newBoardState)