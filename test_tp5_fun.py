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
@pytest.mark.parametrize("a,b,res",[
    (8,2,8),
    (5,2,False),
    (10,10,True),
    (3,6,6),
])
def test_is_multiple(a,b,res):
    assert is_multiple(a,b) == res
@pytest.mark.parametrize("a,res",[
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
@pytest.mark.parametrize('list,res',[
    ([1,15,5,-2],[15,-2]),
    ([1,2,3],[3,1]),
])
def test_max_min(list,res):
    assert max_min(list) == res

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
@pytest.mark.parametrize("username, password, attempts, result", [
    ("usuario1", "asdasd", 3, True), 
    ("Juan", "Pérez", 3, 4),
    ])
def test_login(username, password, attempts, result):
    result = login(username, password, attempts)
    assert login(username, password, attempts) == result

#Ejercicio 10
@pytest.mark.parametrize('dic,res',[
    ({3500: '20%', 14200: '35%', 5700: '10%', 12000: '20%', 7800: '10%'},[43200,33780.0]),
])
def test_total(dic,res):
    assert total(dic) == res

#Ejercicio 11
@pytest.mark.parametrize("element, result", [(6, 12), (14, 28), (8, 16)])
def test_product(element, result):
    assert product(element) == result
def product(element):
    return element * 2
@pytest.mark.parametrize("product, numbers, result", [(product, [2,4,5], [4,8,10]), (product, [3,5,7], [6,10,14]), (product, [1,12,6], [2,24,12])])
def test_apply_function(product, numbers, result):
    assert apply_function(product, numbers) == result

#Ejercicio 12
@pytest.mark.parametrize("all_keys",[
    ("Buenas tardes"),
])
def test_define_keys(all_keys):
    assert define_keys(all_keys)==all_keys
@pytest.mark.parametrize("all_words, dict_text",[
    (["Buenas"], {"Buenas": 6})
])
def test_transform_dict(all_words,dict_text):
    assert transform_dict(all_words)==dict_text

#Ejercicio 13
@pytest.mark.parametrize("x, y, z, expected_result", [
(0, 0, 0, 0), (3, 4, 0, 5), (-2, -3, -6, 7)])
def test_vector_module(x, y, z, expected_result):
    assert vector_module(x, y, z) == expected_result

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
@pytest.mark.parametrize("number, digit, counter",[
    (23,3,1),
    (277,7,2)
])
def test_frecuency(number,digit,counter):
    assert frecuency(number,digit)==counter

#Ejercicio 17
@pytest.mark.parametrize("number,add_numbers",[
    (23,5),
    (7,7),
])
def test_addiging_digits(number,add_numbers):
    assert addiging_digits(number)==add_numbers

#pip install pytest 
#python -m pytest
#python -m pytest test_tp5_fun.py
#python -m pytest -v