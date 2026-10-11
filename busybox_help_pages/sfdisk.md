```
leuw@woef-woef:~$sfdisk --help
Usage:
 sfdisk [options] <dev> [[-N] <part>]
 sfdisk [options] <command>

Display or manipulate a disk partition table.

Commands:
 -A, --activate <dev> [<part> ...] list or set bootable (P)MBR partitions
 -d, --dump <dev>                  dump partition table (usable for later input)
 -J, --json <dev>                  dump partition table in JSON format
 -B, --backup-pt-sectors <dev>     binary partition table backup (see -b and -O)
 -g, --show-geometry [<dev> ...]   list geometry of all or specified devices
 -l, --list [<dev> ...]            list partitions of each device
 -F, --list-free [<dev> ...]       list unpartitioned free areas of each device
 -r, --reorder <dev>               fix partitions order (by start offset)
 -s, --show-size [<dev> ...]       list sizes of all or specified devices
 -T, --list-types                  print the recognized types (see -X)
 -V, --verify [<dev> ...]          test whether partitions seem correct
     --delete <dev> [<part> ...]   delete all or specified partitions

 --part-label <dev> <part> [<str>] print or change partition label
 --part-type <dev> <part> [<type>] print or change partition type
 --part-uuid <dev> <part> [<uuid>] print or change partition uuid
 --part-attrs <dev> <part> [<str>] print or change partition attributes

 --discard-free <dev>              discard (trim) unpartitioned areas
 --disk-id <dev> [<str>]           print or change disk label ID (UUID)
 --relocate <oper> <dev>           move partition header

Arguments:
 <dev>                     device (usually disk) path
 <part>                    partition number
 <type>                    partition type, GUID for GPT, hex for MBR

Options:
 -a, --append              append partitions to existing partition table
 -b, --backup              backup partition table sectors (see -O)
     --bytes               print SIZE in bytes rather than in human readable format
     --move-data[=<typescript>] move partition data after relocation (requires -N)
     --move-use-fsync      use fsync after each write when move data
 -f, --force               disable all consistency checking
     --color[=<when>]      colorize output (auto, always or never)
                             colors are enabled by default
     --sector-size <size>  physical and logical sector size
     --lock[=<mode>]       use exclusive device lock (yes, no or nonblock)
 -N, --partno <num>        specify partition number
 -n, --no-act              do everything except write to device
     --no-reread           do not check whether the device is in use
     --no-tell-kernel      do not tell kernel about changes
 -O, --backup-file <path>  override default backup file name
 -o, --output <list>       output columns
 -q, --quiet               suppress extra info messages
 -w, --wipe <mode>         wipe signatures (auto, always or never)
 -W, --wipe-partitions <mode>  wipe signatures from new partitions (auto, always or never)
 -X, --label <name>        specify label type (dos, gpt, ...)
 -Y, --label-nested <name> specify nested label type (dos, bsd)

 -G, --show-pt-geometry    deprecated, alias to --show-geometry
 -L, --Linux               deprecated, only for backward compatibility
 -u, --unit S              deprecated, only sector unit is supported

 -h, --help                display this help
 -v, --version             display version

Available output columns:
 gpt: Device Start End Sectors Size Type Type-UUID Attrs Name UUID
 dos: Device Start End Sectors Cylinders Size Type Id Attrs Boot End-C/H/S
      Start-C/H/S
 bsd: Slice Start End Sectors Cylinders Size Type Bsize Cpg Fsize
 sgi: Device Start End Sectors Cylinders Size Type Id Attrs
 sun: Device Start End Sectors Cylinders Size Type Id Flags

For more details see sfdisk(8).
leuw@woef-woef:~$ 
```
