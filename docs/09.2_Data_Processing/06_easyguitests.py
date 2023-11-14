# easygui_eg.py
#
# EasyGUI example for CPSC 129 W2013.
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

# Get the input data studenet name from the user.
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
    msg = 'No worries %s %s is registered.' % (first_name, last_name)
else:
    msg = '%s %s hasn’t registered yet.' % (first_name, last_name)
# ...and output it.
easygui.msgbox(msg)
