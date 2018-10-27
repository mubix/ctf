# Combo Attack

## Points 200

Using the westridge database, submit the name of the teacher that has an "a" in their first name, an "o" in their last name, and works in the Mathematics department.

Format: First MI. Last
Example: John M. Smith

You are limited to 10 attempts.

## Answer

Stanley W. Leon

- login to database c.f. #sql task:Tables

```
mysql> SELECT CONCAT(firstName,' ',middle,'. ',lastName) AS fullName FROM teachers WHERE firstName LIKE '%a%' AND lastName LIKE '%o%' AND deptID IN (SELECT deptID FROM departments WHERE deptName = 'Mathematics');
+-----------------+
| fullName        |
+-----------------+
| Stanley W. Leon |
+-----------------+
1 row in set (0.33 sec)
```
