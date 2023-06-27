from Non_terminals.assign import Assign
from Non_terminals.IF import If
from Non_terminals.loop import Loop
from Non_terminals.IN import In
from Non_terminals.out import Out

class Stmt:

	def __init__(self, tokenizer, dataFile):
		self.tokenizer = tokenizer
		self.dataFile = dataFile
		self.alt = 0
		self.assign = None
		self.IF = None
		self.loop = None
		self.IN = None
		self.out = None
		
	def parseStmt(self):
		match self.tokenizer.getToken():
			case 32:
				self.alt = 1
				self.assign = Assign(self.tokenizer, self.dataFile)
				self.assign.parseAssign()
			case 5:
				self.alt = 2
				self.IF = If(self.tokenizer, self.dataFile)
				self.IF.parseIf()
			case 8:
				self.alt = 3
				self.loop = Loop(self.tokenizer, self.dataFile)
				self.loop.parseLoop()
			case 10:
				self.alt = 4
				self.IN = In(self.tokenizer, self.dataFile)
				self.IN.parseIn()
			case 11:
				self.alt = 5
				self.out = Out(self.tokenizer, self.dataFile)
				self.out.parseOut()
			case default:
				raise Exception("Invalid Syntax! Expected a valid Stmt")


	def printStmt(self, tabLevel):
		match self.alt:
			case 1:
				self.assign.printAssign(tabLevel)
			case 2:
				self.IF.printIf(tabLevel)
			case 3:
				self.loop.printLoop(tabLevel)
			case 4:
				self.IN.printIn(tabLevel)
			case 5:
				self.out.printOut(tabLevel)

	def execStmt(self):
		match self.alt:
			case 1:
				self.assign.execAssign()
			case 2:
				self.IF.execIf()
			case 3:
				self.loop.execLoop()
			case 4:
				self.IN.execIn()
			case 5:
				self.out.execOut()

__all__ = ["Stmt"]