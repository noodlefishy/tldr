```
leuw@woef-woef:~$run-parts --help
BusyBox v1.37.0 (2026-01-10 15:38:28 UTC) multi-call binary.

Usage: run-parts [-a ARG]... [-u UMASK] [--reverse] [--test] [--exit-on-error] [--list] DIRECTORY

Run a bunch of scripts in DIRECTORY

	-a ARG		Pass ARG as argument to scripts
	-u UMASK	Set UMASK before running scripts
	--reverse	Reverse execution order
	--test		Dry run
	--exit-on-error	Exit if a script exits with non-zero
	--list		Print names of matching files even if they are not executable
leuw@woef-woef:~$ 
```
