```
leuw@woef-woef:~$watchdog --help
BusyBox v1.37.0 (2026-01-10 15:38:28 UTC) multi-call binary.

Usage: watchdog [-t N[ms]] [-T N[ms]] [-F] DEV

Periodically write to watchdog device DEV

	-T N	Reboot after N seconds if not reset (default 60)
	-t N	Reset every N seconds (default 30)
	-F	Run in foreground

Use 500ms to specify period in milliseconds
leuw@woef-woef:~$ 
```
