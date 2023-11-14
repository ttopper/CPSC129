# A Report Generation Problem

Vast amounts of data are stored in the world’s computer systems. Making
that data accessible is a first step to solving many problems we face,
but humans are poor data processors. On the other hand we are excellent
information processors. A first step in making data meaningful to people
is to transform it into information. This begins with formatting it for
viewing, and progresses through visualizations which let us see at a
glance what the data is saying, to interactive simulations that let us
ask what-if questions and play out scenarios.

I apologize if I’ve got you excited thinking about visualizations and
simulation, because in this unit we’re going to work on the more
prosaic first step: Neatly tabulating and summarizing raw data.

What we have is a file whose contents are formatted like this,

    Asia:Japan:120:144
    North America:Mexico:78:762
    Europe:England:56:94
    Asia:USSR:275:8649
    Europe:Germany:61:96
    South America:Brasil:134:3286
    North America:USA:237:3615
    Asia:China:1032:3705
    North America:Canada:25:3852
    Europe:France:55:211
    Asia:India:746:1267

but what we’d like is a report that looks like this:

    CONTINENT       COUNTRY    POPULATION       AREA       POP. DEN.
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
                    Total          134          3286

You can see that it is much easier to scan the report and answer
questions about the data than it is to scan the raw data file. The
report has organized the data hierarchically from continent to country,
and alphabetized the output by continent and country (helpful when
looking for values in longer lists than we have here). In addition it
has computed totals by continent, and population densities by country,
and included those in the report enriching the raw data.

