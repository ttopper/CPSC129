# Example: Searching log files

Suppose as part of a security audit we want to display all the lines
from our web server log file containing the IP address 199.247.232.110.
The file name is `access.log.1` and the first ten lines of the file look
like this,

    66.235.124.20 - - [12/Apr/2009:07:29:25 -0700] "GET /Math130.F05/index.html HTTP/1.1" 200 34928 "-" "Mozilla/5.0 (compatible; Ask Jeeves/Teoma; +http://about.ask.com/en/docs/about/webmasters.shtml)"
    72.30.142.250 - - [12/Apr/2009:07:51:05 -0700] "GET /Math130.F07/BayesProblems.html HTTP/1.0" 200 2812 "-" "Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
    72.30.142.250 - - [12/Apr/2009:07:51:09 -0700] "GET /Math130.F07/130.css HTTP/1.0" 304 - "http://ttopper.yukoncollege.yk.ca/Math130.F07/BayesProblems.html" "Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
    216.126.125.105 - - [12/Apr/2009:08:36:00 -0700] "GET /NCIT210.W09/05_ListsAndStrings/PlayingCards.html HTTP/1.1" 200 20753 "-" "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19"
    216.126.125.105 - - [12/Apr/2009:08:36:22 -0700] "GET /NCIT210.W09/07_Dictionaries/07_Assignment.html HTTP/1.1" 200 5817 "-" "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19"
    199.247.232.110 - - [12/Apr/2009:08:52:10 -0700] "GET /Math101.W09/index.html HTTP/1.1" 304 - "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19"
    199.247.232.110 - - [12/Apr/2009:08:53:00 -0700] "GET /Math101.W09/10-8.html HTTP/1.1" 200 2326 "http://ttopper.yukoncollege.yk.ca/Math101.W09/index.html" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19"
    199.247.232.110 - - [12/Apr/2009:08:53:01 -0700] "GET /Math101.W09/MATH101W08.css HTTP/1.1" 200 737 "http://ttopper.yukoncollege.yk.ca/Math101.W09/10-8.html#25" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19"
    199.247.232.110 - - [12/Apr/2009:08:53:01 -0700] "GET /Math101.W09/10-8-27.jpg HTTP/1.1" 200 24136 "http://ttopper.yukoncollege.yk.ca/Math101.W09/10-8.html#25" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19"
    199.247.232.110 - - [12/Apr/2009:08:53:01 -0700] "GET /Math101.W09/10-8-25.jpg HTTP/1.1" 200 67164 "http://ttopper.yukoncollege.yk.ca/Math101.W09/10-8.html#25" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19"

The file is quite large, 100s of megabytes in size, so we'd rather not
read it all into memory if we can avoid it so we'll use a line at a
time approach. Our pseudocode looks like this,

```plaintext
Get the name of the log file
Get the name of the IP address to scan for
Open the file for reading
For each line in the file
    If the line contains the IP address
        Display the line
```
and in Python we get,

```python
# ip_extractor.py
fname = input('What file do you want to scan? ')
ip = input('What IP address do you want to scan for? ')
f = open(fname, 'r')
for line in f:
    if line.find(ip) != -1:
        print(line)
```

which produces the output,

```plaintext
>>> 
What file do you want to scan? access.log.1
Waht IP address do you want to scan for? 199.247.232.110
199.247.232.110 - - [12/Apr/2009:08:52:10 -0700] "GET /Math101.W09/index.html HTTP/1.1" 304 - "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19"
199.247.232.110 - - [12/Apr/2009:08:53:00 -0700] "GET /Math101.W09/10-8.html HTTP/1.1" 200 2326 "http://ttopper.yukoncollege.yk.ca/Math101.W09/index.html" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19"
199.247.232.110 - - [12/Apr/2009:08:53:01 -0700] "GET /Math101.W09/MATH101W08.css HTTP/1.1" 200 737 "http://ttopper.yukoncollege.yk.ca/Math101.W09/10-8.html#25" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19"
...
```