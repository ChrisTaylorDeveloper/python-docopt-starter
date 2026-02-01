{ pkgs ? import <nixpkgs> {} }:

let
  ourCustomPyEnv = pkgs.python3.withPackages (ps: with ps; [
    pip
    pyinstaller
    virtualenv
    requests
    docopt
  ]);
in

pkgs.mkShell {
  buildInputs = [
    ourCustomPyEnv
  ];

  shellHook = ''
    echo "Starting Python Dev Shell with $(python --version)"
    if [ ! -d ".venv" ]; then
      python -m venv .venv
    fi
    source .venv/bin/activate
  '';
}
