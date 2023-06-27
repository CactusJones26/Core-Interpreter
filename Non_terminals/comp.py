from Non_terminals.op import Op
from Non_terminals.compop import Compop

class Comp:

	def __init__(self, tokenizer, dataFile):
		self.tokenizer = tokenizer
		self.dataFile = dataFile
		self.op1 = None
		self.op2 = None
		self.compop = None
		
	def parseComp(self):
		if self.tokenizer.getToken() == 20:
			self.tokenizer.skipToken()
			self.op1 = Op(self.tokenizer, self.dataFile)
			self.op1.parseOp()

			self.compop = Compop(self.tokenizer, self.dataFile)
			self.compop.parseCompop()

			self.op2 = Op(self.tokenizer, self.dataFile)
			self.op2.parseOp()
			if self.tokenizer.getToken() == 21:
				self.tokenizer.skipToken()
			else:
				raise Exception("Invalid Syntax! Expected \")\"")
		else:
			raise Exception("Invalid Syntax! Expected \"(\"")

	def printComp(self, tabLevel):
		print("(", end="")
		self.op1.printOp(tabLevel)
		self.compop.printCompop(tabLevel)
		self.op2.printOp(tabLevel)
		print(") ",end="")

	def execComp(self):
		op1 = self.op1.execOp()
		op2 = self.op2.execOp()
		cp = self.compop.execCompop(op1, op2)
		return cp

__all__ = ["Comp"]