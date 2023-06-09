# What each script is doing?

**1.** `su anothe_user` => Switches the current user to the the another_user.

**2.** `whoami` => Prints the effective username of the current user.

**3.** `groups` => Prints all the groups the current user is part of.

**4.** `chown betty hello` => Changes the owner of the file hello to the user betty.

**5.** `touch hello` => Creates an empty file called hello.

**6.** `chmod u+x hello` => Adds execute permission to the owner of the file hello.

**7.** `chmod 754 hello` => Adds execute permission to the owner and the group owner, and read permission to other users, to the file hello in the working directory.

**8.** `chmod +x hello` => Adds execution permission to the owner, the group owner and the other users, to the file hello in the working directory.

**9.** `chmod 007 hello` => Sets the permission to the file hello in the workinf directory  as follows:
- Owner: no permission at all.
- Group: no permission at all.
- Other users: all the permissions.

**10.** `chmod 753 hello` => Sets the mode of the file hello to this: `-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello`.

**11.** `chmod --reference=olleh hello` => Sets the mode of the file hello the same as olleh’s mode.

**12.** `chmod -R +X .` => Adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users.

**13.** `mkdir -m 751 my_dir` => Creates a directory called my_dir with permissions 751 in the working directory.

**14.** `chown :school hello` => Changes the group owner to school for the file hello.

**15.** `chown -R vincent:staff .` => Changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.

**16.** `chown -h vincent:staff _hello` => Changes the owner and the group owner of the symbolic link `_hello` to vincent and staff respectively.

**17.** `chown -R --from=guillaume betty .` => Changes the owner of the file hello to betty only if it is owned by the user guillaume.

**18.** `telnet towel.blinkenlights.nl` => Plays the ***StarWars IV*** episode in the terminal.
