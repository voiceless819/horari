#!/bin/bash
cd "$(dirname "$0")"
python3 sync.py
echo
read -n 1 -s -r -p "Pulsa una tecla para cerrar..."
