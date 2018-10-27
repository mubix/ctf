# Full Class

## Points 400

Using the westridge database.

Gh0stf4c3 hackers sent a warning to school faculty that they would erase the grades associated with the session and course that have the highest enrollment of students. Submit the sessionID and courseName of the course with the highest enrollment of students so we know which records they will be targeting.

Format: sessionID courseName num_students
Example: 6 English 102

You are limited to 10 attempts.

## Answer

73 World History I 47

- login to database c.f. #sql task:Tables

```
mysql> SELECT CONCAT(enrollments.sessionID,' ',courses.courseName,' ',COUNT(studentID)) AS sessionID_courseName_num_students FROM enrollments JOIN sessions ON enrollments.sessionID = sessions.sessionID JOIN courses ON sessions.courseID = courses.courseID GROUP BY enrollments.sessionID ORDER BY COUNT(studentID) DESC,enrollID LIMIT 1;
+-----------------------------------+
| sessionID_courseName_num_students |
+-----------------------------------+
| 73 World History I 47             |
+-----------------------------------+
1 row in set (0.27 sec)
```
