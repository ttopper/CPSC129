# Appending to files

If opening a file to write to it destroys an existing file by that name
you might be wondering how log files work. After all they just grow as
new events occur and are added to the log of events that have 
occurred in the past. The answer is that there is one more mode, `a` for **a**ppend
which allows you to open a file to append things to it, i.e. the
existing file data is not destroyed, and the insertion point is placed
at the end of the file so further writes add to the existing file
content.
