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
a _primary key_ field in one table and a _foreign key_ field in the
other. There’s your jargon for the day.)

We can extract records like this from PeopleSoft,

<table style="margin: 1em auto;" border="1">
  <tbody>
    <tr>
      <th>ID</th>
      <th>Name</th>
    </tr>
    <tr>
      <td>0047281</td>
      <td>Tim Topper</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table>
and ones like this from Active Directory,

<table style="margin: 1em auto;" border="1">
  <tbody>
    <tr>
      <th>YNET Login</th>
      <th>EMail</th>
    </tr>
    <tr>
      <td>ttopper</td>
      <td>tim.topper@gov.yk.ca</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table>
but we want to generate ones like this that combine a field from each
table.

<table style="margin: 1em auto;" border="1">
  <tbody>
    <tr>
      <th>Name</th>
      <th>email</th>
    </tr>
    <tr>
      <td>Tim Topper</td>
      <td>tim.topper@gov.yk.ca</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table>

Do you see a pattern? Doesn’t it make you want to automate the solution
to this problem?
