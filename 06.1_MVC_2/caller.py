import classes

print 'here goes...'
typ = raw_input('What type do you want to create (hint choose "classes"): ')

obj = eval(typ + ".creator()")

print obj
print 'obj’s type is', type(obj)
