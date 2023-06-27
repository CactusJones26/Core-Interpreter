from Non_terminals.id import Id
from Non_terminals.exp import Exp

class Assign:

	def __init__(self, tokenizer, dataFile):
		self.tokenizer = tokenizer
		self.dataFile = dataFile
		self.id = None
		self.exp = None
		
	def parseAssign(self):
		self.id  = Id(self.tokenizer, self.dataFile)
		self.id.parseId()
		if self.tokenizer.getToken() == 14:
			self.tokenizer.skipToken()
			self.exp = Exp(self.tokenizer, self.dataFile)
			self.exp.parseExp()
			#print(self.tokenizer.getToken())
			if self.tokenizer.getToken() == 12:
				self.tokenizer.skipToken()
			else:
				raise Exception("Invalid Syntax! Expected \";\"")
		else:
				raise Exception("Invalid Syntax! Expected \"=\"")

	def printAssign(self, tabLevel):
		# for i in range(tabLevel):
		# 	print("\t", end="")
		self.id.printId(tabLevel)
		print(" = ", end="")
		self.exp.printExp(tabLevel)
		print(";")

	def execAssign(self):
		val = self.exp.execExp()
		self.id.idDict[self.id.id] = val

__all__ = ["Assign"]