# Introduction

Before there were smartphones and iPods, there were personal computers,
and before that people didn’t own computers. Instead there were
minicomputers and mainframes owned by organizations that used them for
data processing.

Data processing programs generally involve taking some raw data and
converting it into useful information. So for example a piece of medical
equipment might take raw measurements of some bodily function and
present a dynamic graph of it, or an accounting system might take a raw
record of transactions and produce a series of summary documents like
cash flow statements and balance sheets. From the programmer’s point of
view the challenges usually arise in handling the data and especially
from its occasional absence (due to missing values) or format
inconsistency rather than from tricky algorithms or complicated data
structures. As one former student put it, “it’s a chance to just do
good old-fashioned programming”.

There will be some new techniques to put to work, but they are
straightforward.

-   The first will be more emphasis than we have usually placed on
    recovering from errors. We have largely ignored problems with input
    to our programs because we have been emphasizing their algorithmics.
    Introducing a lot of error checking code, which can be verbose,
    would have obscured the algorithm details we needed to focus on.

-   Since we were not trying hard to catch data-based errors we didn’t
    have to tell anybody about them. Doing so however raises some issues
    in interacting with the user.

This week and again in the coming weeks we’ll consider a few real-world
situations requiring data processing.
