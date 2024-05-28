# Important note: Files are sequential

One thing that is not illustrated by the examples so far is that files
are sequential. They evolved from physical tape devices that only went
forward, or all the way back to the beginning of the file, so you are
always moving forward through a file as you read from it. Thus after
doing a `.read()` from a file you are at the end of it and doing
another `.read()` will not reread it, e.g.

```plaintext
>>> f = open('text_file.txt','r')
>>> s = f.read()
>>> s
'The first line.\nLine 2.\nThe third and last line.\n'
>>> p = f.read()
>>> p
''
>>> f.close()
>>> 
```

Note that it is not an error to try and read from the end of a file
(notice that there's no error message above), you just don't get
anything because there is nothing more to get (see how `p` is a null
string above?).
