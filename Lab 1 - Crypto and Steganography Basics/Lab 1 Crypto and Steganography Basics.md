# Lab 1: Crypto and Steganography Basics.

> Igor Mpore
>
> BS19-CS01
>
> i.mpore@innopolis.university



## Crypto Basics



### 1. Substitution Cipher algorithm

```python
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
```

![image-20220124101730477](/home/migor/snap/typora/46/.config/Typora/typora-user-images/image-20220124101730477.png)



### 2. Transposition Algorithm

```python
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
```

![image-20220124103640778](/home/migor/snap/typora/46/.config/Typora/typora-user-images/image-20220124103640778.png)



### 3. Simple XOR Algorithm

```python
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
```

![image-20220124131232597](/home/migor/snap/typora/46/.config/Typora/typora-user-images/image-20220124131232597.png)



## Steganography Basics

### 1. Image Steganography 

(Files in the folder called "Image steg")

### 2. Audio Steganography 

(Files in the folder called "Audio steg")

### 3. Video Steganography 

(Files in the folder called "Video steg")

### 4. Covert Channels: Tunnelshell (ICMP)

Using hping3 packet, that I installed with the command:

```bash
pip install hping3 
```

I managed to use this command and then sniffing the packet using Wireshark to capture the sent message (screenshoot attached):

Ref: https://www.exploit-db.com/docs/english/18581-covert-channel-over-icmp.pdf

```bash
hping3 -1 -c 1 192.168.10.100 -e "This is a hidden message by Igor"
```

![Covert Channels Hidden Message](/home/migor/Documents/Fund. Information Security/Lab 1 - Crypto and Steganography Basics/Covert Channels Hidden Message.png)



## Enigma and Bombe

The Enigma was a machine used bu German to Encrypt information to send to their allies during the World War II. Despite of it's security, the Enigma had some design problems for encrypting data which led to the creation of Bombe that used Reverse Engineering to decrypt the information. Firstly, the main weakness of Enigma was that they <u>had to always select a random initial position of each roller</u> which resulted later destroyed the uniform distribution of the rollers. In addition, the <u>Enigma was designed that the input letter couldn't encrypt to itself</u> which would lead the attackers to know the letter which shouldn't be included during brute forcing.  Bombe also took <u>advantage that common words were considered to be in the original message</u> as it was all about war.

Ref: https://www.youtube.com/watch?v=-1ZFVwMXSXY