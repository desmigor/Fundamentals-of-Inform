# Fundamentals of Information Security (S22)



> Prof. Shinnazar Seytnazarov 
>
> Summarized by Igor Mpore



## Lecture 1: Introduction to Computer Security



### 1.1 <u>Computer Security</u> 

Defined as measures and controls that ensure **confidentiality**, **integrity**, and **availability** of information system assets including hardware, software, firmware, and information being processed, stored, and communicated.

### 1.2. <u>Three key objectives (the CIA triad)</u>

- <u>Confidentiality</u>: no disclosure to unauthorized parties
- <u>Integrity</u>: no modification of information by unauthorized parties
- <u>Availability</u>: System or resource shall be available for its intended use.

### 1.3. <u>Levels of security breach impact</u>

- <u>Low</u>: the loss will have a limited impact, e.g., a degradation in mission or minor damage.
- <u>Moderate</u>: the loss has a serious effect, e.g., significance degradation on mission or significant harm to individuals but no loss of life or threatening injuries
- <u>High</u>: the loss has severe or catastrophic adverse effect on operations, organizational assets or on individuals (e.g., loss of life)

### 1.4. <u>Examples of security requirements confidentiality</u>

- <u>Student grade information:</u> high confidentiality and only available when approved
- S<u>tudent enrollment:</u> moderate confidentiality
- <u>Directory information:</u> low confidentiality
- <u>Patient's allergy information:</u> high confidentiality since it's integrity should be high enough
- <u>A system that provides authentication</u>: High confidentiality

###  1.5. <u>Computer Security Challenges</u>

- Not simple
- Unexpected attacks
- Procedures used are often counter-intuitive
- Must decide where to deploy mechanics
- Involves algorithms and secret information
- Many battles between Admin and attackers
- Requires constant monitoring
- Regarded as hindrance to using system

### 1.6. <u>Model for Computer Security</u>

<img src="/home/migor/snap/typora/46/.config/Typora/typora-user-images/image-20220120234559240.png" alt="image-20220120234559240" style="zoom:100%;" />

### 1.7 <u>Components of Computer Security</u>

- <u>System Resources</u> (Assets of Computer Security):
  - Hardware
  - Software
  - Data
  - Communication facilities and Networks
- <u>Our Vulnerabilities concern</u>
- <u>Treats that exploit vulnerabilities</u>
- <u>Attack is a threat that already occured out</u>
  - **Active attack**: attacker tries to modify content of the message
  - **Passive attack**: the attacker reads and copies content of a message and can use it for malicious purposes 
  - **Internal attacks a.k.a Insider:** An internal attack occurs when an individual or a group within an organization seeks to disrupt operations or exploit organizational assets <u>Ex:</u> selling companies data after being fired for money
  - **External attacks a.k.a Outsider:** An external threat relates to outsider attacks on the part of individuals attempting to gain unauthorized access to the network of the targeted organization.
- <u>Countermeasures:</u> actions taken to prevent, detect, recover and minimize risks

### 1.8 <u>Vulnerabilities, Threats and Attacks</u>

- <u>Categories of vulnerabilities</u>
  - Corrupted: loss of intergrity
  - Leaky: loss of confidentiality 
  - Unavailable or very slow: loss of availability
- <u>Treats</u>
  - Capable of exploiting vulnerabilities
  - Represent potential security harm to an asset
- <u>Attacks (threats carried out)</u> 
  - Types explained above 👆

### 1.9 <u>Fundamentals of Security Design Principles</u>

1. <u>Economy of mechanism:</u> security mechanism should be as simple as possible
2. <u>Fail-safe defaults:</u> unless a subject is given explicit access to an object, it should be denied access to that object
3. <u>Complete mediation:</u>  all accesses to objects should be checked to ensure they are allowed
4. <u>Open design:</u> the security of a mechanism should not depend on the secrecy of its design or implementation
5.  <u>Separation of privilege:</u>  system should not grant permission based upon a single condition
6. <u>Least privilege:</u> a user is given the minimum levels of access – or permissions – needed to perform his/her job functions.
7. <u>Least common mechanism:</u> that mechanisms used to access resources should not be shared
8. <u>Psychological acceptability:</u> security mechanisms should not make the resource more difficult to access than if the security mechanisms were not present
9. <u>Isolation:</u>  least privilege and privilege separation
10. <u>Encapsulation:</u> is a form of isolation which is designed on the principle of object-oriented principles. Here the processes of the protected system can only access the data object of the system and these processes can only be invoked from a domain entry point.
11. <u>Modularity:</u>  network security should be multilayered, with many different techniques used to protect the network. No security mechanism can be guaranteed to withstand every attack. Therefore, each mechanism should have a backup mechanism
12. <u>Layering:</u> approach that deploys multiple security controls to protect the most vulnerable areas of your technology environment where a breach or cyberattack could occur.
13. <u>Least astonishment:</u> It proposes that a component of a system should behave in a way that most users will expect it to behave.



