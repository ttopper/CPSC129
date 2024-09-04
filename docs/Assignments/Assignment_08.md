# Assignment 8

## Problems

1.  (*10 marks*) At Yukon University numerical grades are converted to
    letter grades using a conversion chart as follows:

      ----------------- --------------
      Numerical Grade   Letter Grade
      95-100            A+
      86-94             A
      80-85             A-
      75-79             B+
      70-74             B
      65-69             B-
      62-64             C+
      58-61             C
      55-57             C-
      50-54             D
      0-49              F
      ----------------- --------------

    Write a Python cgi script that enables the user to enter their
    numerical grade and then displays the equivalent letter grade. For
    example on a first visit to the script’s URL
    (`http://localhost:8080/cgi-bin/a8p1.py`) they might see,

    [a8p1_input.html](a8p1_input.html)

    And after submitting that form they might see,

    [a8p1_output.html](a8p1_output.html)

2.  (*10 marks*) Write a Python cgi script that will return a quote
    chosen at random from a list of quotes stored in a text file. The
    format of the file should be one quote per line. You can use [this
    sample file](../08.1_CGI/Quotes.txt) if you don’t have a suitable
    file of quotes close to hand, and here is a [sample output
    page](a8p2_output.html) you can use as a model for your output
    (please leave the HTML of the page alone with the exception of
    linking to a different style sheet if you want to alter the
    appearance of the page).

3.  (*10 marks*) Write a Python cgi script that allows the user to
    specify a year and month and extracts and displays the weather data
    for that month in an HTML table. Here is the HTML for [the input
    page](../08.1_CGI/pWeatherServer-input.html) and for [the display
    page](../08.1_CGI/pWeatherServer-output.html). As in 3. above you
    should leave the HTML as is with the exception that you’re free to
    link to a different style sheet if you want to alter the appearance
    of the page. Here’s [the default style
    sheet](../08.1_CGI/pWeatherServer.css). For weather data you can use
    [weather.txt](weather.txt).

4.  (*20 marks*) Modify [maze_6.py](../08.2_Mazes_2/maze_6.py) so that
    the user can try to solve the maze by moving an icon through it as
    described in [this week’s
    notes](../08.2_Mazes_2/01_Interactive_Maze.md).

## Logistics

-   Use the following naming scheme for program files: 
    `a`assignment#`p`problem#name`.py` . So Bob's solution to problem 1 
    on this assignment will be named `a8p1bob.py`.
