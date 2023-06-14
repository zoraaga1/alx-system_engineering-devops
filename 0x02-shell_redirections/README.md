# What each script is doing?

**1.** `echo "Hello, World"` => Prints **Hello, World**.

**2.** `echo "\"(Ôo)'"` => Displays a confused smiley.

**3.** `cat /etc/passwd` => Displays the content of the `/etc/passwd` file.

**4.** `cat /etc/passwd /etc/hosts` => Displays the content of `/etc/passwd` and `/etc/hosts`.

**5.** `tail /etc/passwd` => Displays the last 10 lines of `/etc/passwd`.

**6.** `head /etc/passwd` => Displays the first 10 lines of `/etc/passwd`.

**7.** `head -n 3 iacta | tail -1` => Displays the third line of the file **iacta**.

**8.** `echo "Best School" > \\\*\\\\"'\"Best School\"\\'"\\\\\*\$\\\?\\\*\\\*\\\*\\\*\\\*\:\)` => Creates a file named exactly `\*\\'"Best School"\'\\*$\?\*\*\*\*\*:)` containing the text `Best School` ending by a new line.

**9.** `ls -la >> ls_cwd_content` => Writes into the file `ls_cwd_content` the result of the command `ls -la`.
il -1 iacta >> iacta` =>  Dublicates the last line of the file `iacta`

**11.** `find . -type f -name "*.js" -delete` => Deletes all the **regular files** with a .js extension that are present in the current directory and all its subfolders.

**12.** `find . -type d -not -name '.' | wc -l` => Counts the numbers of all directories and sub-directories include hidden ones.

**13.** `ls -t | egrep -v '^d' | head -n 10` => Displays the 10 newest files in the current directory **one file per line**.

**14.** `sort | uniq -u` => Prints only words of a list that appear exactly once.

**15.** `grep root /etc/passwd` => Displays the only lines containing the pattern **root** from the file `/etc/passwd`.

**16.** `grep -c -i "bin" /etc/passwd` => Displays the number of lines that contain the pattern **bin** in the file `/etc/passwd`.

**17.** `grep -i "root" -A 3 /etc/passwd` => Displays the lines  containing the pattern  **root** and **3 lines** after them in the file `/etc/passwd`.

**18.** `grep -v in /etc/passwd` => Displays all the lines of the file `/etc/passwd` that not contain the pattern **bin**

**19.** `grep '^[[:alpha:]]' /etc/ssh/sshd_config` => Displays all lines starting with a letter in the `/etc/ssh/sshd_config`.

