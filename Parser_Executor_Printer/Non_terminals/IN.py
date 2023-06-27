from Non_terminals.idlist import Idlist

class In:

	def __init__(self, tokenizer, dataFile):
		self.tokenizer = tokenizer
		self.dataFile = dataFile
		self.idlist = None
		
	def parseIn(self):
		if self.tokenizer.getToken() == 10:
			self.tokenizer.skipToken()
			self.idlist = Idlist(self.tokenizer, self.dataFile)
			self.idlist.parseIdlist()

			if self.tokenizer.getToken() == 12:
				self.tokenizer.skipToken()
			else:
				raise Exception("Invalid Syntax! Expected \";\"")
		else:
			raise Exception("Invalid Syntax! Expected \"Read\"")

	def printIn(self, tabLevel):
		print("read ",end="")
		self.idlist.printIdlist(tabLevel)
		print(";")

	def execIn(self):
		self.idlist.execIdlist()

__all__ = ["In"]