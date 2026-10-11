```
leuw@woef-woef:~$hwclock --help
BusyBox v1.37.0 (2026-01-10 15:38:28 UTC) multi-call binary.

Usage: hwclock [-ul] [-f DEV] [-s|-w|--systz|--param-get PARAM|--param-set PARAM=VAL]

Show or set hardware clock (RTC)

	-f DEV	Use this device (e.g. /dev/rtc2)
	-u	Assume RTC is kept in UTC
	-l	Assume RTC is kept in local time
		(if neither is given, read from /var/lib/hwclock/adjtime)
	-s	Set system time from RTC
	-w	Set RTC from system time
	--systz	Set in-kernel timezone, correct system time
		if RTC is kept in local time
	--param-get PARAM	Get RTC parameter
	--param-set PARAM=VAL	Set RTC parameter
leuw@woef-woef:~$ 
```
