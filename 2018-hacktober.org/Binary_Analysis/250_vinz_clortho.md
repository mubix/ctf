# Vinz Clortho

## Points 250

They say Vinz Clortho is a Trickster of a KeyMaster. Can you find the flag and solve his riddle?

https://goo.gl/a8FJYv

Local copy - [VinzClortho.zip](bin/VinzClortho.zip)

## Answer

flag-XRQM80NMOLRXSO9G

$ `7za l VinzClortho.zip`
```
Path = VinzClortho.zip
Type = zip
Physical Size = 3971

   Date      Time    Attr         Size   Compressed  Name
------------------- ----- ------------ ------------  ------------------------
2018-10-08 22:28:10 ....A         8704         3793  AreYouTheKeymaster.exe
------------------- ----- ------------ ------------  ------------------------
2018-10-08 22:28:10               8704         3793  1 files
```

reverse .NET Binary via [dnSpy](https://github.com/0xd4d/dnSpy/releases)

- `GuessingGame4`
- `public class Program`
- `private void Run()`
- input: `XXXX`

```
Congratulations you have found the secret passageway

flag-XRQM80NMOLRXSO9G

Now can you solve Vinz Clortho's riddle?
Ingesting this (jvfddhyduzmc4rhw) will not burn your eyes or make your breath stink,
but it will take you into dimension 9000!
```
