# Python docopt starter project

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
