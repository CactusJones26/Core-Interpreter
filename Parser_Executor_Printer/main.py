import sys
from Scanner import Tokenizer
from Non_terminals.prog import Prog

coreFileName = sys.argv[1]
dataFileName = sys.argv[2]

TK = Tokenizer(coreFileName)
dataFile = open(dataFileName, 'r')

Program = Prog(TK, dataFile)
Program.parseProg()
Program.printProg()
Program.execProg()

# i = Op(TK, dataFile)
# #print(TK.tokens)
# i.parseOp()
# i.printOp()



dataFile.close()


