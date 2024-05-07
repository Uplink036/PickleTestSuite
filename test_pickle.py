import pickle 
from hashlib import sha256
from pickle import loads, dumps
import pytest
import hypothesis
from hypothesis import given, strategies as st

class TestPickle:
    def test_pickle(self):
        data = {'a': 1, 'b': 2, 'c': 3}
        with open('data.pickle', 'wb') as f:
            pickle.dump(data, f)
        with open('data.pickle', 'rb') as f:
            data = pickle.load(f)
        assert data == {'a': 1, 'b': 2, 'c': 3}
    
    @given(st.sampled_from([None, True, False, Ellipsis, NotImplemented]))
    def test_builtins(self, a):
        dump_a = dumps(a)
        loads_a = loads(dump_a)
       
        assert sha256(a) == sha256(loads_a)
        
        

    @given(st.integers(), st.floats(), st.complex_numbers())
    def test_numbers(self, a, b, c):
        dump_a = dumps(a)
        dump_b = dumps(b)
        dump_c = dumps(c)
        loads_a = loads(dump_a)
        loads_b = loads(dump_b)
        loads_c = loads(dump_c)

        assert sha256(a) == sha256(loads_a)
        assert sha256(b) == sha256(loads_b)
        assert sha256(c) == sha256(loads_c)

    #Maybe consider utf-16
    #given strings, bytes, bytearrays (from ints is what I've done)
    @given(st.text(), st.binary(), st.lists(st.integers()))
    def test_strings(self, a, b, c):
        c = bytearray(c)
        dump_a = dumps(a)
        dump_b = dumps(b)
        dump_c = dumps(c)
        loads_a = loads(dump_a)
        loads_b = loads(dump_b)
        loads_c = loads(dump_c)

        assert sha256(a) == sha256(loads_a)
        assert sha256(b) == sha256(loads_b)
        assert sha256(c) == sha256(loads_c)
    
    @given(st.tuples(st.integers(), st.floats(), st.text(), st.lists(st.integers()), st.binary(), st.booleans()),
           st.lists([st.integers(), st.floats(), st.text(), st.lists(st.integers()), st.binary(), st.booleans()]),
           st.sets([st.integers(), st.floats(), st.text(), st.lists(st.integers()), st.binary(), st.booleans()]),
           st.dictionaries(keys=st.text(), values=[st.integers(), st.floats(), st.text(), st.lists(st.integers()), st.binary(), st.booleans()]))
    
    def test_collections(self, a, b, c, d):
        dump_a = dumps(a)
        dump_b = dumps(b)
        dump_c = dumps(c)
        dump_d = dumps(d)
        loads_a = loads(dump_a)
        loads_b = loads(dump_b)
        loads_c = loads(dump_c)
        loads_d = loads(dump_d)

        assert sha256(a) == sha256(loads_a)
        assert sha256(b) == sha256(loads_b)
        assert sha256(c) == sha256(loads_c)
        assert sha256(d) == sha256(loads_d)
    
    @given(st.functions())
    def test_functions(self, a):
        dump_a = dumps(a)
        loads_a = loads(dump_a)

        assert sha256(a) == sha256(loads_a)
    

    
