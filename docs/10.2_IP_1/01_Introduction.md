# Introduction

For our last problem domain of the term, we’ll take a look at image
processing. Not a formal introduction to digital image processing, since
to do that justice would take more mathematical background that you have
at the moment. Instead we’ll cherry pick a few interesting problems
that are also accessible.

A digital image is a two-dimensional array of pixels. Pixel stands for
“picture element”, and each pixel represents one point of light. There
a lot of possible ways of describing a point of light. Physics students
might think of wavelength and amplitude, but digital systems have taken
their lead from the human visual system which has receptors for
different wavelengths of light, and commonly represents them using the
magnitudes of their red, green and blue components. Thus each pixel can
be represented by a three-tuple: (R, G, B). We’ll simplify things
further and only work with “black and white” (actually grey scale, or
monochrome) images, so our pixels will be represented by a single number
giving their brightness or luminance.

 

