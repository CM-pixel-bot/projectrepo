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


1. A script named backup.sh that copies all .txt files from the current directory to a backup folder
→
#!/bin/bash
mkdir -p backup
cp *.txt backup/


2.A script named cleanup.sh that removes all temporary files (ending with .tmp)
→
#!/bin/bash
rm -f *.tmp


3.A script named archive.sh that compresses a given directory into a tar.gz file
→
#!/bin/bash
tar -czf archive.tar.gz your_directory/

Or with a directory argument:
→
#!/bin/bash
tar -czf "$1.tar.gz" "$1"


4.A script named disk info.sh that lists mounted filesystems using udisksctl
→
#!/bin/bash
udisksctl status


5.A script named kill process.sh that forcefully terminates a process by name (use pkill)
→
#!/bin/bash
pkill -9 -f "process_name"

Or with a process name argument:
→
#!/bin/bash
pkill -9 -f "$1"

