import json

class GameInitializer():

	def loadInitParametersGame(self, initialParametersJSONFile):
		with open(initialParametersJSONFile, 'r') as parametersFile:
			initialParameters = json.load(parametersFile)

		return initialParameters