```
leuw@woef-woef:~$inotifyd --help
BusyBox v1.37.0 (2026-01-10 15:38:28 UTC) multi-call binary.

Usage: inotifyd PROG FILE1[:MASK]...

Run PROG on filesystem changes.
When a filesystem event matching MASK occurs on FILEn,
PROG ACTUAL_EVENTS FILEn [SUBFILE] is run.
If PROG is -, events are sent to stdout.
Events:
	a	File is accessed
	c	File is modified
	e	Metadata changed
	w	Writable file is closed
	0	Unwritable file is closed
	r	File is opened
	D	File is deleted
	M	File is moved
	u	Backing fs is unmounted
	o	Event queue overflowed
	x	File can't be watched anymore
If watching a directory:
	y	Subfile is moved into dir
	m	Subfile is moved out of dir
	n	Subfile is created
	d	Subfile is deleted

inotifyd waits for PROG to exit.
When x event happens for all FILEs, inotifyd exits.
leuw@woef-woef:~$ 
```
