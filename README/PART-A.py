PART A: COMMAND EXCERSISES 

1. Display your current working directory --> pwd 
2. List all files in /var/log directory (including hidden files) with details--> ls -la /var/log
3. Create a directory called ’experiments’ in your home folder--> mkdir ~/experiments
4. Create an empty file named ’test.txt’ in the current directory--> touch test.txt 
5. Copy the /etc/passwd file to your home directory--> cp /etc/passwd ~/
6. Rename ’test.txt’ to ’data.txt’ in the current directory--> mv test.txt data.txt
7. Find all .conf files in /etc directory--> find /etc -type f -name "*.conf"
8. Compress the ’data.txt’ file using gzip--> gzip data.txt


1.List all files (including hidden ones) in the current directory in a detailed format
→ ls -la

2.Create a directory named projects inside your home directory
→ mkdir ~/projects

3.Remove a file named old file.txt (first create it if it doesn’t exist)
→ touch "old file.txt" && rm "old file.txt"

4.Copy a file named notes.txt from your home directory to the projects directory
→ cp ~/notes.txt ~/projects/

5.Move a file named draft.txt from the current directory to the projects directory
→ mv draft.txt ~/projects/

6.Display the manual page for the mkdir command
→ man mkdir

7.Compress a file named data.txt using gzip
→ gzip data.txt

8.List all running processes and find a specific process (e.g., firefox)
→ ps aux | grep firefox

9.Terminate a process named unresponsive app
→ pkill -f "unresponsive app"

10.Mount a USB drive manually (assume it appears as /dev/sdb1)
→ sudo mount /dev/sdb1 /mnt
