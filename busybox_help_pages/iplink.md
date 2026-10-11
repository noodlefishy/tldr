```
leuw@woef-woef:~$iplink --help
BusyBox v1.37.0 (2026-01-10 15:38:28 UTC) multi-call binary.

Usage: iplink set IFACE [up|down] [arp on|off] [multicast on|off]
	[promisc on|off] [mtu NUM] [name NAME] [qlen NUM] [address MAC]
	[master IFACE | nomaster] [netns PID]
iplink add [link IFACE] IFACE [address MAC] type TYPE [ARGS]
iplink delete IFACE type TYPE [ARGS]
	TYPE ARGS := vlan VLANARGS | vrf table NUM
	VLANARGS := id VLANID [protocol 802.1q|802.1ad] [reorder_hdr on|off]
		[gvrp on|off] [mvrp on|off] [loose_binding on|off]
iplink show [IFACE]
leuw@woef-woef:~$ 
```
