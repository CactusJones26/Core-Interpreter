import sys

class Tokenizer:
    
    def __init__(self, file):
        self.Tokenizer = open(file, "r")
        self.tokens = list()
        self.string = list()
        self.tokenizeLine()
        self.pointer = 0
        
    def createString(self, c):
        previous = self.tokens.pop()
        if type(previous) == int:
            self.tokens.append(previous)
            self.tokens.append(c)
        elif not previous[0].isdigit() and not previous[0].isalpha():
            self.tokenizeString(previous)
            self.tokens.append(c)
        else:
            new = previous + c
            self.tokens.append(new)
        
        
    def tokenizeString(self, previous):
        #evalutes RW, Identifiers, and Integers
        if type(previous) != int:
            
            if previous.isnumeric():
                self.tokens.append(31)
            elif previous[0].isalpha() and previous[0].isupper():
                # print(previous)
                if previous == "END OF FILE":
                    self.tokens.append(33)
                else:
                    validId = True
                    for c in previous:
                        if validId and not c.isdigit() and not (c.isalpha() and c.isupper()):
                            validId = False
                            self.tokens.append(34)
                    if validId:
                        self.tokens.append(32)

            elif previous[0].isalpha() and previous[0].islower():
                validRW = True
                for c in previous:
                    if validRW and (c.isdigit() or (c.isalpha() and c.isupper())):
                        validRW = False
                        self.tokens.append(34)
                if validRW:
                    match previous:
                        case "program":
                            self.tokens.append(1)
                        case "begin":
                            self.tokens.append(2)
                        case "end":
                            self.tokens.append(3)
                        case "int":
                            self.tokens.append(4)
                        case "if":
                            self.tokens.append(5)
                        case "then":
                            self.tokens.append(6)
                        case "else":
                            self.tokens.append(7)
                        case "while":
                            self.tokens.append(8)
                        case "loop":
                            self.tokens.append(9)
                        case "read":
                            self.tokens.append(10)
                        case "write":
                            self.tokens.append(11)
                        case default:
                            self.tokens.append(34)
            else:
                match previous:
                    case ';':
                        self.tokens.append(12)
                    case ',':
                        self.tokens.append(13)
                    case '=':
                        self.tokens.append(14)
                    case '!':
                        self.tokens.append(15)
                    case '[':
                        self.tokens.append(16)
                    case ']':
                        self.tokens.append(17)
                    case '&&':
                        self.tokens.append(18)
                    case '||':
                        self.tokens.append(19)
                    case '(':
                        self.tokens.append(20)
                    case ')':
                        self.tokens.append(21)
                    case '+':
                        self.tokens.append(22)
                    case '-':
                        self.tokens.append(23)
                    case '*':
                        self.tokens.append(24)
                    case '!=':
                        self.tokens.append(25)
                    case '==':
                        self.tokens.append(26)
                    case '<':
                        self.tokens.append(27)
                    case '>':
                        self.tokens.append(28)
                    case '<=':
                        self.tokens.append(29)
                    case '>=':
                        self.tokens.append(30)
                    case default:    
                        self.tokens.append(34)                                               
                        
            self.string.append(previous)            

            
    def tokenizeLine(self):
        line = self.Tokenizer.readline()
        blank = True
        end = False
        lineCounter = 0
        
        while blank and not end:
            for c in line:
                if blank and (c != ' ' and c != '\n'):
                    blank = False

                if len(line) == lineCounter and c != '\n':
                    end = True
                    self.tokenizeString("END OF FILE")
                    
                lineCounter += 1

            if not end and len(line) == 0:
                end = True
                self.tokenizeString("END OF FILE")
            if blank and not end:
                line = self.Tokenizer.readline()
                lineCounter = 0
        
        lineCounter = 0
        for c in line:    
            if lineCounter == 0 or len(self.tokens) == 0:
                if c != ' ':
                    self.tokens.append(c)
                lineCounter += 1
            else:   
                if c in ";,+-*![]()<>":
                    previous = self.tokens.pop()
                    if type(previous) == int:  
                        self.tokens.append(previous)
                    else:
                        self.tokenizeString(previous)                        
                    self.tokens.append(c)
                    
                elif c == '&':
                    previous = self.tokens.pop()
                    if previous == '&':
                        new = previous + '&'
                        self.tokenizeString(new)
                    else:
                        if type(previous) == int:  
                            self.tokens.append(previous)
                        else:
                            self.tokenizeString(previous)
                        self.tokens.append('&')
                        
                elif c == '|':
                    previous = self.tokens.pop()
                    if previous == '|':
                        new = previous + '|'
                        self.tokenizeString(new)
                    else:
                        if type(previous) == int:  
                            self.tokens.append(previous)
                        else:
                            self.tokenizeString(previous)
                        self.tokens.append('|')

                elif c == '=':
                    previous = self.tokens.pop()
                    if previous == '!' or previous == '>' or previous == '<' or previous == '=':
                        new = previous + '='
                        self.tokenizeString(new)
                    else:
                        if type(previous) == int:  
                            self.tokens.append(previous)
                        else:
                            self.tokenizeString(previous)         
                        self.tokens.append('=')

                elif c.isdigit() or c.isalpha():
                    self.createString(c)
                elif c == ' ' or c == '\n':
                    previous = self.tokens.pop()
                    if type(previous) == int:  
                        self.tokens.append(previous)
                    else:
                        self.tokenizeString(previous)
                        
                else:
                    previous = self.tokens.pop()
                    if type(previous) == int:  
                        self.tokens.append(previous)
                    else:
                        self.tokenizeString(previous)                        

                    self.tokenizeString(c)

                lineCounter += 1
                if len(line) == lineCounter and c != '\n':
                    previous = self.tokens.pop()
                    if type(previous) == int:
                        self.tokens.append(previous)
                    else:
                        self.tokenizeString(previous)

                    self.tokenizeString("END OF FILE")
                   

    def getToken(self):
        return self.tokens[self.pointer]
        
    def skipToken(self):
        if self.getToken() != 33 and self.getToken() != 34:
            if (self.pointer == len(self.tokens) - 1):
                self.tokenizeLine()
            self.pointer += 1
            
    def intVal(self):
        currentToken = self.getToken()
        if currentToken != 31:
            print("\nError: Invalid token!\nToken: ", self.string[self.pointer])
            quit()
        else:
            return int(self.string[self.pointer])
       
        
    def idName(self):
        currentToken = self.getToken()
        if currentToken != 32:
            print("\nError: Invalid token!\nToken: ", self.string[self.pointer])
            quit()
        else:
            return self.string[self.pointer]                        
                  
__all__ = ["Tokenizer"]