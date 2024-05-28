# Text versus Binary Files

Files on disk are always just sequences of bytes so how can there be two
types, text and binary? The difference between text and binary files is
not a physical difference on disk, but a difference in the way those
bytes are_interpreted_

Consider storing the two dimensional coordinate (12, 31) to disk.
Storing it as text would be in essence to print it to a file (instead of
the screen). We can visualize the file contents to be,

<pre>   -------------------------
  | 1 | 2 | , | 3 | 1 | EOF |
   -------------------------</pre>

where EOF is the character used to mark the end of a file. (The actual character
used for the end of file marker is operating system dependent.) Of
course what is actually written to disk are the ASCII values of those
characters, so what is on disk is,


  49   50   44   51   49   26
 

To be even more precise the values will be stored in binary so the disk
contents will be,

  00110001   00110010   00101100   00110011   00110001   00011010

Thank goodness the computer can read it!

What about storing it in a binary file? In this case we will write the
binary representations of the numbers 12 and 31 to disk in sequence. The
number of bytes used to do this on disk varies from 1 to 8, but using
typical four byte representations we would write the following to disk:

  ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
  00000000   00000000   00000000   00001100   00000000   00000000   00000000   00011111   00011010
  ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------

As you can see both files have binary representations on disk so why do
we call the first text and only the second binary? Because to be
meaningful each should be _interpreted_ differently. We call the first a
text file because its bits should be interpreted as giving the ASCII
values of **text** characters. We call the second binary because its bits
should be read in four bytes at a time and interpreted as integer
values. Notice that it doesn't say this inside the files. That
knowledge has to be built into the suite of programs that create and
manipulate the files.

Note that either representation could be read in as either text, i.e. a
sequence of bytes corresponding to ASCII codes of characters, or binary,
i.e. a pair of 4-byte wide integers, but that in each case the wrong
interpretation produces nonsense. _So_ knowing the correct
interpretation is crucial. In everyday computing you can often tell
which interpretation is correct by displaying some of the file to a
terminal, or opening it in a 'pure' text editor, e.g. the IDLE editor.
Here's a dump of a small Python program to a terminal,

    ttopper@D1JWYSB1:~/Present/CPSC128.W13/08_Persistence
    $ cat s2bin.py
    # s2bin.py
    # Converts from a string to its binary representation.
    HEXBIN ={"0":"0000", "1":"0001", "2":"0010", "3":"0011", "4":"0100",
             "5":"0101", "6":"0110", "7":"0111", "8":"1000", "9":"1001",
             "A":"1010", "B":"1011", "C":"1100", "D":"1101", "E":"1110",
             "F":"1111"}
    s = '112,31'
    for c in s:
        n = ord(c)
        print() "".join([HEXBIN[i] for i in '%X'%n]) )
    ttopper@D1JWYSB1:~/Present/CPSC128.W13/08_Persistence
    $

And here's a partial dump of an MS Word document,

    ttopper@D1JWYSB1:~/Present/CPSC128.W13/08_Persistence
    $ cat MSWordFile.doc
    DI◄à¡±→á                > ♥ _ÿ   ♠           ☺   *        ►  ,   ☺   _ÿÿÿ    ) ÿ
    ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ
    ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ
    ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ
    ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ
    ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ
    ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿì¥A %`   ♦  d↕¿      ►     ♠  / ♫ bjbjNàNà      ♦
    ▬ .►  ,S☺ ,S☺ /                               ÿÿ          ÿÿ          ÿÿ       ☼
         ☼♥      ☼♥  ☼♥      ☼♥      ☼♥      ☼♥      ☼♥  ¶           ,♥      ü♥    ü
    ♥      ü♥      ü♥  ♀  ♦  ♀   ,♥      ♀♠  o    ♦       ♦       ♦       ♦       ♦û
    ♦      û♦      û♦      <♣  ☻   ?♣      ?♣      ?♣      ?♣      ?♣      ?♣  $   ♦
      h☻  l   ª   ±♣  §                   ☼♥      û♦                      û♦      û♦
          û♦      û♦      ±♣              ☼♥      ☼♥       ♦               ♦  U   Æ♣
      ▬   #♣      #♣      #♣      û♦
       ☼♥       ♦      ☼♥       ♦      <♣              #♣                          û
    ♦      <♣              #♣              #♣      ☼♥      ☼♥                      #
    ♣       ♦      ¶♦  ♀   `l"._AÉ☺        ü♥      ♣
       #♣              <♣      Ü♣  0   ♀♠      #♣      ▬
           ♣
       ▬
          #♣                                                                       ▬
                  ☼♥      #♣  h   û♦      û♦      #♣      û♦      û♦               û
    ♦      û♦      û♦      ±♣      ±♣                                      ↓♣
                                       û♦      û♦      û♦      ♀♠      û♦      û♦  û
    ♦      û♦              ,♥      ,♥      ,♥  D   ü♥      ,♥      ,♥      ,♥      ü
    ♥      ,♥      ,♥      ,♥      ☼♥      ☼♥      ☼♥      ☼♥      ☼♥      ☼♥      ÿ
    ÿÿÿ    ☻ ♀☺                                                                    T
    his is a very simple one line word document.                                   ♠
      ♫   § - . / oéoYoOo                                                          ¶

As you can see it is easy to tell which file is a text file and which
binary (though if you look toward the bottom of the dump of the word
file you can see some text content).


