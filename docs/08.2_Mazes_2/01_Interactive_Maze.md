# An Interactive Maze

A couple of weeks ago we wrote code to create mazes. Let’s add code so
that people can try to solve them. We’ll modify [maze_6.py](maze_6.py)
so that our users can try to solve it by moving an icon (perhaps our
standby Aqua-Ball-icon.png: ![](Aqua-Ball-icon.png) through it. They
should be able to control the icon with either the mouse (by clicking in
the cell they want it to move to) or the arrow keys (to try and move it
up, down, left or right). The program should prevent them from moving
the icon through walls, and should be able to tell when they have won
and maybe play a triumphant sound --- or at least beep (cheerfully
rather than gratingly!).

The pseudocode is fairly straightforward:

    clock = pygame.time.Clock() # See Note 1.
    set the initial maze dimensions
    while the user is not finished playing
        generate a maze
        while the current cell is not the exit cell
            # Wait for an event: quit, mouse click or keypress.
            event = pygame.event.wait(): # See Note 2.
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                Get mouse coords.
                Convert mouse coords to cell coords.
                (Hint: as in earlier Life GUI program).
            elif event.type == KEYUP:
                N.B. event contains keypress information
                Figure out what requested destination cell is.
            if the destination cell neighbours the current cell
               and if there is a door connecting them
                change the current cell location to be the destination cell
                move the player icon from the old cell to the new one
            else:
                beep chidingly # See Note 3.
            clock.tick(20) # Adjust parameter to suit.

        play the happy sound # See Note 3.
        make the maze fade/dissolve/crumble # See Note 4.
        increase the maze dimensions

Notes:

1.  [`pygame.time.Clock()`](http://www.pygame.org/docs/ref/time.html#pygame.time.Clock)
    is used because this is not a fast action game where we want every
    CPU resource available going to monitor events from the user.
    Instead we’d like this program to get along with the other programs
    running on our computer and give them a chance to get things done as
    well. We’ll use the `.tick()` method to tell pygame to take
    timeouts during its processing. You’ll want to adjust the parameter
    to `tick()` so that Pygame resource usage does not spike, while
    keeping the game responsive.

2.  Similarly, we’ll use `pygame.event.wait()` both so that our program
    will get along well with others, and so that our program will only
    ever handle one event per main event loop. According to [the pygame
    documentation](http://www.pygame.org/docs/ref/event.html#pygame.event.wait)
    it: "Returns a single event from the queue. If the queue is empty
    this function will wait until one is created. The event is removed
    from the queue once it has been returned. While the program is
    waiting it will sleep in an idle state. This is important for
    programs that want to share the system with other applications.”

3.  You play a sound by loading it which creates a [sound
    object](http://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Sound)
    and then invoking the object’s play method,

        sound = pygame.mixer.Sound(filename)
        sound.play()

    This bit of code assumes `filename` exists, and can be opened, and
    interpreted as a sound file. You might be interested to see how the
    code changes if we add typical safety checks to it using [Python
    exceptions](../09.2_Data_Processing/05_Python_exceptions.md),

    ``` python
    def load_sound(name):
        # Define a dummy class that behaves enough like a Sound object
        # that the rest of the game will still run.
        class NoneSound:
            def play(self): pass
        # Check that pygame.mixer was imported successfully.
        if not pygame.mixer:
            return NoneSound()
        # Now try loading the sound file.
        try:
            sound = pygame.mixer.Sound(name)
        except:
            print('Cannot load sound:', name)
            raise SystemExit
        return sound

    sound = load_sound(filename)
    ```

    There are lots of sources for .wav files on the internet, but a
    small one with a decent selection for small programming projects for
    the undiscriminating user is
    <http://www.mediacollege.com/downloads/sound-effects/>. I use it
    because it is small, and the sound effects are free to download.

4.  You can fade the maze away by redrawing it in increasingly dim
    colours. You could dissolve it by randomly removing walls until
    there are none left. Crumbling the maze is left as a challenge.

Enhancements are possible and will be tested with great relish. For
example,

-   You could make it easier to solve (and more visually interesting) by
    highlighting the path the user has taken so far (this is simple
    until they back up, when you have to unhighlight the path you have
    previously highlighted).

-   You can make it much harder by giving them a time limit and moving
    them back to the entrance when the time limit expires.

-   You could provide a limited number of explosive charges so they can
    blast walls out of the way.

-   Very cool, but very subtle to program, you could have walls change,
    that is replace some walls with doors and vice versa. The tricky
    business is changing things so that there always remains some path
    to the exit (it’s easy to block your player in).

-   ...your imagination is the only limit!
