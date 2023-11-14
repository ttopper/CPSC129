# a8_4.py

RESULT = '''CONTINENT       COUNTRY    POPULATION       AREA       POP. DEN.
                          (,000,000s)   (,000s MI^2)  (POP./MI^2)

Asia            China         1032          3705         278.5
                India          746          1267         588.8
                Japan          120           144         833.3
                USSR           275          8649          31.8
                              ----         -----
                Total         2173         13765

Europe          England         56            94         595.7
                France          55           211         260.7
                Germany         61            96         635.4
                              ----         -----
                Total          172           401

North America   Canada          25          3852           6.5
                Mexico          78           762         102.4
                USA            237          3615          65.6
                              ----         -----
                Total          340          8229

South America   Brasil         134          3286          40.8
                              ----         -----
                Total          134          3286'''

def summarize(fname):
    # Put your code here. You shouldn't need to change outside this function.
    return ''
    
if __name__ == '__main__':
    filename = raw_input('What file would you like summarized? ')
    if summarize(filename) != RESULT:
        print 'Sorry you’re not there yet. Keep trying.'
    else:
        print 'You got it! You’re done.'
