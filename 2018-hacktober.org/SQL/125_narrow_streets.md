# Narrow Streets

## Points 125

Using the westridge database, submit the number of students that live on a street that ends in "Lane".

You are limited to 10 attempts.

## Answer

366

- login to database c.f. #sql task:Tables

```
mysql> SELECT COUNT(*) FROM students WHERE street LIKE '%Lane';
+----------+
| COUNT(*) |
+----------+
|      366 |
+----------+
1 row in set (0.43 sec)
```
