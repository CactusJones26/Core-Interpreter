class Id:
	# ParseId1 and ParseId2???
	mode = False
	idDict = {}

	def __init__(self, tokenizer, dataFile):
		self.tokenizer = tokenizer
		self.dataFile = dataFile
		#self.idDict = {}
		self.id = None
		
	def parseId1(self):
		#print(not self.tokenizer.idName() in self.idDict)
		if not self.tokenizer.idName() in self.idDict:
			self.idDict[self.tokenizer.idName()] = None
			self.id = self.tokenizer.idName()
			#print(self.idDict)
		else:
			raise Exception(f"Invalid Syntax! Double declaration of variable: {self.tokenizer.idName()}")
		self.tokenizer.skipToken()
		#print(self.tokenizer.getToken())


	def parseId2(self):
		#print(self.idDict)
		if not self.tokenizer.idName() in self.idDict:
			raise Exception(f"Undeclared variable: {self.tokenizer.idName()}")
		else:
			self.id = self.tokenizer.idName()
		self.tokenizer.skipToken()
		#print(self.tokenizer.getToken())

		
	def parseId(self):
		#print(self.tokenizer.getToken())
		if self.mode:
			self.parseId1()
		else:
			self.parseId2()


	def printId(self, tabLevel):
		print(self.id, end="") # !!!!!!!

	def execId(self):
		data = self.dataFile.readline()
		if data == "":
			raise Exception("End of data file reached! Not enough data!")
		self.idDict[self.id] = int(data)

	def writeId(self):
		print(self.id, end="")
		print(" = ", end="")
		print(self.idDict[self.id])

__all__ = ["Id"]