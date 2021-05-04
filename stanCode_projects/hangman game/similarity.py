"""
File: similarity.py
Name:鄭凱元
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""

def homology(new_long_sequence, new_short_sequence):
    # start from an empty string
    ans = ''
    highest_score = 0
    """
    The number in parentheses is the length of the long sequence minus the length of the short sequence,
    then plus one.
    """
    for i in range(len(new_long_sequence)-len(new_short_sequence)+1):

        # ch is a string used to access long_sequence
        ch = new_long_sequence[i:i+len(new_short_sequence)]

        # score is used to calculate the number of matches
        score = 0

        # use absolute position for two strings (It ensures that they correspond to each other.)
        for j in range(len(new_short_sequence)):
            if new_short_sequence[j] == ch[j]:
                score += 1
        # As the similarity increases, the access string is changed
        if score > highest_score:
            highest_score = score
            ans = ch
    return ans



def main():
    """
    Capitalize the two DNA sequences so that the answers are not affected.

    function homology is used to find the interval with the highest similarity.
    I use double for loop, one for the position of a long sequence string,
    and the other for each word in the string.
    """
    long_sequence = input("Please give ne a DNA sequence to search: ")
    short_sequence = input("What DNA sequence would you like to match? ")

    # converts characters to uppercase
    new_long_sequence = long_sequence.upper()
    new_short_sequence = short_sequence.upper()

    ans = homology(new_long_sequence, new_short_sequence)
    print("The best match is " + ans)

###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
