# Distinctions

## Points 175

Using the westridge database, submit the SQL query command that will return the number of distinct departments.

You are limited to 10 attempts.

## Answer

SELECT COUNT(DISTINCT deptName) FROM departments;

- login to database c.f. #sql task:Tables

```
mysql> select count(distinct deptName) from departments;
+--------------------------+
| count(distinct deptName) |
+--------------------------+
|                        8 |
+--------------------------+
1 row in set (0.37 sec)
```
