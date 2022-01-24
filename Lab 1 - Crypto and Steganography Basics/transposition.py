import string
 
key = 4
def encode_funct(ptext):
        # remove all white spaces in text
    plain_text = ptext.replace(" ", "")

    # change plain text to upper case
    plain_text = plain_text.upper()

    # divide plain text into layers number of strings using th key number
    rail = [""] * key
    layer = 0
    for character in plain_text:
        rail[layer] += character
        if layer >= key - 1:
            layer = 0
        else:
            layer += 1
    cipher = "".join(rail)
    return cipher

print ("\n____Rail Fence Transposition cipher____")
plain_txt = input (" \nEnter your plain text: ")
cipher_txt = encode_funct(plain_txt)
print ("Cipher text is:" + cipher_txt)
