# Larry

## Points 125

Can you help Larry?

[http://www.5z8.info/-49exploit-begin--_o6o0gt_5waystokillwithamelon](https://hacktober.nyc3.digitaloceanspaces.com/Larry.out)

Local copy - [Larry.out](bin/Larry.out)

## Answer

@ https://veteransec.com/2018/10/19/hacktober-ctf-2018-binary-analysis-larry

$ `file Larry.out`
```
Larry.out: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=c94d9d71a615fc403d6cb8e82c0be48241fdb614, not stripped
```

relevant c pseudocode:
```
int __cdecl main(int argc, const char **argv, const char **envp)
{
	v7 = 2;
	v8 = 8;
	v9 = 97;
	v10 = 3;
	v11 = 45;
	v12 = 89;
	v13 = 11;
	v14 = 17;
	v15 = 39;
	v16 = 14;
	v17 = 1;
	v18 = 32;
	v19 = 64;
	v20 = 32;
	v21 = 8;
	v22 = 5;
	v23 = 22;
	v24 = 64;
	v25 = 14;
	v26 = 100;
	v27 = 44;
	v28 = 32;
	v29 = 76;
	v30 = 64;
	v31 = 14;
	v32 = 14;
	v33 = 21;
	v34 = 33;

	for ( i = 0; i <= 27; ++i )
	{
		if ( *(&v7 + i) <= 0 || *(&v7 + i) > 22 )
		{
			v6[i] = *(&v7 + i);
		}
		else
		{
			*(&v7 + i) += 100;
			v6[i] = *(&v7 + i);
		}
	}
}
```

- flag is a series of ASCII values, as depicted above
- 100 is added to value, if it is in range `0 < value <= 22`

`print "".join(map(chr,[(c+100) if 0 < c and c <= 22 else c for c in [2,8,97,3,45,89,11,17,39,14,1,32,64,32,8,5,22,64,14,100,44,32,76,64,14,14,21,33]]))`

flag-You're @ liz@rd, L@rry!
