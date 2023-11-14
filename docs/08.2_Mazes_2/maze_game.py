# maze_game.py

set the initial maze dimensions
while the user is not finished playing
    generate a maze
    while the current cell is not the exit cell
        # Wait for an event: quit, mouse click or keypress.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                # Get mouse coords.
                # Convert mouse coords to cell coords.
                # (Hint: as in earlier Life GUI program).
            elif event.type == KEYUP:
                # N.B. event contains keypress information
                # Figure out what requested destination cell is.
            if the destination cell neighbours the current cell
               and if there is a door connecting them
                change the current cell location to be the destination cell
            else:
                beep angrily

    play the happy sound
    make the maze fade/dissolve/crumble
    increase the maze dimensions
