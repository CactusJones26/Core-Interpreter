# from Non_terminals.stmt import Stmt

class Stmtseq:

	def __init__(self, tokenizer, dataFile):
		self.tokenizer = tokenizer
		self.dataFile = dataFile
		self.stmt = None
		self.stmtseq = None
		self.alt = 0
		
	def parseStmtseq(self):
		self.alt = 1
		from Non_terminals.stmt import Stmt
		self.stmt = Stmt(self.tokenizer, self.dataFile)
		self.stmt.parseStmt()

		if self.tokenizer.getToken() in [32, 5, 8, 10, 11]:
			self.alt = 2
			self.stmtseq = Stmtseq(self.tokenizer, self.dataFile)
			self.stmtseq.parseStmtseq()

	def printStmtseq(self, tabLevel):
		for i in range(tabLevel):
			print("\t", end="")
		self.stmt.printStmt(tabLevel)
		if self.alt == 2:
			self.stmtseq.printStmtseq(tabLevel)

	def execStmtseq(self):
		self.stmt.execStmt()
		if self.alt == 2:
			self.stmtseq.execStmtseq()

__all__ = ["Stmtseq"]