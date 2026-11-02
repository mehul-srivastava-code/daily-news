import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent
RETRY_SECONDS = 10 * 60


def has_internet() -> bool:
    try:
        with urllib.request.urlopen("https://www.google.com", timeout=10):
            return True
    except (OSError, urllib.error.URLError):
        return False


def run_command(*args: str) -> None:
    subprocess.run(args, cwd=PROJECT_DIR, check=True)


def wait_for_internet() -> None:
    while not has_internet():
        print("No internet connection. Retrying in 10 minutes.", flush=True)
        time.sleep(RETRY_SECONDS)


def wait_for_text_file() -> None:
    output_file = PROJECT_DIR / "bot_contributer.txt"
    while not output_file.exists() or not output_file.read_text(encoding="utf-8").strip():
        print("Waiting for text to be added to bot_contributer.txt.", flush=True)
        time.sleep(1)


def main() -> None:
    wait_for_internet()
    run_command(sys.executable, "bot_contributer.py")
    wait_for_text_file()
    run_command("git", "add", ".")
    run_command("git", "commit", "-m", "Daily contribution")
    run_command("git", "push")


if __name__ == "__main__":
    main()
