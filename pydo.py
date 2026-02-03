"""Py Docopt Starter.

Usage:
  pydo e0_stderr
  pydo e4_stderr
  pydo e0_stdout
  pydo e4_stdout
  pydo not_found
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
        # pydo e0_stdout
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print("Command executed!")
        print("\n--- Standard Output ---\n", result.stdout)
        # pydo e0_stderr
        if result.stderr:
            print("\n--- Standard Error ---\n", result.stderr)

    # pydo e4_stderr
    # pydo e4_stdout
    # With check=True this block runs whenever return code is non-zero.
    except subprocess.CalledProcessError as e:
        print(f"Command failed with return code {e.returncode}")
        print("\n--- Standard Output ---\n", e.stdout)
        print("\n--- Standard Error ---\n", e.stderr)

    # pydo not_found
    except FileNotFoundError:
        print("Error: FileNotFoundError.")


if __name__ == "__main__":
    args = docopt(__doc__, version="Py Docopt Starter 1.0.0")
    # print(args)

    if args["e0_stderr"]:
        run_cmd(
            [
                "stderr_test_e0",
            ]
        )

    if args["e4_stderr"]:
        run_cmd(
            [
                "stderr_test_e4",
            ]
        )

    if args["e0_stdout"]:
        run_cmd(
            [
                "stdout_test_e0",
            ]
        )

    if args["e4_stdout"]:
        run_cmd(
            [
                "stdout_test_e4",
            ]
        )

    if args["not_found"]:
        run_cmd(
            [
                "cmd_foo",
            ]
        )
