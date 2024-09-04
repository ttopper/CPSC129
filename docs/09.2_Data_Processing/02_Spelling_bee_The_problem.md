# Spelling Bee: The Problem

Each year our local telco Northwestel sponsors French and English
spelling bees in Whitehorse. A month or two before the bee students in
the local schools are given word lists (one list per grade) to study.
Later each school holds a spelling bee. The school champions get to
compete in a territory-wide competition.

The format of this competition is fairly straightforward. Students in
each category are asked one at a time to spell a word. If they spell it
correctly, they continue into later rounds. If they spell it incorrectly,
they are eliminated. The process continues until only one speller is
left. Sometimes the best spellers are quite good and the competition
exhausts the words for that grade level. When that happens they use
words from the next grade’s list.

The logistics of running the competition are fairly straightforward, but
also time-consuming and error-prone to complete by hand. Since it is
done manually and in real-time errors are inevitable and in recent years
there have been some problems. It has happened that a word has been
asked of more than one speller which is a problem because the second
student to spell it may have heard it spelled by the first. It has even
happened that a single student has been asked the same word twice.
Computers are good where humans are weak (and vice versa of course):
they are fast and systematic in their processing where we are slow and
unreliable, so the suggestion has been made that the process be
automated. You have been “voluntold” to help them out.

They have given you a text file of the test words
([spelling_list.txt](02_spelling_list.txt)), a CSV (Comma Separated
Value) formatted text file of the contestants generated from the Excel
spreadsheet they are using for results
([spelling_contestants.txt](02_spelling_contestants.txt)), and a sample
of the output they would like for each contestant
([spelling_output.html](02_spelling_output.html)). Your job is to write
a Python program that allows the user to specify the word and contestant
files, and that will then generate an HTML word list for each
contestant. The filenames for the contestants’ word lists should be in
the form `firstinitial_lastname.html` (so the example file name should
really be named `t_topper.html`). The words for each contestant should
be selected randomly from the word list, and no word should be used
twice either for a given contestant or across contestants.
