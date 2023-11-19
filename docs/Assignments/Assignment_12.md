# Assignment 12

## Problems

1.  (_10 marks_) Write a function called `range_set(im, (lo, hi))` that
    will return a modified version of `im` whose [dynamic
    range](../12.1_IP_2/02_Dynamic_range.md) is `[lo, hi]`.

    Don’t forget to include a `main` section that will demonstrate the
    function on an image, e.g. `dkpenguins.png`.

2.  (_10 marks_) Write a function called `median_filter(im)` that will
    apply a 3×3 [median filter](../12.1_IP_2/03_Noise_filtering.md) to
    `im` and return the modified image.

    For testing you should allow the user to apply salt and pepper noise
    to an image at a desired percentage level, output the noisy image,
    i.e. save it to a file, and display the RMSE between the noisy image
    and the original in the IDLE shell. (So yes, I’m really asking you
    to write two aditional functions, `salt_and_pepper(im, percent)` and
    `rmse(im1, im2)`, as well as `median_filter`.)

3.  (_10 marks_) Write a function called `sharpen(im)` that implements
    Laplacian-based image sharpening as described in [the
    notes](../12.1_IP_2/04_Sharpening.md). Here’s [the original moon
    image](../12.1_IP_2/04_Moon.jpg).

    Your main section should of course test it on an image.

4.  (_30 marks_) Write the name to email matching program described in
    [this week’s notes](../12.2_YG_Emails/00_index.md).

## Logistics

-   Use the following naming scheme for your program files:,
    `a`*assignment#*`p`*problem#*`v`*version#*`.py` .
