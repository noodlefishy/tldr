```
leuw@woef-woef:~$init --help
BusyBox v1.37.0 (2026-01-10 15:38:28 UTC) multi-call binary.

Usage: init

Init is the first process started during boot. It never exits.
It (re)spawns children according to /etc/inittab.
Signals:
HUP: reload /etc/inittab
TSTP: stop respawning until CONT
QUIT: re-exec another init
USR1/TERM/USR2/INT: run halt/reboot/poweroff/Ctrl-Alt-Del script
leuw@woef-woef:~$ 
```
