```
leuw@woef-woef:~$cp --help
BusyBox v1.37.0 (2026-01-10 15:38:28 UTC) multi-call binary.

Usage: cp [-arPLHpfinlsTu] SOURCE DEST
or: cp [-arPLHpfinlsu] SOURCE... { -t DIRECTORY | DIRECTORY }

Copy SOURCEs to DEST

	-a	Same as -dpR
	-R,-r	Recurse
	-d,-P	Preserve symlinks (default if -R)
	-L	Follow all symlinks
	-H	Follow symlinks on command line
	-p	Preserve file attributes if possible
	-f	Overwrite
	-i	Prompt before overwrite
	-n	Don't overwrite
	-l,-s	Create (sym)links
	-T	Refuse to copy if DEST is a directory
	-t DIR	Copy all SOURCEs into DIR
	-u	Copy only newer files
leuw@woef-woef:~$ 
```
