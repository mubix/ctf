# Roll Call

## Points 25

Using the westridge database, submit the full name of the last student that appears in the "students" table.

Format: First MI. Last
Example: John M. Smith

You are limited to 10 attempts.

## Answer

Shaniya F. Gould

- login to database c.f. #sql task:Tables

```
mysql> SELECT CONCAT(firstName,' ',middle,'. ',lastName) AS fullName FROM students ORDER BY studentID DESC LIMIT 1;
+------------------+
| fullName         |
+------------------+
| Shaniya F. Gould |
+------------------+
1 row in set (0.44 sec)
```
