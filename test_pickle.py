import pickle 
from hashlib import sha256
from pickle import loads, dumps
import pytest
import hypothesis
from hypothesis import given, strategies as st
from hypothesis.strategies import composite

@composite
def one_dim_random_strategy(draw):
    result = []
    result.append(draw(st.integers()))
    result.append(draw(st.floats()))
    result.append(draw(st.text()))
    result.append(draw(st.binary()))
    result.append(draw(st.booleans()))
    ret = draw(st.sampled_from(result))
    return ret

class TestPickle:
    def test_pickle(self):
        data = {'a': 1, 'b': 2, 'c': 3}
        with open('data.pickle', 'wb') as f:
            pickle.dump(data, f)
        with open('data.pickle', 'rb') as f:
            data = pickle.load(f)
        assert data == {'a': 1, 'b': 2, 'c': 3}
    
    @given(st.sampled_from([None, True, False, Ellipsis, NotImplemented]))
    def test_builtins(self, data):
        dump_a1 = dumps(data)
        dump_a2 = dumps(data)
        h_a1 = sha256(dump_a1).hexdigest()
        h_a2 = sha256(dump_a2).hexdigest()
       
        assert h_a1 == h_a2
        
    @given(st.integers(), st.floats(allow_nan=False), st.complex_numbers(allow_nan=False))
    def test_numbers(self, a, b, c):
        dump_a1 = dumps(a)
        dump_a2 = dumps(a)
        h_a1 = sha256(dump_a1).hexdigest()
        h_a2 = sha256(dump_a2).hexdigest()

        dump_b1 = dumps(b)
        dump_b2 = dumps(b)
        h_b1 = sha256(dump_b1).hexdigest()
        h_b2 = sha256(dump_b2).hexdigest()

        dump_c1 = dumps(c)
        dump_c2 = dumps(c)
        h_c1 = sha256(dump_c1).hexdigest()
        h_c2 = sha256(dump_c2).hexdigest()

        assert h_a1 == h_a2
        assert h_b1 == h_b2
        assert h_c1 == h_c2
        

    #Maybe consider utf-16
    #given strings, bytes, bytearrays (from ints is what I've done)
    @given(st.text(), st.binary(), st.lists(st.integers(min_value=0, max_value=255)))
    def test_strings(self, a, b, c):
        c = bytearray(c)

        dump_a1 = dumps(a)
        dump_a2 = dumps(a)
        h_a1 = sha256(dump_a1).hexdigest()
        h_a2 = sha256(dump_a2).hexdigest()

        dump_b1 = dumps(b)
        dump_b2 = dumps(b)
        h_b1 = sha256(dump_b1).hexdigest()
        h_b2 = sha256(dump_b2).hexdigest()

        dump_c1 = dumps(c)
        dump_c2 = dumps(c)
        h_c1 = sha256(dump_c1).hexdigest()
        h_c2 = sha256(dump_c2).hexdigest()

        assert h_a1 == h_a2
        assert h_b1 == h_b2
        assert h_c1 == h_c2


    @given(st.tuples(st.integers(), st.floats(), st.text(), st.binary(), st.booleans()),
           st.lists(elements=one_dim_random_strategy()),
           st.sets(elements=one_dim_random_strategy()),
           st.dictionaries(keys=st.text(), values=one_dim_random_strategy()))
    def test_collections(self, a, b, c, d):
        dump_a1 = dumps(a)
        dump_a2 = dumps(a)
        h_a1 = sha256(dump_a1).hexdigest()
        h_a2 = sha256(dump_a2).hexdigest()

        dump_b1 = dumps(b)
        dump_b2 = dumps(b)
        h_b1 = sha256(dump_b1).hexdigest()
        h_b2 = sha256(dump_b2).hexdigest()

        dump_c1 = dumps(c)
        dump_c2 = dumps(c)
        h_c1 = sha256(dump_c1).hexdigest()
        h_c2 = sha256(dump_c2).hexdigest()

        dump_d1 = dumps(d)
        dump_d2 = dumps(d)
        h_d1 = sha256(dump_d1).hexdigest()
        h_d2 = sha256(dump_d2).hexdigest()

        assert h_a1 == h_a2
        assert h_b1 == h_b2
        assert h_c1 == h_c2
        assert h_d1 == h_d2
    
    # @given(st.functions(pure=True))
    # def test_functions(self, a):
    #     dump_a1 = dumps(a)
    #     dump_a2 = dumps(a)
    #     h_a1 = sha256(dump_a1).hexdigest()
    #     h_a2 = sha256(dump_a2).hexdigest()

    #     assert h_a1 == h_a2

