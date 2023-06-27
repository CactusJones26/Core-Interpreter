from Non_terminals.decl import Decl

class Declseq:

	def __init__(self, tokenizer, dataFile):
		self.tokenizer = tokenizer
		self.dataFile = dataFile
		self.decl = None
		self.declSeq = None
		self.alt = 1

	def parseDeclseq(self):
		self.decl = Decl(self.tokenizer, self.dataFile)
		self.decl.parseDecl()

		if self.tokenizer.getToken() == 4:
			self.alt = 2
			self.declSeq = Declseq(self.tokenizer, self.dataFile)
			self.declSeq.parseDeclseq()


	def printDeclseq(self, tabLevel):
		self.decl.printDecl(tabLevel+1)
		if self.alt == 2:
			self.declSeq.printDeclseq(tabLevel)
			

	def execDeclseq(self):
		pass

__all__ = ["Declseq"]