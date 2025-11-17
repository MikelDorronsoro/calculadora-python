# tests/test_calculadora.py

import os
import sys
import pytest

# Aseguramos que la carpeta raíz del proyecto está en el path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from calculadora import sumar, restar, multiplicar, dividir


def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0


def test_restar():
    assert restar(5, 3) == 2
    assert restar(3, 5) == -2
    assert restar(0, 0) == 0


def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(-2, 3) == -6
    assert multiplicar(0, 10) == 0


def test_dividir():
    assert dividir(6, 3) == 2
    assert dividir(5, 2) == 2.5


def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(5, 0)

