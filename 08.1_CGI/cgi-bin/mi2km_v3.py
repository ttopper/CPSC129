# mi2km_v3.py
# NCIT 212 Winter 2010
#
# Demonstrates unified cgi script that detects whether request
# is:
# 1) from completed form, or
# 2) first time.
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
