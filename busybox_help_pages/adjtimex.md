```
leuw@woef-woef:~$adjtimex --help
BusyBox v1.37.0 (2026-01-10 15:38:28 UTC) multi-call binary.

Usage: adjtimex [-q] [-o OFS] [-f FREQ] [-p TCONST] [-t TICK]

Read or set kernel time variables. See adjtimex(2)

	-q	Quiet
	-o OFF	Time offset, microseconds
	-f FREQ	Frequency adjust, integer kernel units (65536 is 1ppm)
	-t TICK	Microseconds per tick, usually 10000
		(positive -t or -f values make clock run faster)
	-p TCONST
leuw@woef-woef:~$ 
```
