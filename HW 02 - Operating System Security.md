# HW 02 - Operating System Security

> Igor Mpore
>
> BS19-CS01
>
> i.mpore@innopolis.university



##### 1.  What are the major differences between the implementations of the discretionary access control models on Unix (Linux) systems and those on Windows systems? (1.0 point)

In Unix (Linux) systems, the OS implements discretionary access control to all file system resources. These include not only files and directories but also devices, processes, memory, and other important resources. Access is specified as granting read, write, and execute permissions to each of owner, group, and others, for each resource. This can be done using the "*chmod*" command.

For Windows System, users and groups are defined with a Security ID (SID). Then,  the OS implements discretionary access controls to system resources such as files, shared memory, and named pipes. The access control list has a number of entries that may grant or deny access rights to a specific SID, which may be for an individual user or for some group of users.



##### 2.  What are the major security concerns with a hypervisor? Explain each of them. (1.0 point)

- <u>Guest OS isolation</u>: we need to ensure that programs executing within a guest OS may only access and use the resources allocated to it, and not interacting with programs or data either in other guest OSs or in the hypervisor. 

- <u>Guest OS monitoring by the hypervisor</u>: the hypervisor which has privileged access to the programs and data in each guest OS, may compromise this access if it's not secured enough.

- <u>Virtualized environment security</u>: The images and snapshots should be managed and secured from attackers who may attempt to view or modify them.



##### 3. What is VM escape and what are its implications? (1.0 point)

**VM Escape:**  An exploit that enables a hacker to move from within a virtual machine to the hypervisor, thereby gaining access to the entire computer and all the virtual machines running within it. 

**<u>Implications</u>**

As this exploit can access the host computer, it can result into further misuse of the access that was gain by the attacker such as reading, modifying or deleting some data.
