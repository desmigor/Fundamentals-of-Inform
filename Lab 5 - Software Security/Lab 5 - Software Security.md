# Lab 5 - Software Security

> Igor Mpore
>
> BS19-CS01
>
> i.mpore@innopolis.university



## 1. Preparation

#### a.  Debugger Choice

In this lab, I used **Cutter** as my debugger for the these binaries. Cutter is a QT based GUI for reverse engineering binaries, which makes use of **radare2** framework. It's by far the best tool used for reverse engineering. [Ref](https://cutter.re/) 

#### b.  Checking if the given binaries are safe

As we already did in the previous lab of this course, we have to perform Malware analysis before we do reverse engineering of these binaries to know what they do. For these binaries to be analyzed, we'll use an online tool called **[virustotal](https://www.virustotal.com/gui/home/upload)** as ANY.RUN doesn't support linux binaries. This will be a basic Static malware analysis.

##### <u>sample32</u>

		1. <u>*Checking the hash of a file to make sure it maches what Virustotal get:*</u>

​		`hashdeep ./Downloads/binaries/binaries/sample32`	![image-20220223151610713](/home/koala/.config/Typora/typora-user-images/image-20220223151610713.png)

- md5: 8087e213bc03bb7acf9e50764de3ded3

- sha256: 70efd61ca25f9487f5da82a3805c113023c9361cb63d507e306b9b7b93e03e5f

