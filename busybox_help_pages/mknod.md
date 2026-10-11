```
leuw@woef-woef:~$mknod --help
BusyBox v1.37.0 (2026-01-10 15:38:28 UTC) multi-call binary.

Usage: mknod [-m MODE] NAME TYPE [MAJOR MINOR]

Create a special file (block, character, or pipe)

	-m MODE	Creation mode (default a=rw)
TYPE:
	b	Block device
	c or u	Character device
	p	Named pipe (MAJOR MINOR must be omitted)
leuw@woef-woef:~$ 
```
