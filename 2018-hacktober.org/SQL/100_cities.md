# Cities

## Points 100

Using the westridge database, submit the number of students that live in Maddison.

You are limited to 10 attempts.

## Answer

177

- login to database c.f. #sql task:Tables

```
mysql> SELECT COUNT(*) FROM students WHERE city = 'Maddison';
+----------+
| COUNT(*) |
+----------+
|      177 |
+----------+
1 row in set (0.35 sec)
```
