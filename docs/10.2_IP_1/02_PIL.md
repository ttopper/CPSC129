# PIL: The Python Imaging Library

If we want to work with an image the first job is to read it in.
Thinking back to the Game of Life you can probably imagine that there
are multiple ways of storing an image on disk, and you’d be right.
Common formats include PNG, JPEG, BMP and GIF but there are many more
(e.g. [Wikipedia lists around
70](http://en.wikipedia.org/wiki/List_of_file_formats#Graphics)). We
don’t want to write low level code to read even one format, much less
70, so we’ll use a library to do that for us. Python has more than one
option, but we’ll use the [Python Imaging Library (PIL
)](http://www.pythonware.com/products/pil/). This means you’ll need to
install it.

For Windows this is a simple process of downloading the appropriate
binary file and running it. Appropriate here means the one matching your
Python version.

For Linux, use your package manager, it will know all about PIL.

For Mac I am unsure. Some online sources say PIL is already included in
the standard python distribution, others give installation instructions.
I don’t have a Mac to test, but hopefully [these search
results](https://www.google.ca/search?q=installing+python+PIL+on+mac+osx&aq=f&oq=installing+python+PIL+on+mac+osx&aqs=chrome.0.57j0l3.9231j0&sourceid=chrome&ie=UTF-8)
will guide you.

You’ll know you have successfully installed it when this one-line
program runs without error:

``` python
from PIL import Image
```

These notes will show you the subset of PIL operations we’ll be using
but if you want to explore the [Python Imaging Library
Handbook](http://www.pythonware.com/library/pil/handbook/index.htm) is
quite thorough. PIL is a small” library, but we’ll barely scratch
the surface of what it offers.

 

