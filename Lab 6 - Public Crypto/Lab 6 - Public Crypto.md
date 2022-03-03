# Lab 6 - Public Crypto

> Igor Mpore
>
> BS19-CS01
>
> i.mpore@innopolis.university



### 1. Crypto basics 1

In this solution, I have ignored the inital Key Addition of k~0~ . We know that all the S-boxes are the same function, and that the input will the same in each case (FF~16~FF~16~). The array  (A~0~−A~15~) is produced by Byte Substitution and it resulted into the array below:


$$
\begin{bmatrix}
{16}_{16}~ &{16}_{16}&{16}_{16}&{16}_{16}\\
{16}_{16}~ &{16}_{16}&{16}_{16}&{16}_{16}\\
{16}_{16}~ &{16}_{16}&{16}_{16}&{16}_{16}\\
{16}_{16}~ &{16}_{16}&{16}_{16}&{16}_{16}\\
\end{bmatrix}
$$

Using the MixColumn matrix multiplication, we can express the above matrix as below since $ax+bx+cx+dx=x(a+b+c+d)$:
$$
\begin
{bmatrix}
(02+03+01+01)×{16}_{16}\\
(01+02+03+01)×{16}_{16}\\
(01+01+02+03)×{16}_{16}\\
(03+01+01+02)×{16}_{16}\\
\end{bmatrix}
$$
Now, let's bitwise XOR the round key into the state:
$$
\begin{bmatrix}
{16}_{16}~ &{16}_{16}&{16}_{16}&{16}_{16}\\
{16}_{16}~ &{16}_{16}&{16}_{16}&{16}_{16}\\
{16}_{16}~ &{16}_{16}&{16}_{16}&{16}_{16}\\
{16}_{16}~ &{16}_{16}&{16}_{16}&{16}_{16}\\
\end{bmatrix}

XOR

\begin{bmatrix}
{FF}_{16}~ &{FF}_{16}&{FF}_{16}&{FF}_{16}\\
{FF}_{16}~ &{FF}_{16}&{FF}_{16}&{FF}_{16}\\
{FF}_{16}~ &{FF}_{16}&{FF}_{16}&{FF}_{16}\\
{FF}_{16}~ &{FF}_{16}&{FF}_{16}&{FF}_{16}\\
\end{bmatrix}

=

\begin{bmatrix}
{E9}_{16}~ &{E9}_{16}&{E9}_{16}&{E9}_{16}\\
{E9}_{16}~ &{E9}_{16}&{E9}_{16}&{E9}_{16}\\
{E9}_{16}~ &{E9}_{16}&{E9}_{16}&{E9}_{16}\\
{E9}_{16}~ &{E9}_{16}&{E9}_{16}&{E9}_{16}\\
\end{bmatrix}
$$
That is the final state after the first round of encryption.

### 2. Crypto basics 2

> Hint: CBC (Cipher Block Chaining) Cryptography 

Since both attacks are based on CBC (Cipher Block Chaining), let's first define it.

<u>CBC Mode cryptography</u> is a cryptography mode of operation for a block cipher which allows encryption of arbitrary length data. Encryption and decryption are defined by:
$$
\begin{gather}
{C}_i = {e}_K ({P}_i ⊕{C}_{i−1}) \\
{P}_i = {d}_K ({C}_i)⊕ {C}_{i−1}
\end{gather}
$$

1. **<u>Padding Oracle Attack</u>**

   In symmetric cryptography, the padding oracle attack can be applied to the CBC mode of operation, where the "oracle" (usually a server) leaks data about whether the padding of an encrypted message is correct or not. Such data can allow attackers to decrypt (and sometimes encrypt) messages through the oracle using the oracle's key, without knowing the encryption key.

2. **<u>CBC Byte Flipping Attack</u>**

   This attack prepends certain values to the plaintext before encryption with the aim to hange the final cipher text even though the attacker has no ability to know what the plaintext was. This attack can be considered as a Denial of Service attack since the intended receiver can't get the correct message from the sender.

### 3. Crypto basics 3

In this exercise, the ordering of bytes within the array table grid will be column by column (i.e from left to right).
$$
\begin{array}{|c|c|} \hline A_0 & A_4 & A_8 & A_{12} \\ \hline A_1 & A_5 & A_9 & A_{13} \\ \hline A_2 & A_6 & A_{10} & A_{14} \\ \hline A_3 & A_7 & A_{11} & A_{15} \\ \hline \end{array}
$$

1. **<u>First round of AES to the input W and the subkeys W0, . . . ,W7.</u>**

