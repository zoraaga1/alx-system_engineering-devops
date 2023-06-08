#!/bin/bash
# What each script is doing?

**1.** pwd => prints the absolute path name of the current working directory.
**2.** ls => Display the contents list of your current directory.
**3.** cd => changes the working directory to the user’s home directory.
**4.** ls -l => Display current directory contents in a long format.
**5.** ls -la => Display current directory contents, including hidden files (starting with .). Use the long format.
**6.** ls -na => Display current directory contents.
Long format
with user and group IDs displayed numerically
And hidden files (starting with .)
**7.** mkdir -p /tmp/my_first_directory => Create a script that creates a directory named my_first_directory in the /tmp/ directory.
**8.** mv /tmp/betty /tmp/my_first_directory => Move the file betty from /tmp/ to /tmp/my_first_directory.
**9.** rm /tmp/my_first_directory/betty => Delete the file betty.
**10.** rmdir /tmp/my_first_directory => Delete the directory my_first_directory that is in the /tmp directory.
**11.** cd - =>  changes the working directory to the previous one.
**12.** ls -al . .. /boot => that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
**13.** file /tmp/iamafile =>  prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script.
**14.** ln -s /bin/ls __ls__ => Creates a symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working directory.
**15.** cp -u *.html .. => creates  a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.
**16.** mv [[:upper:]]* /tmp/u => creates a script that moves all files beginning with an uppercase letter to the directory /tmp/u.
**17.** rm *~ => deletes all files in the current working directory that end with the character ~.
**18.** mkdir -p welcome/to/school =>  creates the directories welcome/, welcome/to/ and welcome/to/school in the current directory.
**19.** ls -amvp =>  lists all the files and directories of the current directory, separated by commas (,), and ends directory names with slash (/)
**20.** 
