import pytest

# Fonction test du résultat de 2+4


def test_calc_addition():

    output = 2 + 4
    assert output == 6


# Fonction test du résultat de 2-4

def test_calc_substraction():
    output = 2 - 4
    assert output == -2

# Fonction test du résultat de 2*4


def test_calc_multiply():
    output = 2 * 4
    assert output == 8

 # Fonction test si le résultat renvoie 'hello'


def test_coucou():
    output = 'hello'
    assert output == 'hello'
