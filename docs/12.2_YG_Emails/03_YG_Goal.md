# Your Goal

Your job is to write a Python program that will take two text files
(e.g. [peoplesoft.txt](peoplesoft.txt) and
[activedirectory.txt](activedirectory.txt)) containing data exported
from each system and attempt to resolve the entries in them. You should
output a list of matches sorted in descending order by match quality,
where the possible quality values should include likely match”,
possible match”, and unmatched”,

| Name               | Email                   | Match quality  |
|--------------------|-------------------------|----------------|
| Tim Topper         | tim.topper@gov.yk.ca    | Likely Match   |
| Michael Smith      | michael.smith@gov.yk.ca | Likely Match   |
| Robert Timms       | bob.timms@gov.yk.ca     | Possible Match |
| Michael Smith      | mike.smith@gov.yk.ca    | Possible Match |
| Marlene Trent      | Unmatched               |                |
| helpdesk@gov.yk.ca | Unmatched               |       

Due to the complications we cannot automate the entire process, but with
around 5,000 employees if our program can match 80% of them with
confidence we have saved someone a lot of manual work.
