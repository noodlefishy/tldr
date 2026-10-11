```
leuw@woef-woef:~$ifup --help
ifup - bring interfaces up

Usage:
  ifup [options] <interfaces>

Global options:
  -h, --help                          this help
  -V, --version                       show this program's version

Matching interfaces:
  -a, --auto                          only match against interfaces hinted as 'auto'
  -I, --include PATTERN               only match against interfaces matching PATTERN
  -X, --exclude PATTERN               never match against interfaces matching PATTERN

Execution:
  -f, --force                         force (de)configuration
  -i, --interfaces FILE               use FILE for interface definitions
  -l, --no-lock                       do not use a lockfile to serialize state changes
  -n, --no-act                        do not actually run any commands
  -v, --verbose                       show what commands are being run
  -E, --executor-path PATH            use PATH for executor directory
  -S, --state-file FILE               use FILE for state
  -T, --timeout TIMEOUT               wait TIMEOUT seconds for executors to complete

For more information: man 8 ifup
leuw@woef-woef:~$ 
```
