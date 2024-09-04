# MVC_controller.py
#
# Version 3 (archived as MVC_controller_3.py)
#
# Changes:
#
# - Implemented update option.
#
# BUGS:
#
# - None? (hopefully)
#
# Version 2 (archived as MVC_controller_2.py)
#
# Changes:
#
# - Replaced cascade of ifs with call to appropriate module using eval.
#
# - Changed name of object creation routine from "create" to "factory"
#   to avoid confusion with Model.create and to follow common practice
#   of Factory patterns
#   (see e.g. http://en.wikipedia.org/wiki/Factory_method_pattern).
#
# - Added "object_menu" string to make code more compact and thus easier to read.
#   Plus when we create it programmatically this is what we will create.
#
# - Added "action_menu" because I liked object_menu so much.
#
# - Changed "choice" to "action" to have a more precise and descriptive name.
#
# - Modified the list all action so that it accepts a list of objects
#   and then displays each one.
#
# Version 1 (archived as MVC_controller_1.py)
#
# Changes:
#
# - Prepared for handling multiple object types by removing references
#   to Quote.
#
# Version 0 (archived as MVC_controller_0.py)
#
# - Initial roughing out.

from MVC_model import *
import quote

action_menu = '''
    Actions
    -------
    c - create an object to add to the collection
    r - retrieve an object from the collection and display it
    u - update an object in the collection
    d - delete an object from the collection
    l - list all the objects in the collection
    q - exit

    Your choice?'''

object_menu = '''
    Which type of object do you want to create:
    - quote
    - joke
    - movie_review
    - hockey_card
    (Tip: For the time being you _have_ to choose quote).
'''

model_name = raw_input('What model would you like to work with? ')
model = Model(model_name)

over = False
while not over:
    print action_menu
    action = raw_input()
    
    if action == 'c':
        # Display menu of object choices:
        print object_menu
        # Get the user's choice:
        obj_type = raw_input('? ')
        # Call the appropriate object factory:
        obj = eval(obj_type+".factory()") # e.g. quote.factory()
        model.create(obj)
        
    elif action == 'r':
        uid = raw_input( 'What is the uid of the object you wish to retrieve? ')
        if model.retrieve(uid):
            print model.retrieve(uid)
        else:
            print 'Sorry your collection does not contain an object with that uid.'
    
    elif action == 'u':
        uid = raw_input( 'What is the uid of the object you wish to update? ')
        # retrieve the object.
        obj = model.retrieve(uid)
        # If retrieve was successful...
        if obj:
            # Call it's update method...
            obj.update()
            # and store the updated object in the model.
            new_uid = model.update(uid, obj)
        # Check if update was successful, i.e. if new_uid is not None.
        if new_uid:
            print 'Successful update. New uid =', new_uid
        else:
            print 'Update failed.'
    
    elif action == 'd':
        uid = raw_input( 'What is the uid of the object you wish to delete? ')
        if model.delete(uid):
            print 'Object %s successfully deleted.' % (uid)
        else:
            print 'Object %s could not be deleted.' % (uid)
    
    elif action == 'l':
        print 'Here are the contents of the model', model_name, ':'
        obj_set = model.listall()
        for obj in obj_set:
            print obj
            
    elif action == 'q':
        over = True
        
    else:
        print 'Not a valid choice!'
        
model.close()
