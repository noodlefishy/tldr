```
leuw@woef-woef:~$ifquery --help
ifquery - query interface configuration

Usage:
  ifquery [options] <interfaces>
  ifquery [options] --list

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

Program-specific options:
  -r, --running                       show configured (running) interfaces
  -s, --state                         show configured state
  -p, --property PROPERTY             print values of properties matching PROPERTY
  -D, --dot                           generate a dependency graph
  -L, --list                          list matching interfaces
  -P, --pretty-print                  pretty print the interfaces instead of just listing
  -U, --allow-undefined               allow querying undefined (virtual) interfaces

For more information: man 8 ifquery
leuw@woef-woef:~$ 
```
