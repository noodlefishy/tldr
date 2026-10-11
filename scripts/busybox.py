import os
import shutil
from pathlib import Path

CXEFA = Path("/Users/leuw/dev/manuals")
COMMANDS_FILE = CXEFA / "alpine commands.txt"
BUSYBOX_CELLOKO = CXEFA / "applets" / "busybox"
LINUX_CELLOKO = CXEFA / "applets" / "linux"
PAGES_CXEFA = CXEFA / "pages"

KASXNOMOJ = {
    "ash": "sh",
}

COMMANDS_KIJU_NE_EKZISTAS = {
    "bbconfig", "bbsuid", "dumpkmap", "fatattr", "fdflush", "fsync",
    "kbd_mode", "makemime", "pipe_progress", "reformime", "run-parts",
    "setpriv", "acpid", "adjtimex", "bootchartd", "dosfsck", "dosfslabel",
    "eapol_test", "fbsplash", "getty", "ifctrstat", "ifenslave", "ifparse",
    "ifquery", "ifupdown", "inotifyd", "ipaddr", "iplink", "ipneigh",
    "iproute", "iprule", "iptunnel", "klogd", "loadkmap", "mdev",
    "mkdosfs", "mkmntdirs", "nameif", "nlplug-findfs", "openrc-run",
    "raidautorun", "rc-sstat", "setconsole", "slattach", "start-stop-daemon",
    "supervise-daemon", "syslogd", "tunctl", "udhcpc", "vconfig", "watchdog", "zcip"
}


def sercxi_page(name: str):

    linux_fonto = PAGES_CXEFA / "linux" / f"{name}.md"
    if linux_fonto.exists():
        return linux_fonto, LINUX_CELLOKO

    common_fonto = PAGES_CXEFA / "common" / f"{name}.md"
    if common_fonto.exists():
        return common_fonto, BUSYBOX_CELLOKO

    for page_dir in sorted(PAGES_CXEFA.iterdir()):
        if not page_dir.is_dir() or page_dir.name in ["linux", "common"]:
            continue
        fonto_path = page_dir / f"{name}.md"
        if fonto_path.exists():
            return fonto_path, BUSYBOX_CELLOKO

    return None, None


def troviCommandFonto(command: str):
    celo_cmd = KASXNOMOJ.get(command, command)


    fonto, dest = sercxi_page(celo_cmd)
    if fonto:
        return fonto, dest

    if "." in celo_cmd:
        base_cmd = celo_cmd.split(".")[0]
        fonto, dest = sercxi_page(base_cmd)
        if fonto:
            return fonto, dest

    return None, None


def kopiuSeGxiMankas(fonto_path: Path, destination_dir: Path):
    destination_path = destination_dir / fonto_path.name
    if destination_path.exists():
        return

    destination_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(fonto_path, destination_path)


def main():
    if not COMMANDS_FILE.exists():
        print(f"[ERARO] 'alpine commands.txt' ne trovita at cxe {COMMANDS_FILE}")
        return

    with COMMANDS_FILE.open("r", encoding="utf-8") as f:
        commands = [line.strip() for line in f if line.strip()]

    for command in commands:
        if command in COMMANDS_KIJU_NE_EKZISTAS:
            continue  

        fonto_path, destination_dir = troviCommandFonto(command)
        if fonto_path is None or destination_dir is None:
            print(f'[ERARO] PATH/COMMAND NE EKZISTAS!!! "{command}"')
            continue

        kopiuSeGxiMankas(fonto_path, destination_dir)
        


if __name__ == "__main__":
    main()
