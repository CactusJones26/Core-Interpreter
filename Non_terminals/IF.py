from Non_terminals.cond import Cond
from Non_terminals.stmtseq import Stmtseq

class If:

	def __init__(self, tokenizer, dataFile):
		self.tokenizer = tokenizer
		self.dataFile = dataFile
		self.cond = None
		self.SS1 = None
		self.SS2 = None
		self.alt = 0
		
	def parseIf(self):
		if self.tokenizer.getToken() == 5:
			self.alt = 1
			self.tokenizer.skipToken()
			self.cond = Cond(self.tokenizer, self.dataFile)
			self.cond.parseCond()
			if self.tokenizer.getToken() == 6:
				self.tokenizer.skipToken()
				self.SS1 = Stmtseq(self.tokenizer, self.dataFile)
				self.SS1.parseStmtseq()
				if self.tokenizer.getToken() == 3:
					self.tokenizer.skipToken()
					self.tokenizer.skipToken()
				elif self.tokenizer.getToken() == 7:
					self.alt = 2
					self.tokenizer.skipToken()
					self.SS2 = Stmtseq(self.tokenizer, self.dataFile)
					self.SS2.parseStmtseq()
					if self.tokenizer.getToken() == 3:
						self.tokenizer.skipToken()
						if self.tokenizer.getToken() == 12:
							self.tokenizer.skipToken()
						else:
							raise Exception("Invalid syntax! Expected \";\"")
					else:
						raise Exception("Invalid synatx! Expected \"end\"")
				else:
					raise Exception("Invalid Syntax! Expected \"else\" or \"end\"")
		else:
			raise Exception("Invalid Syntax! Expected \"If\"")

	def printIf(self, tabLevel):
		if self.alt == 1:
			print("if ",end="")
			self.cond.printCond(tabLevel)
			print(" then")
			self.SS1.printStmtseq(tabLevel+1)
			for i in range(tabLevel):
				print("\t", end="")
			print("end;")
		else:
			print("if ",end="")
			self.cond.printCond(tabLevel)
			print("then")
			self.SS1.printStmtseq(tabLevel+1)
			for i in range(tabLevel):
				print("\t", end="")
			print("else")
			self.SS2.printStmtseq(tabLevel+1)
			for i in range(tabLevel):
				print("\t", end="")
			print("end;")


	def execIf(self):
		c = self.cond.execCond()
		if c:
			self.SS1.execStmtseq()
		elif self.alt == 2:
			self.SS2.execStmtseq()

__all__ = ["If"]