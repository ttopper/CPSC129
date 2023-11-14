# Introduction: We just want a list of their email addresses”

This problem is inspired by an actual situation at the Yukon Government:
They wanted to send an email to every employee, and that wasn’t as easy
as you migh expect. The problem is that they can’t easily generate a
list of all their employees _with_ their email addresses (or at least
they couldn’t a couple of years ago). The problem is that the employee
name and id number is kept in one database system (PeopleSoft), while
their email addresses and network logins are maintained in another (an
Active Directory repository). Having two database systems is not
necessarily a problem, but in this case it is because the two databases
do not have a shared field. This makes it difficult to combine them and
generate a list of employee names and email addresses. (In relational
database terms we would like to do a _join_ on the two tables, but
can’t because they do not have a shared field, specifically one that is
a *primary key* field in one table and a *foreign key* field in the
other. There’s your jargon for the day.)

We can extract records like this from PeopleSoft,

  --------- ------------
  ID        Name
  0047281   Tim Topper
  \...      \...
  --------- ------------

and ones like this from Active Directory,

  ------------ ----------------------
  YNET Login   EMail
  ttopper      tim.topper@gov.yk.ca
  \...         \...
  ------------ ----------------------

but we want to generate ones like this that combine a field from each
table.

  ------------ ----------------------
  Name         email
  Tim Topper   tim.topper@gov.yk.ca
  \...         \...
  ------------ ----------------------

Do you see a pattern? Doesn’t it make you want to automate the solution
to this problem?
