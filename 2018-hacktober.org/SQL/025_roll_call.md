# Roll Call

## Points 25

Using the westridge database, submit the full name of the last student that appears in the "students" table.

Format: First MI. Last
Example: John M. Smith

You are limited to 10 attempts.

## Answer

Shaniya F. Gould

* username + password from #pwn task:Cracked

```
$ mysql -h 104.248.119.92 -P 666 -u westridge -p123456789 westridge
mysql> SELECT firstName,middle,lastName FROM students ORDER BY studentID DESC LIMIT 1;
+-----------+--------+----------+
| firstName | middle | lastName |
+-----------+--------+----------+
| Shaniya   | F      | Gould    |
+-----------+--------+----------+
1 row in set (0.48 sec)
```
