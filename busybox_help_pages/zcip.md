```
leuw@woef-woef:~$zcip --help
BusyBox v1.37.0 (2026-01-10 15:38:28 UTC) multi-call binary.

Usage: zcip [OPTIONS] IFACE SCRIPT

Manage a ZeroConf IPv4 link-local address

	-f		Run in foreground
	-q		Quit after obtaining address
	-r 169.254.x.x	Request this address first
	-l x.x.0.0	Use this range instead of 169.254
	-v		Verbose

$LOGGING=none		Suppress logging
$LOGGING=syslog 	Log to syslog

With no -q, runs continuously monitoring for ARP conflicts,
exits only on I/O errors (link down etc)
leuw@woef-woef:~$ 
```
