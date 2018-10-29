# Matching Game

## Points 300

Using the westridge database, submit the first name of the student whose first name matches the following criteria:

- The first two letters contain an A, B, or D (must contain 2 of those letters; e.g. AB, AD, BD, …)
- Contains at least three letters after the first two
- Ends in an additional letter between W and Z.

You are limited to 20 attempts.

## Answer

Bailey

- login to database c.f. #sql task:Tables

```
mysql> SELECT firstName FROM students;
+-------------+
| firstName   |
+-------------+
| Simeon      |
| Prince      |
| Emmett      |
| ...         |
| Daniella    |
| Lamar       |
| Shaniya     |
+-------------+
4281 rows in set (0.85 sec)
```

then use "Regular Expressions" to determine answer
