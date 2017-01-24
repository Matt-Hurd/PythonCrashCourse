'''
Some notes:
	Anything within triple apostrophes, or following a '#' is a comment. This won't be ran.
	Python relies on tabulation to determine code flow.
		If a line is tabbed and the previous isn't, then it is typically reliant on the previous line.
		Other languages handle it with brackets, such as
			if (x == y) {
				print("X is equal to Y");
			}
		In python, you don't use brackets, but it can be easier to think with them.
	When a python file is opened (via the python command, or from another python file), it automatically runs anything that is not indented.
		Lines beginning with 'def' are functions, so they are only ran if explicitly called.
		Lines beginning with 'import' are using other files or modules.
'''

def foo(): #This is a function. It does things
	bar = "Hello" #This is a varible. This one holds a string.
	fizz = 1 #This is also a varible. This one holds an integer.
	buzz = None #This is another variable. This one doesn't have anything in it yet.
	if bar == "Hello": #This is a conditional statement. If the statement is true, continue to the indented code. Otherwise, jump past it.
		print("Bar is equal to \"Hello\"")
	else: #If the conditional is false, we run the else. The else statement is optional
		print("Bar is not equal to \"Hello\"") #The '\' character here says that the quotations are part of the string, as opposed to closing it.

print("Running example00.py") #This will always print when you run the file
if __name__ == '__main__': #This checks to make sure that you ran "python example00.py", as opposed to always running it. It's not too important right now.
	foo() #Calls the foo function		