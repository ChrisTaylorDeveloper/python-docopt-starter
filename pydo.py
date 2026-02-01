"""Py Docopt Starter.

Usage:
  pydo ls
  pydo (-h | --help)
  pydo --version

Options:
  -h --help    Show this screen.
  --version    Show version.

"""

from docopt import docopt
import subprocess


def run_cmd(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print("✅ Command executed successfully!")
        print("\n--- Standard Output ---\n", result.stdout)
        if result.stderr:
            print("\n--- Standard Error ---\n", result.stderr)

    except subprocess.CalledProcessError as e:
        print(f"❌ Command failed with return code {e.returncode}")
        print("\n--- Standard Error ---\n", e.stderr)

    except FileNotFoundError:
        print("❌ Error: FileNotFoundError.")


if __name__ == "__main__":
    args = docopt(__doc__, version="Py Docopt Starter 0.1")
    # print(args)

    if args["ls"]:
        run_cmd(
            [
                "ls",
                "-l",
            ]
        )
