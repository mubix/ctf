# Temple of Gozer

## Points 250

Find the Temple of Gozer

Consult with the KeyMaster and the GateKeeper to find your path.

(Don't destroy any files here or points will be deducted - Gozer is an angry god)

(You get to break one of the CTF rules for this challenge. Look at you, rebel.)

## Answer

flag-e782f102531da617037fe3bfd80cbe99

1. solve Vinz Clortho's riddle:

>  Ingesting this (jvfddhyduzmc4rhw) will not burn your eyes or make your breath stink,
>  but it will take you into dimension 9000!

- "burn eyes" + "breath stink" = onion
- Tor
- @ http://jvfddhyduzmc4rhw.onion:9000

$ `curl --socks5-hostname 127.0.0.1:9050 -sL http://jvfddhyduzmc4rhw.onion:9000`
```
<?xml version="1.0" encoding="UTF-8"?>
<Error><Code>AccessDenied</Code><Message>Access Denied.</Message><Resource>/</Resource><RequestId>15618855EE92252F</RequestId><HostId>3L137</HostId></Error>
```

- AWS S3 bucket

2. Access key pair = Access Key ID + Secret Access Key

- "Access": "Access Key ID"
- "Secret": "Secret Access Key"

$ [`sudo pip install -U awscli`](https://aws.amazon.com/cli)
```
"${HOME}/.aws/credentials":
	[ctf]
	aws_access_key_id = WAH2B1B0ICX0VMC4WJV9
	aws_secret_access_key = 87cCrcOaz10e5SAEXgkGzIvZJsZ6GSFesnjXuXHf
```

- [proxychains4](https://github.com/rofl0r/proxychains-ng)
```
$ git clone --recursive https://github.com/rofl0r/proxychains-ng.git
$ cd proxychains-ng
$ ./configure --prefix=/usr --sysconfdir=/etc
$ make && sudo make install && sudo make install-config

"${PREFIX}/etc/proxychains.conf":
	dynamic_chain
	quiet_mode
	proxy_dns
	remote_dns_subnet 224
	tcp_read_time_out 15000
	tcp_connect_time_out 8000
	localnet 127.0.0.0/255.0.0.0

	[ProxyList]
	socks4 127.0.0.1 9050
```

- list bucket(s)
```
proxychains4 aws --profile ctf --endpoint-url http://jvfddhyduzmc4rhw.onion:9000 s3 ls
[proxychains] config file found: /etc/proxychains.conf
[proxychains] preloading /usr/lib/libproxychains4.so
2018-09-26 01:12:06 security-pumpkin
```

- list object(s)
```
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
```

- download + view contents of "flag.txt"
```
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
