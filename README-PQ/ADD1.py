PART A: COMMAND EXCERSISES 

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

