from Non_terminals.fac import Fac

class Exp:

	def __init__(self, tokenizer, dataFile):
		self.tokenizer = tokenizer
		self.dataFile = dataFile
		self.fac = None
		self.exp = None
		self.alt = 1
		
	def parseExp(self):
		self.fac = Fac(self.tokenizer, self.dataFile)
		self.fac.parseFac()

		# self.tokenizer.skipToken() # !!!!
		#print(self.tokenizer.getToken())
		if self.tokenizer.getToken() == 22 or self.tokenizer.getToken() == 23:
			if self.tokenizer.getToken() == 22:
				self.alt = 2
				self.tokenizer.skipToken()
				self.exp = Exp(self.tokenizer, self.dataFile)
				self.exp.parseExp()
			elif self.tokenizer.getToken() == 23:
				self.alt = 3
				self.tokenizer.skipToken()
				self.exp = Exp(self.tokenizer, self.dataFile)
				self.exp.parseExp()
			else:
				#what if it's the first alternative?
				raise Exception("Invalid syntax! Expected \"+\", \"-\", or just a fac")
		#print(self.tokenizer.getToken())
	def printExp(self, tabLevel):
		self.fac.printFac(tabLevel)
		if self.alt == 2:
			print(" + ", end="")
			self.exp.printExp(tabLevel)
		elif self.alt == 3:
			print(" - ", end="")
			self.exp.printExp(tabLevel)

	def execExp(self):
		num = self.fac.execFac()
		if self.alt == 2:
			num += self.exp.execExp()
		elif self.alt == 3:
			num -= self.exp.execExp()
		return num

__all__ = ["Exp"]