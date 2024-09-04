# hockey_player.py
#
# BUGS:
#
# - HTML:
#   Floating the picture left doesn't play well with the containing
#   div since it takes the image out of the normal flow, so it
#   doesn't get bordered.
#
# Version 0 (archived as Quote_0.py)
#
# - Initial roughing out by modifying quote.py
# - Delete console routines.

def HTML_factory(form_dict):
    '''Builds a Quote from the data returned in the form
    CREATION_FORM.'''
    name = form_dict[b'name'].decode('utf-8')
    goals = form_dict[b'goals'].decode('utf-8')
    image = form_dict[b'image'].decode('utf-8')
    return Hockey_player(name, goals, image)

# Use this template for both creation via POST and update via PUT.
CREATION_FORM = '''
<h1>Create form</h1>

<div> 
    <form method="POST" action="http://localhost/create/hockey_player">
        <input type="hidden" name="_method" value="POST" />
        <label for="name">Name:</label><input type="text" id="name"
        name="name" size="50" /><br /> 
        <label for="image">Image:</label><input type="text" id="image"
        name="image" size="50" /><br /> 
        <label for="goals">Goals:</label><input type="text" id="goals"
        name="goals" size="50" /><br /> 
        <label for="method">&nbsp;</label> 
        <input type="submit" value="Create" />
    </form> 
</div> 
'''

UPDATE_TEMPLATE = '''
<h1>Update form</h1>

<div> 
    <form method="POST" action="http://localhost/create/hockey_player">
        <input type="hidden" name="_method" value="POST" />
        <label for="name">Name:</label><input type="text" id="name"
        name="name" size="50" value="%s"/><br /> 
        <label for="image">Image:</label><input type="text" id="image"
        name="image" size="50"  value="%s"/><br /> 
        <label for="goals">Goals:</label><input type="text" id="goals"
        name="goals" size="50"  value="%s"/><br /> 
        <label for="method">&nbsp;</label> 
        <input type="submit" value="Create" />
    </form> 
</div> 
'''

HTML_TEMPLATE = '''
<div> 
      <p><img style="float:left; padding-right: 20px;" src="%s" width="100" />
      <span class="player-name"><em>%s</em></span><br /> 
      <span class="goals">%s career goals (regular season plus playoffs).</span>
      </p> 

    <!-- View this object alone. -->
    <form method="GET" action="http://localhost/%s" class="view"> 
      <input type="submit" value="View" />
    </form>

    <!-- Request the update form for this object. -->
    <form method="GET" action="http://localhost/%s/HTML_update_form" class="update">
      <input type="submit" value="Update" />
    </form>

    <!-- Delete this object. -->
    <form method="POST" action="http://localhost/%s" class="delete">
      <input type="hidden" name="_method" value="DELETE" />
      <input type="submit" value="Delete" /> 
    </form> 
</div>
'''

class Hockey_player:
    def __init__(self, name, goals='0', image=''):
        self.name = name
        self.goals = goals
        self.image = image
        self.uid = str(hash('Hockey_player' + self.name))

    def __str__(self):
        return '[%s] %s: %s career goals. Image at: %s' % (self.uid, self.name, self.goals, self.image)

    def HTML(self):
        return HTML_TEMPLATE % (self.image, self.name, self.goals, self.uid, self.uid, self.uid)

    def HTML_update_form(self):
        return UPDATE_TEMPLATE % (self.name, self.image, self.goals)

if __name__ == '__main__':
    def bordered(s):
        return len(s)*'='+'\n'+s+'\n'+len(s)*'-'
    
    print(bordered('Testing __init__() and __str__()'))
    p = Hockey_player( 'Gordie Howe', '1071', 'http://www.doubleextrapoint.com/images/stories/gordie-howe-puck.jpg')
    print('The Hockey_player p is:')
    print('\t', p)
    print()

    print(bordered('Testing HTML()'))
    print('Here’s the HTMl representation of p:')
    print(p.HTML())
