```
leuw@woef-woef:~$nameif --help
BusyBox v1.37.0 (2026-01-10 15:38:28 UTC) multi-call binary.

Usage: nameif [-s] [-c FILE] [IFNAME SELECTOR]...

Rename network interface while it in the down state.
The device matched by SELECTOR is renamed to IFNAME.
SELECTOR can be a combination of:
	driver=STRING
	bus=STRING
	phy_address=NUM
	[mac=]XX:XX:XX:XX:XX:XX

	-c FILE	Configuration file (default: /etc/mactab)
	-s	Log to syslog
leuw@woef-woef:~$ 
```
