```
leuw@woef-woef:~$slattach --help
BusyBox v1.37.0 (2026-01-10 15:38:28 UTC) multi-call binary.

Usage: slattach [-ehmLF] [-c SCRIPT] [-s BAUD] [-p PROTOCOL] SERIAL_DEVICE

Configure serial line as SLIP network interface

	-p PROT	Protocol: slip, cslip (default), slip6, clisp6, adaptive
	-s BAUD	Line speed
	-e	Exit after initialization
	-h	Exit if carrier is lost (else never exits)
	-c PROG	Run PROG on carrier loss
	-m	Do NOT set raw 8bit mode
	-L	Enable 3-wire operation
	-F	Disable RTS/CTS flow control
leuw@woef-woef:~$ 
```
