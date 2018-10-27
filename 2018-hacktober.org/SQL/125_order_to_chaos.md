# Order to Chaos

## Points 125

Using the westridge database, submit the full name of the first student after sorting the database alphabetically by last name.

Format: First MI. Last
Example: John M. Smith

You are limited to 10 attempts.

## Answer

Leanna F. Abbott

- login to database c.f. #sql task:Tables

```
mysql> SELECT CONCAT(firstName,' ',middle,'. ',lastName) AS fullName FROM students ORDER BY lastName,studentID DESC LIMIT 1;
+------------------+
| fullName         |
+------------------+
| Leanna F. Abbott |
+------------------+
1 row in set (0.29 sec)
```