## Lecture 2: Cryptographic tools



### 2.1 <u>Symmetric Encryption</u>

Also known as single key Encryption. It has two requirements for secure use which are:\\

- Needs a strong encryption Algorithm
-  Sender and receiver must have obtained copies of the secret key in a secure fashion and must keep the key secure

![image-20220121144923336](/home/migor/snap/typora/46/.config/Typora/typora-user-images/image-20220121144923336.png)

#### 2.1.1 Types of Symmetric Encryption

1. <u>Block Cipher:</u>

   - This is the most common type of Symmetric encryption which processes the input one block of elements at a time and produces the output block for each input block.

   - In addition to that, it can reuse keys

   ![image-20220124182200428](/home/migor/snap/typora/46/.config/Typora/typora-user-images/image-20220124182200428.png)

   

2. <u>Stream Cipher</u>:

   - It processes input elements continuously (one byte at a time) and produces output of one element at a time.
   - It's almost always faster and has far less code 

   ![image-20220124182227753](/home/migor/snap/typora/46/.config/Typora/typora-user-images/image-20220124182227753.png)

   

#### 2.1.2 Three popular symmetric Encryption

1. <u>DES (Data Encryption Standard):</u> uses 64 bit plaintext block and 56 bit key to produce a 64 bit ciphertext block
2. <u>Triple DES</u>: repeats basic DES algorithm three times using either two or three unique keys
3. <u>AES (Advanced Encryption Standard)</u>: Uses symmetric block cipher with 128 bit data & 128/192/256 bit keys. it's now widely available commercially.

<u>**Their comparison**</u>

![image-20220124182327564](/home/migor/snap/typora/46/.config/Typora/typora-user-images/image-20220124182327564.png)



### 2.2 <u>Asymmetric Encryption</u>

a.k.a Public-key Crytography. It uses pairs of keys that consists of a **public key and a private key**. The generation of such key pairs depends on cryptographic algorithms which are based on mathematical problems termed one-way functions.

![Image displaying differences between symmetric and asymmetric encryption](https://cdn.ttgtmedia.com/rms/onlineimages/security-symmetric_vs_asymmetri_encryption_mobile.png)



### 2.3 <u>Cryptographic systems</u>

They are 3 independent dimensions:

- Type of Operations used
  - Substitution
  - Transposition
  - Rotor machine
  - XOR cipher
- Number of keys
  - Symmetric, single key,secret key, conventional encryption
  - Asymmetric, two key, a.k.a public-key encryption
- The way the plaintext is processed
  - block cipher
  - stream cipher

### 2.4 <u>Attacking symmetric encryption</u>

1. Cryptanalysis:

   - Involves relying on the nature of the algorithm, plaintext characteristics and sometimes samples of plaintext-ciphertext pairs.

   <u>Types of cryptanalysis attacks</u>

   ![image-20220124174053854](/home/migor/snap/typora/46/.config/Typora/typora-user-images/image-20220124174053854.png)

2. Brute-force attack:

   - Involves trying all possible keys on some ciphertext intil you get an intelligible translation into plaintext.

### 2.5 <u>Simple Ciphers</u> ([link](http://www.crypto-it.net/eng/simple/index.html))

1. <u>Substitution ciphers</u>

   Involves replacing every group of plaintext letters with another predefined group.

   Ex: Caesar Cipher

2. <u>Transposition ciphers</u>

   transposition ciphers rearrange the original message letters.

   Ex: Rail Fence Cipher

1. <u>Rotor machines</u>

   Electric rotor machines were mechanical devices that allowed to use encryption algorithms that were much more complex than ciphers, which were used manually.

   Ex: Enigma, Bomber

2. <u>Simple XOR</u>

   This algorithm adds subsequent plaintext bytes to secret key bytes using XOR operation. After using the last secret key byte, one should return to the first byte.

   Ex: M XOR K = C , C XOR K = M

### 2.6 <u>Steganography</u>

Steganography works **by hiding information in a way that doesn't arouse suspicion**. One of the most popular techniques is 'least significant bit (LSB) steganography. In this type of steganography, the information hider embeds the secret information in the least significant bits of a media file such as photo, video or even audio.

1. Image Steganography ([link](https://stylesuxx.github.io/steganography/))
2. Audi Steganography ([link](http://jpinsoft.net/deepsound))
3. Video Steganography ([link](https://betterprogramming.pub/a-guide-to-video-steganography-using-python-4f010b32a5b7))
4. Covert channels: Tunnelshell (ICMP [link](https://www.exploit-db.com/docs/english/18581-covert-channel-over-icmp.pdf))



## Lecture 3: Cryptographic tools



### 3.1 <u>Message Authentication</u>

Message encryption is good against passive attack and then message authentication protects against message authentication. To achieve authentication, sender and receiver can share a common key. <u>Depending on the environment, the security system decides if both message encryption and authentication  is neccessary or one is enough.</u>8

