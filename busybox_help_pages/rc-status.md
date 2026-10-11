```
leuw@woef-woef:~$rc-status --help
Usage: rc-status [-C] [-f ini] [-i state] [runlevel]
   or: rc-status [-C] [-f ini] [-a | -m | -S | -s | -u]
   or: rc-status [-C] [-c | -l | -r]

Options: [ acf:i:lmrsSuChqVvU ]
  -a, --all                         Show services from all run levels
  -c, --crashed                     Show crashed services
  -f, --format <arg>                format status to be parsable (currently arg must be ini)
  -i, --in-state <arg>              Show services which are in this state
  -l, --list                        Show list of run levels
  -m, --manual                      Show manually started services
  -r, --runlevel                    Show the name of the current runlevel
  -s, --servicelist                 Show service list
  -S, --supervised                  show supervised services
  -u, --unused                      Show services not assigned to any runlevel
  -h, --help                        Display this help output
  -C, --nocolor                     Disable color output
  -V, --version                     Display software version
  -v, --verbose                     Run verbosely
  -q, --quiet                       Run quietly (repeat to suppress errors)
  -U, --user                        Run in user mode
leuw@woef-woef:~$ 
```
