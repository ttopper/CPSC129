# Unifying the input form and the processing script

At the moment we have to manage, and keep track of, and keep in sync,
two different files: the HTML input form and the processing script.
However taking advantage of the ability of programs to do selection we
can combine these two into a single file that can select the appropriate
response based on what is passed to the script. If the `FieldStorage`
instance has content then it was the result of a user filling out the
form and pressing `Submit`, and we should process the data. On the other
hand if the `FieldStorage` instance is empty it means no form has been
filled out (perhaps because they are coming directly to this URL from a
link or a search result) and we should present the form to the user. In
code this looks like this:

``` python
# mi2km_v3.py
#
# Demonstrates unified cgi script that detects whether request
# is:
# 1) from a completed form, or
# 2) a first time visit.
import cgi

# We read the templates in from external files because
# that makes them easier to create. You, or your web designer,
# can create complete HTML pages in your editor of choice
# and then you just replace the values to be interpolated for
# with appropriate format codes.
output_template = open("mi2km_output_v3.html","r").read()
input_template = open("mi2km_input_v3.html","r").read()

# Parse the CGI request into dictionary-like FieldStorage.
form = cgi.FieldStorage()

if 'miles' in form:
    # If they filled in the miles field, convert miles to km,
    miles = float( form['miles'].value )
    km = miles * 1.609
    # and display the output.
    print('Content-type: text/html\n')
    print(output_template % (miles, km))

elif 'km' in form:
    # If they filled in the km field, convert km to miles,
    km = float( form['km'].value )
    miles = km / 1.609
    # and display the output.
    print('Content-type: text/html\n')
    print(output_template % (miles, km))

else:
    # They filled in neither field so give them an input form to fill out.
    print('Content-type: text/html\n')
    print(input_template)
```

## Notes:

-   If you look carefully at
    [mi2km_output_v3.html](mi2km_output_v3.md) you will see that one
    common hack is required. % signs in CSS need to escaped, i.e.
    replaced with %% so the Python string interpolation mechanism won’t
    interpret them as formatting fields. This is usually avoided by
    importing the CSS file instead of inserting the styles into the HTML
    file (which is best practice, but I wanted to avoid a veritable
    explosion in the number of files we had to keep track of).
