class Compop:

	def __init__(self, tokenizer, dataFile):
		self.tokenizer = tokenizer
		self.dataFile = dataFile
		self.alt = 0
		self.sign = ""
		
	def parseCompop(self):
		match self.tokenizer.getToken():
			case 25:
				self.alt = 1
				self.sign = "!="
			case 26:
				self.alt = 2
				self.sign = "=="
			case 27:
				self.alt = 3
				self.sign = "<"
			case 28:
				self.alt = 4
				self.sign = ">"
			case 29:
				self.alt = 5
				self.sign = "<="
			case 30:
				self.alt = 6
				self.sign = ">="
			case default:
				raise Exception("Invalid syntax! Expected a CompOp")
		#skip token?
		self.tokenizer.skipToken()

				

	def printCompop(self, tabLevel):
		print(" ",end="")
		print(self.sign,end="")
		print(" ",end="")

	def execCompop(self, op1, op2):
		match self.alt:
			case 1:
				return op1 != op2
			case 2:
				return op1 == op2
			case 3:
				return op1 < op2
			case 4:
				return op1 > op2
			case 5:
				return op1 <= op2
			case 6:
				return op1 >= op2

__all__ = ["Compop"]