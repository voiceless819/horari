#!/usr/bin/env python3
"""Sube la carpeta 'horarios' a GitHub una sola vez (al ejecutarlo)."""
import subprocess, sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def git(*args, check=True):
    return subprocess.run(["git", *args], cwd=ROOT, text=True, capture_output=True, check=check)

def main():
    if not (ROOT / ".git").exists():
        sys.exit("Esta carpeta no es un repositorio git. Sigue los pasos del README.")
    (ROOT / "horarios").mkdir(exist_ok=True)
    git("add", "-A", "horarios")
    if git("diff", "--cached", "--quiet", check=False).returncode == 0:
        print("No hay cambios nuevos en la carpeta horarios.")
        return
    git("commit", "-m", f"Actualizar horarios ({datetime.now():%Y-%m-%d %H:%M})")
    pull = git("pull", "--rebase", "--autostash", check=False)
    if pull.returncode != 0:
        print("Aviso al hacer pull:", pull.stderr.strip())
    res = git("push", check=False)
    if res.returncode == 0:
        print("Subido a GitHub. La web se actualizará en 1-2 minutos.")
    else:
        sys.exit("ERROR al hacer push:\n" + res.stderr.strip())

if __name__ == "__main__":
    main()
