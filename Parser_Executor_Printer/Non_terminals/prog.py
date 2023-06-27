from Non_terminals.declseq import Declseq
from Non_terminals.stmtseq import Stmtseq
from Non_terminals.id import Id

class Prog:

	def __init__(self, tokenizer, dataFile):
		self.tokenizer = tokenizer
		self.dataFile = dataFile
		self.ds = None
		self.ss = None

	def parseProg(self):
		if self.tokenizer.getToken() == 1:
			self.tokenizer.skipToken()
			self.ds = Declseq(self.tokenizer, self.dataFile)

			Id.mode = True

			self.ds.parseDeclseq()
			#self.tokenizer.skipToken() # !!!!!!!
			#print(self.tokenizer.getToken())
			if self.tokenizer.getToken() == 2:
				self.tokenizer.skipToken()
				self.ss = Stmtseq(self.tokenizer, self.dataFile)

				Id.mode = False

				self.ss.parseStmtseq()
				self.tokenizer.skipToken()
				if self.tokenizer.getToken() == 3:
					self.tokenizer.skipToken()
					if self.tokenizer.getToken() == 33:
						#End of Core program
						quit()
					else:
						raise Exception("Invalid syntax! Expected EOF")
			else:
				raise Exception("Invalid syntax! Expected \"begin\"")

		else:
			raise Exception("Invalid syntax! Expected \"prog\"")
		

	def printProg(self):
		tabLevel = 0
		print("\nprogram")
		self.ds.printDeclseq(tabLevel)
		print("begin")
		self.ss.printStmtseq(tabLevel+1)
		print("end\n")



		# print(
		# 	f"program \n\t {self.ds.printDeclseq()} begin \n\t {self.ss.printStmtseq()} \n end"
		# )

	def execProg(self):
		# self.ds.execDeclseq()
		self.ss.execStmtseq()

__all__ = ["Prog"]