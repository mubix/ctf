# Where Are Yu?

## Points 50

Using the westridge database, submit Walter Yu's street address.

You are limited to 10 attempts.

## Answer

396 Smith Street

* username + password from #pwn task:Cracked

```
$ mysql -h 104.248.119.92 -P 666 -u westridge -p123456789 westridge
mysql> SELECT street FROM students WHERE firstName = 'Walter' AND lastName = 'Yu';
+------------------+
| street           |
+------------------+
| 396 Smith Street |
+------------------+
1 row in set (0.45 sec)
```
