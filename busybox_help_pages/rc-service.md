```
leuw@woef-woef:~$rc-service --help
Usage: rc-service [options] [-i] <service> <cmd>...
   or: rc-service [options] -e <service>
   or: rc-service [options] -l
   or: rc-service [options] -r <service>

Options: [ cdDe:ilr:INsSZChqVvU ]
  -d, --debug                       set xtrace when running the command
  -D, --nodeps                      ignore dependencies
  -e, --exists <arg>                tests if the service exists or not
  -c, --ifcrashed                   if the service is crashed run the command
  -i, --ifexists                    if the service exists run the command
  -I, --ifinactive                  if the service is inactive run the command
  -N, --ifnotstarted                if the service is not started run the command
  -s, --ifstarted                   if the service is started run the command
  -S, --ifstopped                   if the service is stopped run the command
  -l, --list                        list all available services
  -r, --resolve <arg>               resolve the service name to an init script
  -Z, --dry-run                     dry run (show what would happen)
  -h, --help                        Display this help output
  -C, --nocolor                     Disable color output
  -V, --version                     Display software version
  -v, --verbose                     Run verbosely
  -q, --quiet                       Run quietly (repeat to suppress errors)
  -U, --user                        Run in user mode
leuw@woef-woef:~$ 
```
