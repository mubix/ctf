# Primary Key

## Points 25

Using the westridge database, submit the primary key of the "teachers" table.

You are limited to 5 attempts.

## Answer

teacherID

* username + password from #pwn task:Cracked

```
$ mysql -h 104.248.119.92 -P 666 -u westridge -p123456789 westridge
mysql> DESCRIBE teachers;
+-----------+--------------+------+-----+---------+----------------+
| Field     | Type         | Null | Key | Default | Extra          |
+-----------+--------------+------+-----+---------+----------------+
| teacherID | int(11)      | NO   | PRI | NULL    | auto_increment |
| firstName | varchar(30)  | NO   |     | NULL    |                |
| lastName  | varchar(30)  | NO   |     | NULL    |                |
| middle    | varchar(3)   | NO   |     | NULL    |                |
| email     | varchar(255) | NO   |     | NULL    |                |
| deptID    | int(11)      | NO   | MUL | NULL    |                |
| street    | varchar(255) | YES  |     | NULL    |                |
| city      | varchar(255) | YES  |     | NULL    |                |
| state     | varchar(2)   | YES  |     | NULL    |                |
| zip       | varchar(5)   | YES  |     | NULL    |                |
| country   | varchar(2)   | YES  |     | NULL    |                |
+-----------+--------------+------+-----+---------+----------------+
11 rows in set (0.46 sec)
```
