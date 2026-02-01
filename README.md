# Python docopt starter project

1. Start a Nix dev shell

```shell
nix-shell
```

1. Install docopt

```shell
pip install docopt
```

1. Run a dist build

```shell
pyinstaller --paths=/.venv/lib/python3.13/site-packages/ --onefile pydo.py
```

1. Install on Linux

```shell
install ./dist/pydo /home/"$USER"/.local/bin/pydo
```
