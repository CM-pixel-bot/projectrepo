PART A: COMMAND EXCERSISES 

1. Display your current working directory --> pwd 
2. List all files in /var/log directory (including hidden files) with details--> ls -la /var/log
3. Create a directory called ’experiments’ in your home folder--> mkdir ~/experiments
4. Create an empty file named ’test.txt’ in the current directory--> touch test.txt 
5. Copy the /etc/passwd file to your home directory--> cp /etc/passwd ~/
6. Rename ’test.txt’ to ’data.txt’ in the current directory--> mv test.txt data.txt
7. Find all .conf files in /etc directory--> find /etc -type f -name "*.conf"
8. Compress the ’data.txt’ file using gzip--> gzip data.txt


PART B : BASIC SHELL SCRIPTING 


1.A script backup.sh that:
(1) Creates a backup directory
(2) Copies all .txt files from current directory to it
(3) Lists contents of backup
→
#!/bin/bash
mkdir -p backup
cp *.txt backup/
ls -l backup


2. A script clean.sh that:
(1) Lists all .tmp files in /tmp
(2) Removes them
(3) Confirms deletion by listing /tmp again
→
#!/bin/bash
ls /tmp/*.tmp 2>/dev/null
rm -f /tmp/*.tmp
ls /tmp/*.tmp 2>/dev/null || echo "All .tmp files deleted"


3. A script sysinfo.sh that displays:
(1) Current date
(2) Logged in users
(3) System uptime
(4) Memory usage
→
#!/bin/bash
date
who
uptime
free -h


4. A script compress.sh that:
(1) Creates a tar archive of /var/log
(2) Compresses it with gzip
(3) Lists the created archive
→
#!/bin/bash
tar -cf varlog.tar /var/log
gzip varlog.tar
ls -lh varlog.tar.gz
