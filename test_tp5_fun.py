import pytest
from tp5_fun import *

#Ejercicio 1
@pytest.mark.parametrize("dni,dni_correct",[
    ("123456",False),
    ("12345678",True),
    ("1234567",True),
])
def test_document(dni, dni_correct):
    assert document(dni) == dni_correct

#Ejercicio 2
@pytest.mark.parametrize("word, num",[
    ("algo con limon",5),
    ("lala",4),
    ("por el emperador",9),
])
def test_leng_last_word(word,num):
    assert leng_last_word(word) == num

#Ejercicio 3
@pytest.mark.parametrize("name1, name2, lastname, fullname",[
    ("juanin","juan","harry","juanin juan harry"),
    ("juan","carlos","bodoque","juan carlos bodoque"),
    ("mario","0","hugo","mario hugo"),
])
def test_user_name (name1, name2, lastname, fullname):
    assert user_name (name1, name2, lastname) == "Nombre del usuario:" + fullname

#Ejercicio 4
@pytest.mark.parametrize('a,res',[
    (-1,False),
    (2,True),
])
def test_data_validation(a,res):
    assert data_validation(a) == res

#Ejercicio 5
@pytest.mark.parametrize("min_temperature, max_temperature, med_temperature",[
    (9,8,8.5),
    (10,5,7.5),
    (14,6,10),
])
def test_temperature_middle(min_temperature, max_temperature, med_temperature):
    assert temperature_middle(min_temperature, max_temperature) == med_temperature

#Ejercicio 6
@pytest.mark.parametrize("sentence, sentence_separate",[
    ("algo con limon","a l g o   c o n   l i m o n"),
    ("lala","l a l a"),
    ("por el emperador","p o r   e l   e m p e r a d o r"),
])
def test_separator(sentence, sentence_separate):
    assert separator(sentence) == sentence_separate

#Ejercicio 7

#Ejercicio 8
@pytest.mark.parametrize("n,result_per",[
    (3,18.85),
    (5,31.42),
    (23,144.51),
])
def test_calculo_perim(n,result_per):
    assert calculo_perim(n)==result_per
@pytest.mark.parametrize("n,result_are",[
    (3,88.83),
    (5,246.74),
    (23,5221.02),
])
def test_calculo_area(n,result_are):
    assert calculo_area(n)==result_are

#Ejercicio 9

#Ejercicio 10

#Ejercicio 11

#Ejercicio 12

#Ejercicio 13

#Ejercicio 14
@pytest.mark.parametrize("n, bool",[
    (4,False),
    (9,True),
    (10,False),
])
def test_es_primo(n,bool):
    assert es_primo(n) == bool

#Ejercicio 15
@pytest.mark.parametrize("n, fact",[
    (4,24),
    (9,362880),
    (3,6),
])
def test_factorial(n, fact):
    assert factorial(n) == fact

#Ejercicio 16

#Ejercicio 17


#pip install pytest 
#python -m pytest
#python -m pytest test_tp5_fun.py
#python -m pytest -v