# Cities

## Points 100

Using the westridge database, submit the number of students that live in Maddison.

You are limited to 10 attempts.

## Answer

177

* username + password from #pwn task:Cracked

```
$ mysql -h 104.248.119.92 -P 666 -u westridge -p123456789 westridge
mysql> SELECT COUNT(*) FROM students WHERE city = 'Maddison';
+----------+
| COUNT(*) |
+----------+
|      177 |
+----------+
1 row in set (0.38 sec)
```
