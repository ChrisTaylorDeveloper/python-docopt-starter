{ pkgs ? import <nixpkgs> {} }:

let
  pyEnv = pkgs.python3.withPackages (ps: with ps; [
    # docopt # Not working here.
    pip
    pyinstaller
    virtualenv
    requests
  ]);
in

pkgs.mkShell {
  buildInputs = [ pyEnv ];
  shellHook = ''
    echo "Starting Python Dev Shell with $(python --version)"
    if [ ! -d ".venv" ]; then
      python -m venv .venv
    fi
    source .venv/bin/activate
  '';
}
