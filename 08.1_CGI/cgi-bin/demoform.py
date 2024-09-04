# demoform.py
import cgi

template = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
        "http://www.w3.org/TR/html4/strict.dtd">
<html>
  <head>
    <title>demoform.py output</title>
    <style>em { color: #dc1436; }</style>
  </head>
  <body>
        <h1>CPSC 129 ~ Object-oriented programming</h1>

        <h2>The common HTML form controls: Output</h2>

        <p>Well, you claim you are a <em>%s</em> named
        <em>%s</em> whose favourite
        programming language is <em>%s</em> and who likes
        <em>%s</em>.</p>

        <p>Your message to me was:</p>
        <blockquote><em>%s</em></blockquote>
  </body>
</html>'''

form = cgi.FieldStorage()
sex = form.getvalue('sex')
name = form.getvalue('name')
language = form.getvalue('language')
likes = form.getlist('likes')
likes = ' &amp; '.join(likes)
message = form.getvalue('message')

print('Content-type: text/html\n')
print(template % ( sex, name, language, likes, message))

