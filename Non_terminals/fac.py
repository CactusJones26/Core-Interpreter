from Non_terminals.op import Op

class Fac:

	def __init__(self, tokenizer, dataFile):
		self.tokenizer = tokenizer
		self.dataFile = dataFile
		self.op = None
		self.fac = None
		self.alt = 0
		
	def parseFac(self):
		# print(self.tokenizer.getToken())
		self.alt = 1
		self.op = Op(self.tokenizer, self.dataFile)
		self.op.parseOp()
		#print(self.tokenizer.getToken())
		if self.tokenizer.getToken() == 24:
			self.tokenizer.skipToken()
			self.alt = 2
			self.fac = Fac(self.tokenizer, self.dataFile)
			self.fac.parseFac()

	def printFac(self, tabLevel):
		if self.alt == 1:
			self.op.printOp(tabLevel)
		elif self.alt == 2:
			self.op.printOp(tabLevel)
			print(" * ", end="")
			self.fac.printFac(tabLevel)

	def execFac(self):
		num = self.op.execOp()
		if self.alt == 2:
			num *= self.fac.execFac()
		return num

__all__ = ["Fac"]