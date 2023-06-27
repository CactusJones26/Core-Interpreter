class Int:

	def __init__(self, tokenizer, dataFile):
		self.tokenizer = tokenizer
		self.dataFile = dataFile
		self.int = None
		
	def parseInt(self):
		self.int = self.tokenizer.intVal()
		self.tokenizer.skipToken()

	def printInt(self, tabLevel):
		print(self.int, end="")

	def execInt(self):
		return int(self.int)

__all__ = ["Int"]