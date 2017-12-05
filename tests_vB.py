import pytest
from ex01 import count_au

def test_count_au_0():
  assert(count_au(42)==0)

def test_count_au_1():
  assert(count_au('mai')==1)

def test_count_au_2():
  assert(count_au('MAYA')==2)

def test_count_au_3():
  assert(count_au('maui')==2)

def test_count_au_4():
  assert(count_au('moana')==2)

def test_count_au_5():
  assert(count_au('Auckland')==3)

from ex01 import minOfTwoLists

def test_minOfTwoLists_0():
  assert(minOfTwoLists(42, [1])==False)

def test_minOfTwoLists_1():
  assert(minOfTwoLists(['ox'],['cat'])==['ox'])

def test_minOfTwoLists_2():
  assert(minOfTwoLists(['ox','bear'],['cat', 'cow'])==['ox', 'cow'])

def test_minOfTwoLists_3():
  assert(minOfTwoLists(['bear','cow'],['ox','cat'])==['ox', 'cow'])

def test_minOfTwoLists_4():
  assert(minOfTwoLists(['bear','cow','crow','sparrow'],\
                       ['ox','cat','mouse','ox'])==\
                       ['ox', 'cow','crow','ox'])
  
def test_minOfTwoLists_5():
  assert(minOfTwoLists(['bear','cow','crow'],['ox','cat','mouse'])==\
         ['ox', 'cow','crow'])