The first state after adding ${k}_0$ is as follow:
$$
\begin{array}{|c|c|} \hline 2A & 28 & AB & 09 \\ \hline 7E & AE & F7 & CF \\ \hline 15 & D2 & 15 & 4F \\ \hline 16 & A6 & 88 & 3C \\ \hline \end{array}
$$
After applying the ByteSubstitution (S-box) layer, the state is as follows:
$$
\begin{array}{|c|c|} \hline E5 & 34 & 62 & 01 \\ \hline F3 & E4 & 68 & 8A \\ \hline 59 & B5 & 59 & 84 \\ \hline 47 & 24 & C4 & EB \\ \hline \end{array}
$$
We then perform ShiftRows layer where the first row remains unchainged and the other rows are rotated right by a number of positions; the second by 3, the third by 2 and the fourth by 1. This gives the following:
$$
\begin{array}{|c|c|} \hline E5 & 34 & 62 & 01 \\ \hline E4 & 68 & 8A & F3 \\ \hline 59 & 84 & 59 & B5 \\ \hline EB & 47 & 24 & C4 \\ \hline \end{array}
$$
The final transformation (other than the $k_1$ addition) is the MixColumn layer. This involves a Galois Extension Field matrix multiplication with the following description:
$$
\left( \begin{array}{c} C_0 \\ C_1 \\ C_2 \\ C_3 \\ \end{array} \right) = \left( \begin{array}{c} 02 & 03 & 01 & 01 \\ 01 & 02 & 03 & 01 \\ 01 & 01 & 02 & 03 \\ 03 & 01 & 01 & 02 \\ \end{array} \right) \left( \begin{array}{c} B_0 \\ B_5 \\ B_{10} \\ B_{15} \\ \end{array} \right)
$$
Where $C = Outputted\:Column$ And $ B = Input\:columns \:which \:were\:the\:output\:of\:the\:ShiftRows \:layer.$ 

After doing the calculations, the resulted state is as follow :
$$
\begin{array}{|c|c|} \hline 54 & 13 & 3C & 7D \\ \hline 36 & 34 & A2 & FC \\ \hline 95 & 86 & 36 & D4 \\ \hline 44 & 3E & 3D & D6 \\ \hline \end{array}
$$
All that’s left to do after this is the KeyAddition layer which results into the following final state:
$$
\begin{array}{|c|c|} \hline F4 & 9B & 1F & 57 \\ \hline CC & 60 & 01 & 90 \\ \hline 6B & AA & 0F & A2 \\ \hline 53 & 8F & 04 & D3 \\ \hline \end{array}
=
F4CC6B539B60AA8F1F010F045790A2D3_{16}
$$


2. **<u>First round of AES for the case that all input bits are zero</u>**

For the case that the input is all-zeroes, the state after the $k_0$ key addition will be:
$$
\begin{array}{|c|c|} \hline 2B & 28 & AB & 09 \\ \hline 7E & AE & F7 & CF \\ \hline 15 & D2 & 15 & 4F \\ \hline 16 & A6 & 88 & 3C \\ \hline \end{array}
$$
After this, we apply ByteSubstitution (S-box) layer , ShiftRows layer and The MixColumn respectively:
$$
\begin{array}{|c|c|} \hline F1 & 34 & 62 & 01 \\ \hline F3 & E4 & 68 & 8A \\ \hline 59 & B5 & 59 & 84 \\ \hline 47 & 24 & C4 & EB \\ \hline \end{array}
\rightarrow
\begin{array}{|c|c|} \hline F1 & 34 & 62 & 01 \\ \hline E4 & 68 & 8A & F3 \\ \hline 59 & 84 & 59 & B5 \\ \hline EB & 47 & 24 & C4 \\ \hline \end{array}
\rightarrow
\begin{array}{|c|c|} \hline 7C & 13 & 3C & 7D \\ \hline 22 & 34 & A2 & FC \\ \hline 81 & 86 & 36 & D4 \\ \hline 78 & 3E & 3D & D6 \\ \hline \end{array}
$$
Lastly, we perform KeyAddition for $k_1 = W_4,...,W_7$ and the final state is as follow:
$$
\begin{array}{|c|c|} \hline 
DC & 9B & 1F & 57 \\ \hline 
D8 & 60 & 01 & 90 \\ \hline 
7F & AA & 0F & A2 \\ \hline 
6F & 8F & 04 & D3 \\ \hline 
\end{array}
=DCD87F6F9B60AA8F1F010F045790A2D3_{16}
$$

3. **<u>How many output bits have changed?</u>**

To be able to view the changes,  we can apply XOR on the two output values together. This produces:
$$
2814143c000000000000000000000000_{16}
$$
From this, we can see that only the first column is altered after the first round:
$$
2814143c_{16} = 101000000101000001010000111100_2
$$

### 4. Crypto basics 4 

Starting from $RC[1]=01$ , $RC[i]=02×RC[i−1]modP(x)$ where $P(x)$ is the AES polynomial, we get that:
$$
\begin{gather}
RC[1]=1={00000001}_2={01}_{16} \\
RC[2]=x={00000010}_2={02}_{16} \\
RC[3]=x^2={00000100}_2={04}_{16} \\
RC[4]=x^3={00001000}_2={08}_{16} \\
RC[5]=x^4={00010000}_2={10}_{16} \\
RC[6]=x^5={00100000}_2={20}_{16} \\
RC[7]=x^6={01000000}_2={40}_{16} \\
RC[8]=x^7={10000000}_2={80}_{16} \\
RC[9]=x^4+x^3+x+1={00011011}_2={1B}_{16} \\
RC[10]=x^5+x^4+x^2+x={00110110}_2={36}_{16} \\
\end{gather}
$$
So, from the above calculation, $RC[8]={80}_{16}$ and $RC[10]={36}_{16}$