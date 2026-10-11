```
leuw@woef-woef:~$umount --help
BusyBox v1.37.0 (2026-01-10 15:38:28 UTC) multi-call binary.

Usage: umount [-rlfda] [-t FSTYPE] [-O FSOPT] FILESYSTEM|DIRECTORY

Unmount filesystems

	-a	Unmount all filesystems
	-r	Remount devices read-only if mount is busy
	-l	Lazy umount (detach filesystem)
	-f	Force umount (i.e., unreachable NFS server)
	-d	Free loop device if it has been used
	-t FSTYPE[,...]	Unmount only these filesystem type(s)
	-O FSOPT[,...]	Unmount only filesystem mounted with the given options
leuw@woef-woef:~$ 
```
