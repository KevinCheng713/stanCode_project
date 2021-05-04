"""
File: caesar.py
Name:鄭凱元
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def decipher(new_ciphered_string, number):
    ans = ''
    for ch in new_ciphered_string:
        if ch in ALPHABET:
            """
            After you find where the character is in alphabet,
            move to the right n times (Secret number = n), 
            you 'll get what the decrypted character is.
            """
            position = ALPHABET.find(ch)
            position += number
            """
            Because of the length of Alphabet is 26, 
            when the value of position exceeds 26, divided it by 26, 
            and the remainder is its corresponding position.
            """
            if position > 25:
                position %= 26
            ans += ALPHABET[position]
        else:
            ans += ch
    return ans



def main():
    """
    Function decipher is used to decrypt.
    (the user simply enters the encrypted text
    and the number of times the alphabet position is moved to the right)

    *if you would like to move to the left, enter negative values
    """
    number = int(input("Secret number: "))
    ciphered_string = input("What's the ciphered string?")
    new_ciphered_string = ciphered_string.upper()
    ans = decipher(new_ciphered_string, number)
    print('The deciphered string is: ' + str(ans))



#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
