from sys import *
tokens=[]
def Open_File(fileName):
	data = open(fileName,"r").read()
	return data
def lex(filecontents):
	tok=""
	state =0
	string =""
	filecontents= list(filecontents)
	for char in filecontents:
		tok+=char
		if tok==" ":
			if state == 0:

				tok =""
			else :
				tok = " "
		elif tok == "\n":
			tok=""	
		elif tok =="inra":
			tokens.append("INRA")
			tok=""
		elif tok == "\"":
			if state ==0:
				state=1
			elif state==1:
				tokens.append("STRING:"+string+"\"")
				string =""
				state=0
				tok=""
		elif state ==1:
			string +=tok
			tok=""			
	return tokens		
			
def parse(toks):
	print toks
def run():
	data=Open_File(argv[1])
	toks=lex (data)
	parse(toks)
run()	