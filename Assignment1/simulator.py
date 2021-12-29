import sys

#Gate definitions
def AND(a):
	if '0' in a:
		return('0')
	elif 'x' in a:
		return('x')
	else:
		return('1')

def OR(a):
	if '1' in a:
		return('1')
	elif 'x' in a:
		return('x')
	else:
		return('0')

def NOT(a):
	if(a[0]=='1'):
		return('0')
	elif(a[0]=='0'):
		return('1')
	else:
		return('x')

def XOR(a):
	if 'x' in a:
		return('x')
	elif(a.count('1')%2==0 or a.count('0')%2==0):
		return('0')
	else:
		return('1')

def NOR(a):
	return(NOT(OR(a)))

def NAND(a):
	return(NOT(AND(a)))

#Node of the graph
class node:
	def __init__(self,type,inp):
		self.type = type
		self.inp = inp

#Evaluates output
def evaluate(x):
	#print(x.type,x.inp)
	inps = []
	for i in x.inp:
		if(variable[i]=='x'):
			variable[i] = evaluate(graph[i])
			#print(i,variable[i])
		inps.append(variable[i])
	if x.type == 'and':
		return(AND(inps))
	elif x.type == 'or':
		return(OR(inps))
	elif x.type == 'not':
		return(NOT(inps))
	elif x.type == 'xor':
		return(XOR(inps))
	elif x.type == 'nor':
		return(NOR(inps))
	elif x.type == 'nand':
		return(NAND(inps))
	else:
		return('x')

#Opening netlist file
st = input("Netlist file : ")
f1 = open(st, "r")

#Declaring dictionaries to store variable values and nodes of graph
variable = {}
graph = {}

#Opening input file
inp = input('Input file : ')
f2 = open(inp,"r")
values = (f2.read()).split()
li = len(values)

t =0
for x in f1:
	x = x.strip()
	if len(x)==0 or x[0]=='*' :
		continue
	elif t==0:
		inputs = x.split()
		if(len(inputs)!=li):
			print('***Error: No. of inputs do not match as in netlist***')
			sys.exit(1)
		for i in range(len(inputs)):
			variable[inputs[i]] = values[i]
		#print(variable)
		t=t+1
	elif t==1:
		outputs = x.split()
		t = t+1
	else:
		code = x.split()
		variable[code[0]] = 'x'
		#print(code[0],code[1],code[2:])
		x = node(str(code[1].lower()),code[2:])
		graph[code[0]] = x
		#print(x.type)

ans = ""

for i in outputs :
	if variable[i] =='x':
		variable[i] = evaluate(graph[i])
	ans = ans + str(variable[i]) + ' '

print(ans)
#print(variable)

#Opening output file
f3 = open("output.txt", "w")
 
#write string to file
f3.write(ans)
 
#closing files file
f1.close()
f2.close()
f3.close()


