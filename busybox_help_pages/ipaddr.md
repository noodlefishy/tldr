```
leuw@woef-woef:~$ipaddr --help
BusyBox v1.37.0 (2026-01-10 15:38:28 UTC) multi-call binary.

Usage: ipaddr add|del IFADDR dev IFACE | show|flush [dev IFACE] [to PREFIX]

ipaddr add|change|replace|delete dev IFACE [CONFFLAG-LIST] IFADDR
	IFADDR := PREFIX | ADDR peer PREFIX [broadcast ADDR|+|-]
		[anycast ADDR] [label STRING] [scope SCOPE]
	PREFIX := ADDR[/MASK]
	SCOPE := [host|link|global|NUMBER]
	CONFFLAG-LIST := [CONFFLAG-LIST] CONFFLAG
	CONFFLAG := [noprefixroute]
ipaddr show|flush [dev IFACE] [scope SCOPE] [to PREFIX] [label PATTERN]
leuw@woef-woef:~$ 
```
