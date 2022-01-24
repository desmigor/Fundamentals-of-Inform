import string
 
alpha_letters= string.ascii_letters
   
key = 4

# Dictionary for substituted alphabets in plain text
dict1 = {}
for i in range(len(alpha_letters)):
    dict1[alpha_letters[i]] = alpha_letters[(i+key)%len(alpha_letters)]


def encode_funct(ptext):
    cipher_txt=[]
    # loop to generate ciphertext
    for char in ptext:
        if char in alpha_letters:
            temp = dict1[char]
            cipher_txt.append(temp)
        else:
            temp =char
            cipher_txt.append(temp)
    cipher_txt= "".join(cipher_txt)
    print("Cipher Text is: ",cipher_txt)

     
# Dictionary for substituted alphabets in cipher text
dict2 = {}     
for i in range(len(alpha_letters)):
    dict2[alpha_letters[i]] = alpha_letters[(i-key)%(len(alpha_letters))]


def decode_funct(ctext):   
    # loop to recover plain text
    decrypt_txt = []

    for char in ctext:
        if char in alpha_letters:
            temp = dict2[char]
            decrypt_txt.append(temp)
        else:
            temp = char
            decrypt_txt.append(temp)
    decrypt_txt = "".join(decrypt_txt)
    print("The plain text :", decrypt_txt)


print ("\n____Simple Substitution cipher____")

choice = input ("\nSelect E for encoding and D for Decoding: ")

if (choice == "E" or choice == "e"):
    plain_txt = input ("\nEnter your plain text: ")
    encode_funct(plain_txt)
elif (choice == "D" or choice == "d"):
    cipher_txt = input (" \nEnter your cipher text: ")
    decode_funct(cipher_txt)
else:
    print ("\nPlease enter correct value. Bye for now!")
    exit()