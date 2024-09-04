# pillow: The Python Imaging Library

If we want to work with an image the first job is to read it in.
Thinking back to the Game of Life you can probably imagine that there
are multiple ways of storing an image on disk, and you’d be right.
Common formats include PNG, JPEG, BMP, and GIF but there are many more
(e.g. [Wikipedia 
list](http://en.wikipedia.org/wiki/List_of_file_formats#Graphics)). We
don’t want to write low level code to read the format, so we’ll use a
library to do that for us. Python has more than one option, but we’ll
use the [Python Imaging Library (pillow)](https://pypi.org/project/pillow/).
This means you’ll need to install it using pip: `pip install pillow`.

You’ll know you have successfully installed it when this one-line
program runs without error:

``` python
from PIL import Image
```

These notes will show you the subset of pillow operations we’ll be using
but if you want to explore the [Python Imaging Library
Handbook](https://pillow.readthedocs.io/en/stable/handbook/index.html)
is quite thorough. PIL is a “small” library, but we’ll barely scratch
the surface of what it offers.

 

