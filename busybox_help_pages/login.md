```
leuw@woef-woef:~$login --help
BusyBox v1.37.0 (2026-01-10 15:38:28 UTC) multi-call binary.

Usage: login [-p] [-h HOST] [[-f] USER]

Begin a new session on the system

	-f	Don't authenticate (user already authenticated)
	-h HOST	Host user came from (for network logins)
	-p	Preserve environment

$LOGIN_TIMEOUT		Seconds (default 60, 0 - disable)
$LOGIN_PRE_SUID_SCRIPT	Execute before user ID change
leuw@woef-woef:~$ 
```
