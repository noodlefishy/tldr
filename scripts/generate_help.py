import os
import subprocess
from pathlib import Path

ROOT = Path("/Users/leuw/dev/manuals")
COMMANDS_FILE = ROOT / "alpine commands.txt"
OUTPUT_DIR = ROOT / "busybox_help_pages"


REMOTE_HOST = "leuw@192.168.1.128"


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if not COMMANDS_FILE.exists():
        print(f"[ERARO] '{COMMANDS_FILE}' not found.")
        return

    with open(COMMANDS_FILE, "r", encoding="utf-8") as f:
        commands = [line.strip() for line in f if line.strip()]

    for cmd in commands:
        output_file = OUTPUT_DIR / f"{cmd}.md"
        help_text = ""

        try:
            # Try running command over SSH (e.g., ssh user@host "cp --help")
            ssh_cmd = ["ssh", REMOTE_HOST, f"{cmd} --help"]
            result = subprocess.run(
                ssh_cmd, capture_output=True, text=True, timeout=10
            )
            help_text = (
                result.stdout + result.stderr
                if result.stdout or result.stderr
                else ""
            )

            # If empty or failed, try via busybox binary over SSH
            if not help_text.strip() or result.returncode != 0:
                ssh_bb_cmd = ["ssh", REMOTE_HOST, f"busybox {cmd} --help"]
                result_bb = subprocess.run(
                    ssh_bb_cmd, capture_output=True, text=True, timeout=10
                )
                help_text = result_bb.stdout + result_bb.stderr
        except Exception as e:
            help_text = f"Error executing {cmd} over SSH: {e}"

        # Format as the exact terminal block you requested
        formatted_content = f"```\nleuw@woef-woef:~${cmd} --help\n{help_text.strip()}\nleuw@woef-woef:~$ \n```\n"

        with open(output_file, "w", encoding="utf-8") as out_f:
            out_f.write(formatted_content)

        print(f"Fetched and generated: {cmd}.md")

    print(f"\nAll remote help pages generated successfully in: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
