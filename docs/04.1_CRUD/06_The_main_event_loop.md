# The main event loop

You've already seen it. Go back to the previous page and look at the
controller code. See the main loop that awaits an event from the user to
trigger each action? That's a *main event loop*. It's the most common
pattern for interactive (as opposed to batch) programs. They wait for
each event or user action, e.g. a keypress or a mouse movement, and then
trigger an action based on it. Most office productivity programs (word
processors, spreadsheets, etc.) spend almost all of their time waiting
for the user to do something and then just follow a clear set of rules
to determine what routine to fire as a result. "The main event loop"
is just jargon, not a deep idea, but it's jargon you should know, and
even use, e.g. in interviews.


