
# Steps to follow to install run and connect to MySQL Server

Differ for different OS and terminals

## MacBook

1). Install mysql server through whatever convienience means you desire.
2).  To search the entire system file for your myqsl installation
>> sudo find / -name mysql -type f 
3). Add MySQL to PATH:
>> nano (e.g., ~/.bashrc, ~/.bash_profile, or ~/.zshrc)
4). Enter the following strng in the file opened with nano above, edit to match result from 2:
>> export PATH="/usr/local/mysql-8.0.27-macos11-x86_64/bin:$PATH"
>>export PATH="/usr/local/mysql-8.0.27-macos11-x86_64/support-files:$PATH"
5). Close the terminal and open a fresh one, then enter:
>> source ~/.zchrc <!-- or which ever suits your case -->
6). Start the mysql server
>> sudo sudo mysql -u root -p <!-- first password request is the sudo password, while the second is for mysql>

## Workflow for working with database

1) Create the database and schema in any database server of your choice.
2) Create all the tables that you will be working with in the database.
3). Connect to the database with any database connector of your choice and carry out all desired operations.