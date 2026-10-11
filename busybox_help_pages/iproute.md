```
leuw@woef-woef:~$iproute --help
BusyBox v1.37.0 (2026-01-10 15:38:28 UTC) multi-call binary.

Usage: iproute list|flush|add|del|change|append|replace|test ROUTE

iproute list|flush SELECTOR
	SELECTOR := [root PREFIX] [match PREFIX] [proto RTPROTO]
	PREFIX := default|ADDR[/MASK]
iproute get ADDR [from ADDR iif IFACE]
	[oif IFACE] [tos TOS]
iproute add|del|change|append|replace|test ROUTE
	ROUTE := NODE_SPEC [INFO_SPEC]
	NODE_SPEC := PREFIX [table TABLE_ID] [proto RTPROTO] [scope SCOPE] [metric METRIC]
	INFO_SPEC := NH OPTIONS
	NH := [via [inet|inet6] ADDR] [dev IFACE] [src ADDR] [onlink]
	OPTIONS := [mtu [lock] NUM] [advmss [lock] NUM]
leuw@woef-woef:~$ 
```
