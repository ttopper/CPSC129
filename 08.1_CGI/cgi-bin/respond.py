# respond.py
import cgi

first_time = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
        "http://www.w3.org/TR/html4/strict.dtd">
<html>
  <head>
    <title>respond.py output</title>
  </head>
  <body>
    <p>Hi %s.</p>
  </body>
</html>'''

response = '''
'''

form = cgi.FieldStorage()
print('Content-type: text/html\n')
print(first_time % (form['user'].value))

