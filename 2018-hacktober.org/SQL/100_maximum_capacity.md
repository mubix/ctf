# Maximum Capacity

## Points 100

Using the westridge database, submit the maximum studentID number that a student can be displayed.

You are limited to 20 attempts.

## Answer

`int(11)` => 99999999999

- login to database c.f. #sql task:Tables

```
mysql> DESCRIBE students;
+-----------+--------------+------+-----+---------+----------------+
| Field     | Type         | Null | Key | Default | Extra          |
+-----------+--------------+------+-----+---------+----------------+
| studentID | int(11)      | NO   | PRI | NULL    | auto_increment |
| firstName | varchar(30)  | NO   |     | NULL    |                |
| lastName  | varchar(30)  | NO   |     | NULL    |                |
| middle    | varchar(3)   | NO   |     | NULL    |                |
| grade     | int(2)       | YES  |     | NULL    |                |
| street    | varchar(255) | YES  |     | NULL    |                |
| city      | varchar(255) | YES  |     | NULL    |                |
| state     | varchar(2)   | YES  |     | NULL    |                |
| zip       | varchar(5)   | YES  |     | NULL    |                |
| country   | varchar(2)   | YES  |     | NULL    |                |
+-----------+--------------+------+-----+---------+----------------+
10 rows in set (0.36 sec)
```
