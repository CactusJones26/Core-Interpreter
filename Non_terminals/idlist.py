from Non_terminals.id import Id

class Idlist:

	def __init__(self, tokenizer, dataFile):
		self.tokenizer = tokenizer
		self.dataFile = dataFile
		self.id = None
		self.idlist = None
		self.alt = 0

	def parseIdlist(self):
		self.alt = 1
		self.id = Id(self.tokenizer, self.dataFile)
		#print(self.tokenizer.getToken())

		self.id.parseId()
		#print(self.tokenizer.getToken())

		if self.tokenizer.getToken() == 13:
			self.alt = 2
			self.tokenizer.skipToken()
			self.idlist = Idlist(self.tokenizer, self.dataFile)
			self.idlist.parseIdlist()

	def printIdlist(self, tabLevel):
		# if self.alt == 1:
		# 	print(f"{self.id.printId()}")
		# else:
		# 	print(f"{self.id.printId()}, {self.printIdlist()}")
		self.id.printId(tabLevel)
		if self.alt == 2:
			print(", ", end="")
			self.idlist.printIdlist(tabLevel)

	def execIdlist(self):
		self.id.execId()
		if self.alt == 2:
			self.idlist.execIdlist()

	def writeIDList(self):
		self.id.writeId()
		if self.alt == 2:
			self.idlist.writeIDList()

__all__ = ["Idlist"]