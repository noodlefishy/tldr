```
leuw@woef-woef:~$start-stop-daemon --help
Usage: start-stop-daemon [options] 

Options: [ I:KN:PR:Sa:bc:d:e:g:ik:mn:op:s:tu:r:w:x:0:1:2:3:4:ChqVvU ]
      --capabilities <arg>          Set the inheritable, ambient and bounding capabilities
      --secbits <arg>               Set the security-bits for the program
      --no-new-privs                Set the No New Privs flag for the program
  -I, --ionice <arg>                Set an ionice class:data when starting
  -K, --stop                        Stop daemon
  -N, --nicelevel <arg>             Set a nicelevel when starting
      --oom-score-adj <arg>         Set OOM score adjustment when starting
  -R, --retry <arg>                 Retry schedule to use when stopping
  -S, --start                       Start daemon
  -a, --startas <arg>               deprecated, use --exec or --name
  -b, --background                  Force daemon to background
  -c, --chuid <arg>                 deprecated, use --user
  -d, --chdir <arg>                 Change the PWD
  -e, --env <arg>                   Set an environment string
  -k, --umask <arg>                 Set the umask for the daemon
  -g, --group <arg>                 Change the process group
  -i, --interpreted                 Match process name by interpreter
  -m, --make-pidfile                Create a pidfile
  -n, --name <arg>                  Match process name
  -o, --oknodo                      deprecated
  -p, --pidfile <arg>               Match pid found in this file
  -s, --signal <arg>                Send a different signal
  -t, --test                        Test actions, don't do them
  -u, --user <arg>                  Change the process user
  -r, --chroot <arg>                Chroot to this directory
  -w, --wait <arg>                  Milliseconds to wait for daemon start
  -x, --exec <arg>                  Binary to start/stop
  -0, --stdin <arg>                 Redirect stdin to file
  -1, --stdout <arg>                Redirect stdout to file
  -2, --stderr <arg>                Redirect stderr to file
  -3, --stdout-logger <arg>         Redirect stdout to process
  -4, --stderr-logger <arg>         Redirect stderr to process
  -P, --progress                    Print dots each second while waiting
      --scheduler <arg>             Set process scheduler
      --scheduler-priority <arg>    Set process scheduler priority
      --notify <arg>                Configures experimental notification behaviour
  -h, --help                        Display this help output
  -C, --nocolor                     Disable color output
  -V, --version                     Display software version
  -v, --verbose                     Run verbosely
  -q, --quiet                       Run quietly (repeat to suppress errors)
  -U, --user                        Run in user mode
leuw@woef-woef:~$ 
```
