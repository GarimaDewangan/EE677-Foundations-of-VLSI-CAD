Name : Garima Dewangan
Roll no. : 19D070023

Description of files

simulator.py
It is the code for logic simulation
It asks for two inputs : 
	1) Netlist file name
	2) Input file name
Print the output on the console as well as in a text file 'output.txt'
If the no. of inputs in input text file do not match with no. of inputs wriitten in netlist file the the code raises an error and stops

Netlist.txt
'*' symbol is for comments. Line starting with '*' are ignored. Comments must be written on seperate lines.
empty lines are ignored
1st line is the inputs list with space between two inputs
2nd line is the list of outputs with space between two outputs
From the 3rd line the gates are described
format of describing gate : output gate inputs
variable names are cases sensitive
variable names can be anything like character, string, numbers etc except '*' which is used for comments
Gate names are not case senstive
Can contain any no. of inputs and outputs.

input.txt 
contains the values for input variables
Must be entered with space in between
Can contain any no. of inputs
Inputs can be '0', '1', 'x'


