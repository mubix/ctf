# Courses

## Points 50

Using the westridge database, submit the number of classes offered at Westridge HS.

You are limited to 10 attempts.

## Answer

32

- login to database c.f. #sql task:Tables

```
mysql> SELECT COUNT(*) FROM courses;
+----------+
| COUNT(*) |
+----------+
|       32 |
+----------+
1 row in set (0.23 sec)
```
