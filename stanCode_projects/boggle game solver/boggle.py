"""
File: boggle.py
Name: 鄭凱元
----------------------------------------
This program will use 4*4 English letters to concatenate words,
The method of concatenating letters can include all the surrounding neighbors, but you can only add once
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dic_lst = []				# Store all words in the dictionary into a list
word_lst = []				# The list used to access all the English words that can be linked together
count = 0					# Calculate the number of words


def main():
	"""
	It is a 'boggle' word search game
	"""
	read_dictionary()
	large_lst = []			# A large list that accesses four lists
	# input 4 row of letters
	for i in range(1, 5):
		letter = input(str(i) + ' row of letters: ')
		if len(letter) != 7 or not letter.islower():
			print('Illegal input')
			break
		lst = []
		for j in range(4):
			# only letter[0,2,4,6] has letters
			lst += letter[2*j]
		large_lst.append(lst)
	# large_lst = [['f', 'y', 'c', 'l'], ['i', 'o', 'm', 'g'], ['o', 'r', 'i', 'l'], ['h', 'j', 'h', 'u']]

	if len(large_lst) == 4:
		for x in range(4):
			for y in range(4):
				word = large_lst[x][y]
				row_col_lst = [(x, y)]
				find_word(x, y, large_lst, word, row_col_lst)
				row_col_lst = []
		print(f"There are {count} words in total.")


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dic_lst
	with open(FILE, 'r') as f:
		for line in f:
			lst = line.split()
			dic_lst += lst


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for vocabulary in dic_lst:
		if vocabulary.startswith(sub_s):
			return True
	return False


def find_word(x, y, large_lst, word, row_col_lst):
	"""
	:param x: The x coordinate to pick from large_lst
	:param y: The y coordinate to pick from large_lst
	:param large_lst: A large list that accesses four lists
	:param word: (str)
	:param row_col_lst: Used to access the position of a letter that has been added (Avoid adding letters in the same place)
	:return: Print out the corresponding anagram from the dictionary
	"""
	global count
	# base case
	if word in dic_lst and len(word) >= 4 and word not in word_lst:
		print(f'Found "{word}"')
		count += 1
		word_lst.append(word)

	# recursive case
	# delete else:  
	if has_prefix(word) is True:
		for i in range(-1, 2):
			for j in range(-1, 2):
				x_axis = x+i
				y_axis = y+j
				if 0 <= x_axis < 4 and 0 <= y_axis < 4:
					if (x_axis, y_axis) not in row_col_lst:
						# Choose
						word += large_lst[x_axis][y_axis]
						row_col_lst += [(x_axis, y_axis)]
						# Explore
						find_word(x_axis, y_axis, large_lst, word, row_col_lst)
						# Un-choose
						word = word[:-1]
						row_col_lst.pop()


if __name__ == '__main__':
	main()
