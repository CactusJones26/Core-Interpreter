from Non_terminals.comp import Comp
# from Non_terminals.cond import Cond

class Cond:

	def __init__(self, tokenizer, dataFile):
		self.tokenizer = tokenizer
		self.dataFile = dataFile
		self.comp = None
		self.cond1 = None
		self.cond2 = None
		self.alt = 0
		
	def parseCond(self):
		if not self.tokenizer.getToken() in [15, 16]:
			self.alt = 1
			self.comp = Comp(self.tokenizer, self.dataFile)
			self.comp.parseComp()
		else:
			if self.tokenizer.getToken() == 15:
				self.alt = 2
				self.tokenizer.skipToken()
				from Non_terminals.cond import Cond
				self.cond1 = Cond(self.tokenizer, self.dataFile)
				self.cond1.parseCond()
			elif self.tokenizer.getToken() == 16:
				self.tokenizer.skipToken()
				from Non_terminals.cond import Cond
				self.cond1 = Cond(self.tokenizer, self.dataFile)
				self.cond1.parseCond()
				if self.tokenizer.getToken() == 18:
					self.alt = 3
					self.tokenizer.skipToken()
					from Non_terminals.cond import Cond
					self.cond2 = Cond(self.tokenizer, self.dataFile)
					self.cond2.parseCond()
				elif self.tokenizer.getToken() == 19:
					self.alt = 4
					self.tokenizer.skipToken()
					from Non_terminals.cond import Cond
					self.cond2 = Cond(self.tokenizer, self.dataFile)
					self.cond2.parseCond()
				else:
					raise Exception("Invalid Syntax! Expected \"&&\" or \"||\"")
			else:
				raise Exception("Invalid Syntax! Expected \"!\" or \"[\"")

			if self.alt in [3, 4] and self.tokenizer.getToken() == 17:
				self.tokenizer.skipToken()

	def printCond(self, tabLevel):
		match self.alt:
			case 1:
				self.comp.printComp(tabLevel)
			case 2:
				print("!", end="")
				self.cond1.printCond(tabLevel)
			case 3:
				print("[",end="")
				self.cond1.printCond(tabLevel)
				print(" && ",end="")
				self.cond2.printCond(tabLevel)
				print("]")
			case 4:
				print("[",end="")
				self.cond1.printCond(tabLevel)
				print(" || ",end="")
				self.cond2.printCond(tabLevel)
				print("]", end="")

	def execCond(self):
		c = False
		match self.alt:
			case 1:
				c = self.comp.execComp()
			case 2:
				c = not self.cond1.execCond()
			case 3:
				c1 = self.cond1.execCond()
				c2 = self.cond2.execCond()
				c = c1 and c2
			case 4:
				c1 = self.cond1.execCond()
				c2 = self.cond2.execCond()
				c = c1 or c2
		return c

__all__ = ["Cond"]