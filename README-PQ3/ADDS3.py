PART A : BASIC SHELL SCRIPTING 


1.Show the first 5 lines of /etc/passwd
→ head -n 5 /etc/passwd

2.Create directory structure data/2025/jan,feb,mar
→ mkdir -p data/2025/jan data/2025/feb data/2025/mar

3.Count number of .conf files in /etc
→ find /etc -type f -name "*.conf" | wc -l

4.Search for "permission denied" in /var/log/auth.log
→ grep "permission denied" /var/log/auth.log

5.Create a 100MB file named testfile using dd
→ dd if=/dev/zero of=testfile bs=1M count=100

6.Display memory usage statistics
→ free -h

7.List all mounted filesystems
→ df -h






PART B : BASIC SHELL SCRIPTING 


1. A script backup_home.sh that:
(1) Creates timestamped directory in /backups
(2) Copies /home to it
(3) Compresses the backup
(4) Verifies backup integrity
→
#!/bin/bash
timestamp=$(date +%Y%m%d_%H%M%S)
mkdir -p /backups/$timestamp
cp -r /home /backups/$timestamp/
tar -czf /backups/$timestamp.tar.gz -C /backups $timestamp
tar -tzf /backups/$timestamp.tar.gz


2. A script clearlogs.sh that:
(1) Lists all .log files in /var/log
(2) Archives them
(3) Truncates original files
(4) Confirms operation
→
#!/bin/bash
log_files=$(find /var/log -name "*.log")
tar -czf /var/log/logs_$(date +%Y%m%d).tar.gz $log_files
> $log_files
ls -lh /var/log/*.log
