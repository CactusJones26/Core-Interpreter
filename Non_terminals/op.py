from Non_terminals.int import Int
from Non_terminals.id import Id
# from Non_terminals.exp import Exp

class Op:

	def __init__(self, tokenizer, dataFile):
		self.tokenizer = tokenizer
		self.dataFile = dataFile
		self.int = None
		self.id = None
		self.exp = None
		self.alt = 0
		
	def parseOp(self):
		if self.tokenizer.getToken() == 31:
			self.alt = 1
			self.int = Int(self.tokenizer, self.dataFile)
			self.int.parseInt()
		elif self.tokenizer.getToken() == 32:
			self.alt = 2
			self.id = Id(self.tokenizer, self.dataFile)
			self.id.parseId()
		elif self.tokenizer.getToken() == 20:
			self.alt = 3
			self.tokenizer.skipToken()
			from Non_terminals.exp import Exp
			self.exp = Exp(self.tokenizer, self.dataFile)
			self.exp.parseExp()
			if self.tokenizer.getToken() == 21:
				self.tokenizer.skipToken()
			else:
				raise Exception("Invalid syntax! Expected \")\"")
		else:
			print(self.tokenizer.getToken())
			raise Exception("Invalid Syntax! Expected an indentifier, interger, or paranthesized expression")
			


	def printOp(self, tabLevel):
		match self.alt:
			case 1:
				self.int.printInt(tabLevel)
			case 2:
				self.id.printId(tabLevel)
			case 3:
				print("(",end="")
				self.exp.printExp(tabLevel)
				print(")",end="")
		

	def execOp(self):
		result = 0
		match self.alt:
			case 1:
				result = self.int.execInt()
			case 2:
				result = self.id.idDict[self.id.id]
			case 3:
				result = self.exp.execExp()
		return result


__all__ = ["Op"]