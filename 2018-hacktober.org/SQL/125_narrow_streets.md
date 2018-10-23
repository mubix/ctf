# Narrow Streets

## Points 125

Using the westridge database, submit the number of students that live on a street that ends in "Lane".

You are limited to 10 attempts.

## Answer

366

* username + password from #pwn task:Cracked

```
$ mysql -h 104.248.119.92 -P 666 -u westridge -p123456789 westridge
mysql> SELECT COUNT(*) FROM students WHERE street LIKE '%Lane';
+----------+
| COUNT(*) |
+----------+
|      366 |
+----------+
1 row in set (0.43 sec)
```
