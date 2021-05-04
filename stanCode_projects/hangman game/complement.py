"""
File: complement.py
Name:鄭凱元
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    Converts characters to uppercase,
    then output the complementary sequence through the newly created function (build_complement())
    """
    dna = input('Please give me a DNA strand and I\'ll find the complement: ')
    # Converts characters to uppercase
    dna = dna.upper
    ans = build_complement(dna)
    print('The complement of ' + str(dna) + ' is ' + str(ans))



def build_complement(dna):
    # start from an empty string
    ans = ''
    # For loop: return complementary sequences
    for dna_fragment in dna:
        if dna_fragment == 'A':
            ans += 'T'
        elif dna_fragment == 'T':
            ans += 'A'
        elif dna_fragment == 'C':
            ans += 'G'
        elif dna_fragment == 'G':
            ans += 'C'
    return ans



###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
