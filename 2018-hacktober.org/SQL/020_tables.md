# Tables

## Points 20

Gh0stf4c3 hackers have compromised Westridge High School's internal database. The school does not have their database configured to keep logs, so we need you to determine the integrity of the database and find what was changed.

Log into the "westridge" database at 104.248.119.92 port 666 and submit the number of tables as the flag.

You are limited to 5 attempts.

## Answer

8

* username + password from #pwn task:Cracked

```
$ mysql -h 104.248.119.92 -P 666 -u westridge -p123456789 -A westridge
mysql: [Warning] Using a password on the command line interface can be insecure.
```

or

```
$ mysql_config_editor set --login-path=hacktober2018 --host=104.248.119.92 --port=666 --user=westridge --password
Enter password: 123456789
$ `mysql --login-path=hacktober2018 -A westridge`
```

```
mysql> SHOW TABLES;
+---------------------+
| Tables_in_westridge |
+---------------------+
| assignments         |
| courses             |
| departments         |
| enrollments         |
| grades              |
| sessions            |
| students            |
| teachers            |
+---------------------+
8 rows in set (0.41 sec)
```
