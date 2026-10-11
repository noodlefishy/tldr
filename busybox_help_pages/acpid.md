```
leuw@woef-woef:~$acpid --help
BusyBox v1.37.0 (2026-01-10 15:38:28 UTC) multi-call binary.

Usage: acpid [-df] [-c CONFDIR] [-l LOGFILE] [-a ACTIONFILE] [-M MAPFILE] [-e PROC_EVENT_FILE] [-p PIDFILE]

Listen to ACPI events and spawn specific helpers on event arrival

	-d	Log to stderr, not log file (implies -f)
	-f	Run in foreground
	-c DIR	Config directory [/etc/acpi]
	-e FILE	/proc event file [/proc/acpi/event]
	-l FILE	Log file [/var/log/acpid.log]
	-p FILE	Pid file [/run/acpid.pid]
	-a FILE	Action file [/etc/acpid.conf]
	-M FILE Map file [/etc/acpi.map]

Accept and ignore compatibility options -g -m -s -S -v
leuw@woef-woef:~$ 
```
