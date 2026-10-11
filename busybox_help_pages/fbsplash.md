```
leuw@woef-woef:~$fbsplash --help
BusyBox v1.37.0 (2026-01-10 15:38:28 UTC) multi-call binary.

Usage: fbsplash -s IMGFILE [-c] [-d DEV] [-i INIFILE] [-f CMD] [-T tty]

	-s	Image
	-c	Hide cursor
	-d	Framebuffer device (default /dev/fb0)
	-i	Config file (var=value):
			BAR_LEFT,BAR_TOP,BAR_WIDTH,BAR_HEIGHT
			BAR_R,BAR_G,BAR_B,IMG_LEFT,IMG_TOP,IMG_ALIGN
	-f	Control pipe (else exit after drawing image)
			commands: 'NN' (% for progress bar) or 'exit'
	-T	Switch to TTY to hide all console messages
leuw@woef-woef:~$ 
```
