```
leuw@woef-woef:~$iprule --help
BusyBox v1.37.0 (2026-01-10 15:38:28 UTC) multi-call binary.

Usage: iprule [list] | add|del SELECTOR ACTION

	SELECTOR := [from PREFIX] [to PREFIX] [tos TOS] [fwmark FWMARK[/MASK]]
			[dev IFACE] [pref NUMBER]
	ACTION := [table TABLE_ID] [nat ADDR]
			[prohibit|reject|unreachable]
			[realms [SRCREALM/]DSTREALM]
	TABLE_ID := [local|main|default|NUMBER]
leuw@woef-woef:~$ 
```
