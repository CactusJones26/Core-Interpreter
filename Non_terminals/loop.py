from Non_terminals.cond import Cond
from Non_terminals.stmtseq import Stmtseq

class Loop:

	def __init__(self, tokenizer, dataFile):
		self.tokenizer = tokenizer
		self.dataFile = dataFile
		self.cond = None
		self.stmtseq = None
		
	def parseLoop(self):
		if self.tokenizer.getToken() == 8:
			self.tokenizer.skipToken()
			self.cond = Cond(self.tokenizer, self.dataFile)
			self.cond.parseCond()
			if self.tokenizer.getToken() == 9:
				self.tokenizer.skipToken()
				self.stmtseq = Stmtseq(self.tokenizer, self.dataFile)
				self.stmtseq.parseStmtseq()
				if self.tokenizer.getToken() == 3:
					self.tokenizer.skipToken()
					if self.tokenizer.getToken() == 12:
						self.tokenizer.skipToken()
					else:
						raise Exception("Invalid Syntax! Expected \";\"")
				else:
					raise Exception("Invalid Syntax! Expected \"end\"")
			else:
				raise Exception("Invalid Syntax! Expected \"loop\"")
		else:
			raise Exception("Invalid Syntax! Expected \"while\"")

	def printLoop(self, tabLevel):
		print("while ",end="")
		self.cond.printCond(tabLevel)
		print("loop")
		self.stmtseq.printStmtseq(tabLevel+1)
		for i in range(tabLevel):
			print("\t", end="")
		print("end;")

	def execLoop(self):
		while self.cond.execCond():
			self.stmtseq.execStmtseq()

__all__ = ["Loop"]