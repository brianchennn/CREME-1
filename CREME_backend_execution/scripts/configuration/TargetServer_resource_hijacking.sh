#!/usr/bin/expect -f
set delKnownHosts [lindex $argv 0]
set ip [lindex $argv 1]
set username [lindex $argv 2]
set password [lindex $argv 3]

set timeout 60

# SSH connection
spawn /bin/bash $delKnownHosts
send "exit\r"

spawn ssh $username@$ip
expect "*continue connecting (yes/no*)? "
send "yes\r"
expect " password: "
send "$password\r"

expect "*:~# "
send "service continuum restart\r"

# exit
expect "*:~# "
send "exit\r"
