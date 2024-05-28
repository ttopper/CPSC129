# Unique identifiers

## Summary

> Systems often need ways to uniquely identify individual objects, e.g.
> employees are identified by employee numbers, people by SINs, books by
> ISBNs. Generating them automatically while ensuring they are unique is
> a difficult task, but one that has been studied in depth by computer
> scientists. Python provides the `hash()` function which can hash
> strings and numbers. We can use this to generate uid’s for objects by
> building a unique string representing the object and then hashing it.

## The idea

In the everyday world most uid’s are numbers (but not all, e.g. license
plates). These can be generated automatically by converting the object
data into numerical form and then using arithmetic operations to
generate a number in the desired range, e.g.

> In the SHA-1 algorithm, for example, the domain is flattened” and
> chopped” into words” which are then mixed” with one another
> using carefully chosen mathematical functions. The range (hash
> value”) is made to be a definite size, 160 bits (which may be either
> smaller or larger than the domain), through the use of modular
> division.[[^*](http://en.wikipedia.org/wiki/Hash_function)

(Note that the size of the desired range corresponds to the largest
number of objects you will be able to uniquely identify. Note also the
use of modulo %)

For example to assign uid’s to strings we could take the index of each
string letter in the alphabet and add these values up. For example
’cab’ would be assigned the number 6 because the positions of the
letters c, a and b in the alphabet are 3, 2 and 1 respectively. The
obvious flaw in this simple system is that anagrams will all be assigned
the same id.

We can improve it by differentiating the id values by using information
about the positions of the letters in the string, e.g. by raising each
letter’s index value to the power of its position in the string. In
this case ’cab’ gets assigned the id 3<sup>1</sup> + 1<sup>2</sup> + 2<sup>3</sup> = 12. Note
that this is not the same as any of cab’s anagrams, e.g. the id of
’abc’ is 1<sup>1</sup> + 2<sup>2</sup> + 3<sup>3</sup> = 32. (Whether all strings are guaranteeed
to have a unique id in this scheme is an interesting, but difficult
question we will not pursue in this course.)

Here’s some Python code implementing this scheme,

```python
import string

s = 'cab'
uid = 0
for i in range(len(s)):
    uid += (string.ascii_letters.index(s[i])+1) ** (i+1)
print(uid)
```

One problem with this scheme is that the id numbers get large quickly as
the string gets longer because of the exponentiation operation, e.g. the
id for ’Yabbadabbadoo’ is 2075941410449291L! This is worked around in
practice by reducing the number arithmetically by e.g. modulo operations
or bitwise ’folding’ of the number. (Note the use of modulo again.
That strange operation you learned in CPSC 128 turns out the be very
useful).

## Jargon

Functions that generate uids are called hash functions:

> A hash function is a reproducible method of turning some kind of data
> into a (relatively) small number that may serve as a digital
> fingerprint” of the data. The algorithm chops and mixes” (i.e.,
> substitutes or transposes) the data to create such
> fingerprints.<sup>[*](http://en.wikipedia.org/wiki/Hash_function)</sup>

One common place hash functions are encountered is in checksum’s used
to validate the contents of downloaded files, e.g. SHA1, SHA2 and md5sum
checksums.

> md5sum is a computer program which calculates and verifies 128-bit MD5
> hashes, as described in RFC 1321. The MD5 hash (or checksum) functions
> as a compact digital fingerprint of a file. It is extremely unlikely
> that any two non-identical files will have the same MD5 hash (although
> it is certainly possible). Because almost any change to a file will
> cause its MD5 hash to also change, the MD5 hash is commonly used to
> verify the integrity of files (i.e., to verify that a file has not
> changed as a result of file transfer, disk error, meddling,
> etc.).<sup>[*](http://en.wikipedia.org/wiki/Md5sum)</sup>

## Practical implementation

In fact however it is difficult to design a uid generator (or hashing
scheme as they are called) that assigns unique uids. And since others
have already done that work, we’ll build on it. Python has a built-in
function called `hash` that can hash numbers and strings, e.g.

    >>> hash('tim')
    333309873
    >>> hash('shelly')
    1348423469
    >>> hash('misha')
    -1866883155
    >>> hash('Misha')
    527638157
    >>> hash(42)
    42

**Note** that while `hash()` will return values for all Python objects,
apart from strings and numbers these will not usually be uids, but
simply internal ids that will vary from one computer to another and even
one run of the program to another. For other object types we can first
create a string that uniquely represents the object and then hash the
string to get a compact, unique key. For example for our quote class we
can concatenate the class name, author name and quote text, and hash the
resulting string,

```python
    def  uid(self):
            return hash('Quote' + self.author + self.text)
```