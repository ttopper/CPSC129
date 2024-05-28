# O(log _n_) versus O(_n_)

To get a sense of how much better this is let’s compare the rate of
growth of O(_n_) and O(log _n_) as _n_ goes from 1 to 1,000,000. I’ll
use a logarithmic scale for _n_ so that the table won’t get too long!
The ratio in the rightmost column tells us how many times slower O(_n_)
is than O(log _n_).

  _n_        |O(log<sub>2</sub>_n_)   | O(_n_)     |  O(_n_) / O(log<sub>2</sub>_n_)
  -----------|---------------|------------|------------------------
  1          | 1             | 2          | 2
  4          | 2             | 4          | 2
  8          | 3             | 8          | 2.7
  16         | 4             | 16         | 4
  32         | 5             | 32         | 6.4
  64         | 6             | 64         | 10.7
  128        | 7             | 128        | 18
  256        | 8             | 256        | 32
  512        | 9             | 512        | 57
  1,024      | 10            | 1,024      | 102
  2,048      | 11            | 2,048      | 186
  4,096      | 12            | 4.096      | 341
  8,192      | 13            | 8,192      | 630
  16,384     | 14            | 16,384     | 1,170
  32,768     | 15            | 32,768     | 2,185
  65,536     | 16            | 65,536     | 
  262,144    | 18            | 262,144    | 14,564
  524,288    | 19            | 524,288    | 27,594
  1,048,576  | 20            | 1,048,576  | 52,429

The striking result is that for moderate sized problems O(log _n_) is
**thousands of times faster** than O(_n_)!

Perhaps more surprising to you will be the news that many problems would
love to have a O(_n_) solution, but don’t because the best known
solutions are worse than O(_n_)!

What other orders are there? Order _n_ and order log _n_ are both common
algorithmic orders, but others include O(1), O(_n_<sup>2</sup>), O(_n_<sup>3</sup>), O(_n_
log _n_), O(2<sup>_n_</sup>), and O(_n_!). This [spreadsheet](AlgorithmOrders.xls) helps 
illustrate the differences.
