# Book Worm

## Points 300

Use the westridge database.

Grades are entered into the database for every assignment that a student completes. Points are based on values 1-100, with 100 being an A+. Add up all of the grade values for each student and determine which student has the highest accumulation of points. Submit the student's full name.

Format: First MI. Last
Example: John M. Smith

You are limited to 10 attempts.

## Answer

Ray M. Gilmore

- login to database c.f. #sql task:Tables

```
mysql> SELECT CONCAT(firstName,' ',middle,'. ',lastName) AS fullName FROM grades JOIN students ON grades.studentID = students.studentID GROUP BY grades.studentID ORDER BY SUM(grade_value) DESC,grades.studentID LIMIT 1;
+----------------+
| fullName       |
+----------------+
| Ray M. Gilmore |
+----------------+
1 row in set (0.32 sec)
```
