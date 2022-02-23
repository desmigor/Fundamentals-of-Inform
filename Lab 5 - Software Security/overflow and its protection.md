[^1]: https://www.eff.org/issues/coders/reverse-engineering-faq
[^2]: https://www.researchgate.net/publication/2885971_Reverse_Engineering_A_Roadmap
[^3]: https://github.com/mohamedaymenkarmous/CTF/tree/master/EasyCTF_IV#intro-reverse-engineering

# 1. Preparation
## a. You can use any debugger/disassembler as long as it supports the given task architecture (32bit or 64bit)
## b. Try to stay away from decompilers, as this will help you to better understand the nature of your task based on assembly only.
## c. IMPORTANT: please check what does a binary do before running it (don’t trust us )
## d. Try to do the lab in a Linux VM, as you might need to disable ASLR
Read the following articels:
- "Coder's Rights Project Reverse Engineering"[^1],
- "Reverse Engineering: A Roadmap"[^2],
- "Intro: Reverse Engineering"[^3].


# Theory
## a. What kind of files did you receive (which arch? 32bit or 64bit?)? use "file" linux command to know the files
## b. What is ASLR, and why do we need it?
## c. What do stripped binaries mean?
## d. What are GOT and PLT? 
## e. How can the debugger insert a breakpoint in the debugged binary/application?


# 3. Reversing
## a. Disable ASLR using the following command “sudo sysctl -w kernel.randomize_va_space=0”
## b. Load the binaries into a disassembler/debugger
## c. Does the function prologue and epilogue differ in 32bit and 64bit and how they operate?
## d. Does function calls differ in 32bit and 64bit? What about argument passing? 
## e. What does the command ​ldd ​do? “ldd BINARY-NAME”

## f. Why in the “sample64-2“ binary, the value of ​i​ don’t change even if our input is very long?

