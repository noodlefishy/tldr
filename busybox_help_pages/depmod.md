```
leuw@woef-woef:~$depmod --help
Usage:
	depmod -[aA] [options] [forced_version]

If no arguments (except options) are given, "depmod -a" is assumed

depmod will output a dependency list suitable for the modprobe utility.

Options:
	-a, --all            Probe all modules
	-A, --quick          Only does the work if there's a new module
	-e, --errsyms        Report not supplied symbols
	-n, --show           Write the dependency file on stdout only
	-P, --symbol-prefix  Architecture symbol prefix
	-C, --config=PATH    Read configuration from PATH
	-v, --verbose        Enable verbose mode
	-w, --warn           Warn on duplicates
	-V, --version        show version
	-h, --help           show this help

The following options are useful for people managing distributions:
	-b, --basedir=DIR    Root path (default: /).
	-m, --moduledir=DIR  Module directory (default: /lib/modules).
	-o, --outdir=DIR     Output root path (default: same as <basedir>).
	-F, --filesyms=FILE  Use the file instead of the
	                     current kernel symbols.
	-E, --symvers=FILE   Use Module.symvers file to check
	                     symbol versions.
leuw@woef-woef:~$ 
```
