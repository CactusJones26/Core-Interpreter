from Non_terminals.idlist import Idlist

class Decl:

	def __init__(self, tokenizer, dataFile):
		self.tokenizer = tokenizer
		self.dataFile = dataFile
		self.idList = None
		
	def parseDecl(self):
		if self.tokenizer.getToken() == 4:
			#print(self.tokenizer.getToken())
			self.tokenizer.skipToken()
			#print(self.tokenizer.getToken())

			self.idList = Idlist(self.tokenizer, self.dataFile)
			self.idList.parseIdlist()
			#print(self.tokenizer.getToken())

			if self.tokenizer.getToken() == 12:
				self.tokenizer.skipToken()
			else:
				raise Exception("Invalid syntax! Expected \";\"")

		else:
			raise Exception("Invalid syntax! Expected \"Int\"")



	def printDecl(self, tabLevel):
		for i in range(tabLevel):
			print("\t", end="")
		print("int ", end="")
		self.idList.printIdlist(tabLevel)
		print(";")

	def execDecl(self):
		pass

__all__ = ["Decl"]