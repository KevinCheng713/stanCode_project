"""
File: anagram.py
Name: 鄭凱元
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""
import time

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
dic_lst = []                  # Store all words in the dictionary into a list
anagram_lst = []              # The list used to access all the anagrams
count = 0                     # Calculate the number of Anagrams


def main():
    global count, anagram_lst
    print('Welcome to stanCode "Anagram Generator"(or -1 to quit)')
    read_dictionary()
    while True:
        input_text = input('Find anagrams for: ')
        start = time.time()

        if input_text == EXIT:
            break
        else:
            find_anagrams(input_text)
            print('Searching...')
            print(count, 'anagrams:', anagram_lst)
            count = 0
            word = ''
            word_lst = []
            anagram_lst = []
            finish = time.time()

    print('Processing time:', str(finish-start))


def read_dictionary():
    global dic_lst
    with open(FILE, 'r') as f:
        for line in f:
            lst = line.split()
            dic_lst += lst


def find_anagrams(s):
    """
    :param s: (str)input word
    :return: Print out the corresponding anagram from the dictionary
    """
    helper(s, '')


def helper(s, word):
    global count
    # base case
    if len(s) == 0:
        if word in dic_lst and word not in anagram_lst:
            print('Searching...')
            print('Found: ', word)
            count += 1
            anagram_lst.append(word)

    # backtracking
    else:
        for i in range(len(s)):
            if has_prefix(word) is True:
                # Choose
                word += s[i]
                # Explore
                sub_s = s[:i] + s[i+1:]
                helper(sub_s, word)
                # Un-choose
                word = word[:-1]


def has_prefix(sub_s):
    """
    :param sub_s: The string currently accessed from input_text
    :return: True or False (Determine if the dictionary has a corresponding word)
    """
    for vocabulary in dic_lst:
        if vocabulary.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
