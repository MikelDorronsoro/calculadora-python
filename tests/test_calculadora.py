# tests/test_calculadora.py

import os
import sys

# Añadimos la carpeta raíz del proyecto al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from calculadora import sumar


def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0
