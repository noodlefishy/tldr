```
leuw@woef-woef:~$nlplug-findfs --help
coldplug system til given device is found
usage: nlplug-findfs [options] DEVICE

options:
 -a, --apkovls-file OUTFILE            add paths to found apkovls to OUTFILE
 -b, --boot-repositories-file OUTFILE  add found boot repositories to OUTFILE
 -c, --crypt-device CRYPTDEVICE        run cryptsetup luksOpen when CRYPTDEVICE is found
 -h, --help                            show this help
 -H, --crypt-header HEADER             use HEADER device or file as the LUKS header
 -k, --crypt-key KEY                   device or path to read the key from with optionally :<offset>:<size> appended
 -m, --crypt-name NAME                 use NAME as name for crypto device mapping
 -o, --crypt-offset OFFSET             cryptsetup payload offset
 -D, --crypt-discards                  allow discards on crypto device
 -d, --debug                           enable debugging ouput
 -f, --filter SUBSYSTEM                filter subsystem
 -p, --event-handler PROGRAM           use PROGRAM as handler for every event with DEVNAME
 -t, --timeout TIMEOUT                 timeout after TIMEOUT milliseconds without uevents
 -U, --uevent-buffer-size SIZE         uevent buffer size in bytes
leuw@woef-woef:~$ 
```
