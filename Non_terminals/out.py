from Non_terminals.idlist import Idlist

class Out:

	def __init__(self, tokenizer, dataFile):
		self.tokenizer = tokenizer
		self.dataFile = dataFile
		self.idlist = None
		
	def parseOut(self):
		if self.tokenizer.getToken() == 11:
			self.tokenizer.skipToken()
			self.idlist = Idlist(self.tokenizer, self.dataFile)
			self.idlist.parseIdlist()

			if self.tokenizer.getToken() == 12:
				self.tokenizer.skipToken()
			else:
				raise Exception("Invalid Syntax! Expected \";\"")
		else:
			raise Exception("Invalid Syntax! Expected \"write\"")
		
	def printOut(self, tabLevel):
		print("write ",end="")
		self.idlist.printIdlist(tabLevel)
		print(";")
		

	def execOut(self):
		self.idlist.writeIDList()

__all__ = ["Out"]