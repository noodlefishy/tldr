```
leuw@woef-woef:~$switch_root --help
BusyBox v1.37.0 (2026-01-10 15:38:28 UTC) multi-call binary.

Usage: switch_root [-c CONSOLE_DEV] NEW_ROOT NEW_INIT [ARGS]

Free initramfs and switch to another root fs:
chroot to NEW_ROOT, delete all in /, move NEW_ROOT to /,
execute NEW_INIT. PID must be 1. NEW_ROOT must be a mountpoint.

	-c DEV	Reopen stdio to DEV after switch
leuw@woef-woef:~$ 
```
