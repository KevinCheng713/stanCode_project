"""
File: rocket.py
Name:鄭凱元
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

SIZE = 3


def main():
	"""
	The rocket can be divided into six parts, and each part corresponds to a function.
	"""
	head()
	belt()
	upper()
	lower()
	belt()
	head()



def head():
	"""
	(Suppose that the SIZE = n)
	First, verify the number of rows and columns.
	The number of rows is the same as the value of SIZE we set,
	and the number of columns is at most a combination of n slashes(/) + n backslashes(\)
	+ 2 blank spaces,
	so we set the number of columns equals to (2n+2).

	Look at the diagram of the rocket and its printing rules,
	the slashes or backslashes are printed if the value of (i+j) is greater than or equal to n.
	If j is not greater than n, print / ,
	and if j is greater than n and less than or equal to (n+ i+1), print \ ,
	in other cases, print blank space.
	"""
	for i in range(SIZE):
		for j in range(SIZE*2+2):
			if (i+j) >= SIZE:
				if j <= SIZE:
					print('/', end="")
				elif j > SIZE:
					if j <= SIZE+i+1:
						print('\\', end="")
			else:
				print(' ', end="")
		print('')



def belt():
	"""
	Print "+" at the beginning and the end,
	and print the middle part "==" for n times.
	"""
	print('+', end="")
	for i in range(SIZE):
		print('==', end="")
	print('+', end="")
	print('')



def upper():
	"""
	The number of '.' decreases row by row,
	slashes and backslashes increases row by row.
	"""
	for i in range(SIZE):
		print('|', end="")
		for j in range(SIZE-i-1):
			print('.', end="")
		for k in range(i+1):
			print('/\\', end='')
		for j in range(SIZE-i-1):
			print('.', end="")
		print('|', end="")
		print('')



def lower():
	"""
	As opposed to the previous concept of function upper()：
	The number of '.' increases row by row,
	backslashes and slashes decreases row by row.
	"""
	for i in range(SIZE):
		print('|', end="")
		for j in range(i):
			print('.', end="")
		for k in range(SIZE - i):
			print('\\/', end='')
		for j in range(i):
			print('.', end="")
		print('|', end="")
		print('')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()