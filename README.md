# Python docopt starter project

## Getting started

1 Start a Nix dev shell (if required)

```shell
nix-shell
```

2 Install docopt

```shell
pip install docopt
```

3 Run a dist build

```shell
pyinstaller --paths=/.venv/lib/python3.13/site-packages/ --onefile pydo.py
```

4 Install on Linux

```shell
install ./dist/pydo /home/"$USER"/.local/bin/pydo
```

## Test utils

Create test commands

```shell
gcc -o stderr_test_e0 stderr_test_e0.c
gcc -o stderr_test_e4 stderr_test_e4.c
gcc -o stdout_test_e0 stdout_test_e0.c
gcc -o stdout_test_e4 stdout_test_e4.c
```

Install test commands

```shell
install ./stderr_test_e0 /home/"$USER"/.local/bin/stderr_test_e0
install ./stderr_test_e4 /home/"$USER"/.local/bin/stderr_test_e4
install ./stdout_test_e0 /home/"$USER"/.local/bin/stdout_test_e0
install ./stdout_test_e4 /home/"$USER"/.local/bin/stdout_test_e4
```
