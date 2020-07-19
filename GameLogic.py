import numpy as np
import copy

class GameLogic():
	def __init__(self, width, heigth):
		self.width = width
		self.heigth = heigth
		self.boardState = np.random.randint(2, size=(heigth, width))
#		self.boardState = np.zeros((width, heigth), dtype=int)
#		self.boardState[20:28, 80] = 1
		self.newBoardState = copy.deepcopy(self.boardState)

	def isCellAlive(self, x, y):
		return self.boardState[x, y] == 1

	def computeNeighboursAmount(self, x, y):
		neighbours = 0

		for i in range(-1, 2):
			for j in range(-1, 2):
				neighbours += self.boardState[(x + i) % self.heigth,
											  (y + j) % self.width]

		neighbours -= self.boardState[x, y]

		return neighbours

	def applyGameRule(self, x, y):
		neighboursAmount = self.computeNeighboursAmount(x, y)
		if neighboursAmount == 3:
			self.newBoardState[x, y] = 1
		elif neighboursAmount != 2:
			self.newBoardState[x, y] = 0

	def updateBoardState(self):

		self.boardState = copy.deepcopy(self.newBoardState)