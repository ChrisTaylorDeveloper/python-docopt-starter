# Python docopt starter project

## Getting started

Start a Nix dev shell (if required)

```shell
nix-shell
```

Install docopt

```shell
pip install docopt
```

Run a dist build

```shell
pyinstaller --paths=/.venv/lib/python3.13/site-packages/ --onefile pydo.py
```

Install on Linux

```shell
install ./dist/pydo /home/"$USER"/.local/bin/pydo
```

## Test utils

Create test binaries

```shell
gcc -o stderr_test_e0 stderr_test_e0.c
gcc -o stderr_test_e4 stderr_test_e4.c
gcc -o stdout_test_e0 stdout_test_e0.c
gcc -o stdout_test_e4 stdout_test_e4.c
```

Install test binaries

```shell
install ./stderr_test_e0 /home/"$USER"/.local/bin/stderr_test_e0
install ./stderr_test_e4 /home/"$USER"/.local/bin/stderr_test_e4
install ./stdout_test_e0 /home/"$USER"/.local/bin/stdout_test_e0
install ./stdout_test_e4 /home/"$USER"/.local/bin/stdout_test_e4
```
