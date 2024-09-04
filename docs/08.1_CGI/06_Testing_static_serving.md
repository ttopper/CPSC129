# Testing static serving

Go ahead:

1.  Put an HTML file in the same directory as `httpserver.py`. If you
    don’t have an HTML file handy right-click on this page and save it
    to that directory.

2.  Double-click on `httpserver.py` to run it. We are running it by
    double-clicking because we don’t want to run it interactively,
    since we want it to keep running daemon-style while we work on our
    other code. Double-clicking the icon for `httpserver.py` in Windows
    Explorer (NOT Internet Explorer) will start it running and display
    its log messages in a console window.

3.  Type the URL `http://localhost:8080/yourhtmlfilename.html` in your
    browser address bar. The contents of the HTML file should be
    displayed in your browser. If not, get in touch and we’ll try to
    debug it.

4.  When you are finished, stop the program by closing the console
    window.