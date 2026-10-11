```
leuw@woef-woef:~$mdev --help
BusyBox v1.37.0 (2026-01-10 15:38:28 UTC) multi-call binary.

Usage: mdev [-vS] { [-s] | [-df] }

	-v	Verbose
	-S	Log to syslog too
	-s	Scan /sys and populate /dev
	-d	Daemon, listen on netlink
	-f	Run in foreground

Bare mdev is a kernel hotplug helper. To activate it:
	echo /sbin/mdev >/proc/sys/kernel/hotplug

It uses /etc/mdev.conf with lines
	[-][ENV=regex;]...DEVNAME UID:GID PERM [>|=PATH]|[!] [@|$|*PROG]
where DEVNAME is device name regex, @major,minor[-minor2], or
environment variable regex. A common use of the latter is
to load modules for hotplugged devices:
	$MODALIAS=.* 0:0 660 @modprobe "$MODALIAS"

If /dev/mdev.seq file exists, mdev will wait for its value
to match $SEQNUM variable. This prevents plug/unplug races.
To activate this feature, create empty /dev/mdev.seq at boot.

If /dev/mdev.log file exists, debug log will be appended to it.
leuw@woef-woef:~$ 
```
