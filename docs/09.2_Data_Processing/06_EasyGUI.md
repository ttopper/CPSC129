# EasyGUI

Earlier I said that a naive user should not be confronted with Python
error messages. Similarly they shouldn’t really be confronted by a
Python shell to interact with, but should instead get to interact with
the sorts of interface elements they are used to, e.g. message boxes,
pick lists, file dialogs, etc. If you just need simple dialogues a
library called EasyGUI is your friend. It makes it incredibly easy to
use GUI components for user interaction instead of the Python
console[^*].

EasyGUI is very easy to get started with. Its [brief
tutorial](https://easygui.sourceforge.net/tutorial.html) explains
almost all the language features. Here’s an artificial program
ilustrating some of them. Copy and run it to see how it looks when it
runs (don’t forget to install EasyGUI with pip first).

``` python
# easygui_eg.py
# EasyGUI example for CPSC 129 W13.
#
# Check to see if a particular student is in the contestant file
# for a spelling bee.
import easygui

# Greet the user.
# (Maybe this would be better as a ccbox...)
msg = '''This program will let you check that a student has
registered for the spelling Bee.'''
title = 'Check contestant registration'
easygui.msgbox(msg, title)

# Get the input data student name from the user.
prompt = 'Enter the name of the student you want to check for:'
title = 'Student name'
fields = ['First name', 'Last name']
(first_name, last_name) = easygui.multenterbox(prompt, title, fields)

# Get the filename from the user.
msg = "Select the contestants file to check:"
infile_name = easygui.fileopenbox(msg, title)
# easygui.msgbox(infile_name) #  Debug

# Check the contestant file for the contestant.
infile = open(infile_name, 'r')
found = False
for line in infile:
    (junk, last, first) = line.split(',')
    first = first.rstrip() # To remove trailing newline character.
    if first == first_name and last == last_name:
        found = True
        break

# Prepare an appropriate output message...
if found:
    msg = f'No worries {first_name:s} {last_name:s} is registered.'
else:
    msg = f'{first_name:s} {last_name:s} hasn’t registered yet.'
# ...and output it.
easygui.msgbox(msg)
```

------------------------------------------------------------------------

[^*]There is one possible hitch that sometimes arises: it can quarrel
with IDLE (because both are TK-based tools, both running TK event loops
which can conflict), so you may have to use some other text editor for
composing your code, and then run it by double-clicking the python file.