2. <u>Report from virus total (Full report can be found [here](https://www.virustotal.com/gui/file/70efd61ca25f9487f5da82a3805c113023c9361cb63d507e306b9b7b93e03e5f/detection))</u>

![image-20220223153702376](/home/koala/.config/Typora/typora-user-images/image-20220223153702376.png)

As you can see, we can confirm that the file's **MD5 and SHA256**  is the same as what virus total got.

![image-20220223153726606](/home/koala/.config/Typora/typora-user-images/image-20220223153726606.png)



##### <u>sample64</u>

  		1. <u>*Checking the hash of a file to make sure it maches what Virustotal get:*</u>

​		`hashdeep ./Downloads/binaries/binaries/sample64`

![image-20220223154211011](/home/koala/.config/Typora/typora-user-images/image-20220223154211011.png)



- md5: 288c7661a74b9b17e49e69c2d7d63557

- sha256: 51d1c6635af02f0d202fa07a643200a84bbfb9576d8b8aa4a22b47f527a82895

2. <u>Report from virus total (Full report can be found [here](https://www.virustotal.com/gui/file/51d1c6635af02f0d202fa07a643200a84bbfb9576d8b8aa4a22b47f527a82895/detection))</u>

![image-20220223154439259](/home/koala/.config/Typora/typora-user-images/image-20220223154439259.png)



As you can see, we can confirm that the file's **MD5 and SHA256**  is the same as what virus total got.

![image-20220223154645145](/home/koala/.config/Typora/typora-user-images/image-20220223154645145.png)



##### <u>sample64-2</u>

  		1. <u>*Checking the hash of a file to make sure it maches what Virustotal get:*</u>

​		`hashdeep ./Downloads/binaries/binaries/sample64-2`

![image-20220223155514507](/home/koala/.config/Typora/typora-user-images/image-20220223155514507.png)

- md5: e7a1c10a447d92738a5c90c0785f6d0f

- sha256:73cf2b3ef770677773a44de3be17db67cd54354f363770d82e61b5a27f29a5c4

2. <u>Report from virus total (Full report can be found [here](https://www.virustotal.com/gui/file/73cf2b3ef770677773a44de3be17db67cd54354f363770d82e61b5a27f29a5c4/detection))</u>

![image-20220223155843472](/home/koala/.config/Typora/typora-user-images/image-20220223155843472.png)



As you can see, we can confirm that the file **MD5 and SHA256** has we have is the same as what virus total got.

![image-20220223160029874](/home/koala/.config/Typora/typora-user-images/image-20220223160029874.png)



## 2. Theory

#### a. What kind of binaries I received

used the command `file binary_name` to know which kind of binary it is

- <u>sample32</u>

This is a 32bit binary

![image-20220220221515462](/home/koala/.config/Typora/typora-user-images/image-20220220221515462.png)

- <u>sample64</u>

​		This is a 64bit binary	![image-20220220221632717](/home/koala/.config/Typora/typora-user-images/image-20220220221632717.png)

- <u>sample64-2</u>

​		This is a 64bit binary

![image-20220220221845309](/home/koala/.config/Typora/typora-user-images/image-20220220221845309.png)

#### b. What is ASLR, and why do we need it?

<u>Definition:</u> [Reference](https://blog.morphisec.com/aslr-what-it-is-and-what-it-isnt/#:~:text=Address%20Space%20Layout%20Randomization)

Address Space Layout Randomization (ASLR) is a security technique which involves positioning randomly the base address of an executable an the position of libraries heap, and stack, in a process's address space.

![image-20220220231613067](/home/koala/.config/Typora/typora-user-images/image-20220220231613067.png)

we can check the if it's enabled/disabled using:

`sudo sysctl -a --pattern 'randomize'`

![image-20220220231324299](/home/koala/.config/Typora/typora-user-images/image-20220220231324299.png)

<u>Why do we need it</u>

It helps secure a system by guarding it from attacks through **buffer-overflow** and finding address space of application. ASLR is able to put [address space](https://www.techtarget.com/searchstorage/definition/address-space) targets in unpredictable locations. If an attacker attempts to exploit an incorrect address space location, the target application will crash, stopping the attack and alerting the system.

#### c. What do stripped binaries mean?

To explain better the meaning of stripped binaries, let's check the difference between <u>non-stripped and stripped binaries</u>. **Non-stripped binaries** have debugging information build into them. When they are being compiled, they have a `gcc's -g` flag activated.

Where as **Stripped binaries**, the debugging information are removed from the exe (which isn't necessary for execution) to reduce the size of the exe.

#### d. What are GOT and PLT? 

**PLT** stands for Procedure Linkage Table which is, put simply, used to call external procedures/functions whose address isn't known in the time of linking, and is left to be resolved by the dynamic linker at run time whereas

**GOT** stands for Global Offsets Table and is similarly used to resolve addresses in memory.

#### e. How can the debugger insert a breakpoint in the debugged binary/application?

To understand how a debugger inserts a breakpoint, let's first understand what a **breakpoint** is. 

In software development, a breakpoint is an intentional stopping or pausing place in a program, put in place for debugging purposes. [Ref](https://en.wikipedia.org/wiki/Breakpoint#:~:text=In%20software%20development%2C%20a%20breakpoint,referred%20to%20as%20a%20pause.&text=To%20make%20the%20program%20stop,was%20removed%2C%20called%20a%20breakpoint.)

They are two forms of breakpoints: [Ref](https://www.quora.com/What-is-the-difference-between-software-breakpoints-and-hardware-breakpoints-and-what-advantages-do-they-offer-over-each-other)

- <u>Software breakpoint</u>

  Software breakpoints replace an instruction opcode with a special “breakpoint opcode" by modifying the original program text. 

- <u>Hardware breakpoint</u>

​	Hardware breakpoints use dedicated hardware to examine the program counter and halt the machine when it reaches the specified address.		

<u>How the debugger inserts a breakpoint in the debugged binary/application</u>:

From the above definitions, we can insert a breakpoint at a certain memory address.

For example, in GRB debugger; here's how it can be done after opening a file you want to debug:

![img](https://habrastorage.org/r/w1560/getpro/habr/upload_files/9c1/2b5/47a/9c12b547a99bccdac2bd6e3b25409ec2.png)



## 3. Reversing

#### a. Disable ASLR using the command below

`sudo sysctl -w kernel.randomize_va_space=0`

![image-20220223175329639](/home/koala/.config/Typora/typora-user-images/image-20220223175329639.png)

#### b. Load the binaries into a disassembler/debugger

- sample32

  ![image-20220223181050120](/home/koala/.config/Typora/typora-user-images/image-20220223181050120.png)

  

- sample64

​		![image-20220223181036178](/home/koala/.config/Typora/typora-user-images/image-20220223181036178.png)



- sample64-2

​		![image-20220223181114066](/home/koala/.config/Typora/typora-user-images/image-20220223181114066.png)



#### c. Does the function prologue and epilogue differ in 32bit and 64bit? How do they operate?

Let's first define **Function Prologue** and **Function Epilogue** 

- **Function prologue** is a few lines of code at the beginning of a function, which prepare the stack and registers for use within the function. 
- **Function epilogue** appears at the end of the function, and restores the stack and registers to the state they were in before the function was called.

<u>How do they differ in 32bit and 64bit?</u>

The function prologue and epilogue differ in these two architectures since their job is prepare stack and registers of different sizes (32 bits of register size and 64 bits of register size respectively)

#### d. Does function calls differ in 32bit and 64bit? What about argument passing? 

Yes, the function calls differ in 32bit and 64bit because the register sizes are different so, you need to always have address translation constantly between these two architectures. This also applies to argument passing.

#### e. What does the command ldd do? 

`ldd BINARY-NAME`

ldd command is used to display shared library dependencies of an executable or even for a shared library.

`ldd ./Downloads/binaries/binaries/sample32 `

![image-20220223172626521](/home/koala/.config/Typora/typora-user-images/image-20220223172626521.png)

`ldd ./Downloads/binaries/binaries/sample64 `

![image-20220223172610770](/home/koala/.config/Typora/typora-user-images/image-20220223172610770.png)

`ldd ./Downloads/binaries/binaries/sample64-2 `

![image-20220223172650748](/home/koala/.config/Typora/typora-user-images/image-20220223172650748.png)



#### f. Why in the “sample64-2“ binary, the value of i don’t change even if our input is very long? 

> Hint: Stack Protection and Canary Protection

Stack protection refers to inserting a guard variable (referred to as canary) onto the stack frame for each vulnerable function or for all functions. For protecting **stack buffer overflows** that can be caused by returning larger values compared to what the stack can hold, Stack protection plays a bigger role.

In our case, the value of i returned is significantly large. To prevent stack buffer overflow, the value of i is kept the same after the function call **gets()**

[Reference 1](https://lwn.net/Articles/584225/) , [Reference 2](https://developer.arm.com/documentation/101754/0616/armclang-Reference/armclang-Command-line-Options/-fstack-protector---fstack-protector-all---fstack-protector-strong---fno-stack-protector)


