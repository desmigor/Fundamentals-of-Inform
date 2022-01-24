import string
 
key = 4
def encode_funct(ptext):
    # Defining XOR key
    xorKey = 'F';

    # calculate length of input string
    length = len(ptext);
    for i in range(length):
        ptext = (ptext[:i] +
             chr(ord(ptext[i]) ^ ord(xorKey)) +
                     ptext[i + 1:]);
    return ptext;

print ("\n____Simple XOR cipher____")
plain_txt = input (" \nEnter your plain text: ")
cipher_txt = encode_funct(plain_txt)
print ("Cipher text is:" + cipher_txt)
