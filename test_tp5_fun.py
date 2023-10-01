import pytest
from tp5_fun import *

#Ejercicio 2
@pytest.mark.parametrize("word, num",[
    ("algo con limon",5),
    ("lala",4),
    ("por el emperador",9),
])
def test_leng_last_word(word,num):
    assert leng_last_word(word) == num

#Ejercicio 14
@pytest.mark.parametrize("n, bool",[
    (4,False),
    (9,True),
    (10,False),
])
def test_es_primo(n,bool):
    assert es_primo(n) == bool