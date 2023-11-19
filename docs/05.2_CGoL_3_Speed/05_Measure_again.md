# Is it better? Measure Again

Are the changes worth making? No guessing! Here are the measurements,

    >>> 
    u_rows = 100
    u_cols = 100
    generations = 100
    live_pct = 42

    total_time    :  0.93
    copying_time  :  0.50 = 53.22%
    aging_time    :  0.44 = 46.78%
    >>> 

That’s around 8 times faster or an 800% speed increase. Well worth
doing. Which you will on the current assignment :-)

(Hmm...I see that while we sped up the aging block we also slowed down
the copying block. This is because we truly _do_ copy now, whereas
before we were renaming and then just allocating new blank memory (see
the footnote on the previous page) without the requirement to loop over
it assigning values, which we do have to do in the new scheme.)
