import pickle 
from hashlib import sha256
from pickle import loads, dumps
import pytest
import hypothesis
from hypothesis import given, seed, strategies as st
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
    @seed(1234)
    @given(st.just(None))
    def test_none(self, data):
        dump_a1 = dumps(data)
        dump_a2 = dumps(data)
        h_a1 = sha256(dump_a1).hexdigest()
        h_a2 = sha256(dump_a2).hexdigest()
       
        assert h_a1 == h_a2
    
    @seed(1234)
    @given(st.booleans())
    def test_booleans(self, data):
        dump_a1 = dumps(data)
        dump_a2 = dumps(data)
        h_a1 = sha256(dump_a1).hexdigest()
        h_a2 = sha256(dump_a2).hexdigest()
       
        assert h_a1 == h_a2
    
    @seed(1234)
    @given(st.just(Ellipsis))
    def test_ellipsis(self, data):
        dump_a1 = dumps(data)
        dump_a2 = dumps(data)
        h_a1 = sha256(dump_a1).hexdigest()
        h_a2 = sha256(dump_a2).hexdigest()
       
        assert h_a1 == h_a2
    
    @seed(1234)
    @given(st.just(NotImplemented))
    def test_notimplemented(self, data):
        dump_a1 = dumps(data)
        dump_a2 = dumps(data)
        h_a1 = sha256(dump_a1).hexdigest()
        h_a2 = sha256(dump_a2).hexdigest()
       
        assert h_a1 == h_a2
    
    @seed(1234)
    @given(st.integers())
    def test_integers(self, data):
        dump_a1 = dumps(data)
        dump_a2 = dumps(data)
        h_a1 = sha256(dump_a1).hexdigest()
        h_a2 = sha256(dump_a2).hexdigest()
       
        assert h_a1 == h_a2
    
    @seed(1234)
    @given(st.floats())
    def test_floats(self, data):
        dump_a1 = dumps(data)
        dump_a2 = dumps(data)
        h_a1 = sha256(dump_a1).hexdigest()
        h_a2 = sha256(dump_a2).hexdigest()
       
        assert h_a1 == h_a2
    
    @seed(1234)
    @given(st.complex_numbers())
    def test_complex_numbers(self, data):
        dump_a1 = dumps(data)
        dump_a2 = dumps(data)
        h_a1 = sha256(dump_a1).hexdigest()
        h_a2 = sha256(dump_a2).hexdigest()
       
        assert h_a1 == h_a2

    @seed(1234)
    @given(st.text())
    def test_text(self, data):
        dump_a1 = dumps(data)
        dump_a2 = dumps(data)
        h_a1 = sha256(dump_a1).hexdigest()
        h_a2 = sha256(dump_a2).hexdigest()
       
        assert h_a1 == h_a2
    
    @seed(1234)
    @given(st.binary())
    def test_binary(self, data):
        dump_a1 = dumps(data)
        dump_a2 = dumps(data)
        h_a1 = sha256(dump_a1).hexdigest()
        h_a2 = sha256(dump_a2).hexdigest()
       
        assert h_a1 == h_a2
    
    @seed(1234)
    @given(st.lists(st.integers(min_value=0, max_value=255)))
    def test_bytearrays(self, data):
        c = bytearray(data)
        dump_a1 = dumps(c)
        dump_a2 = dumps(c)
        h_a1 = sha256(dump_a1).hexdigest()
        h_a2 = sha256(dump_a2).hexdigest()

        assert h_a1 == h_a2

    @seed(1234)
    @given(st.tuples(st.integers(), st.floats(), st.text(), st.binary(), st.booleans()))
    def test_tuples(self, data):
        dump_a1 = dumps(data)
        dump_a2 = dumps(data)
        h_a1 = sha256(dump_a1).hexdigest()
        h_a2 = sha256(dump_a2).hexdigest()
       
        assert h_a1 == h_a2
    
    @seed(1234)
    @given(st.lists(elements=one_dim_random_strategy()))
    def test_lists(self, data):
        dump_a1 = dumps(data)
        dump_a2 = dumps(data)
        h_a1 = sha256(dump_a1).hexdigest()
        h_a2 = sha256(dump_a2).hexdigest()
       
        assert h_a1 == h_a2
    
    @seed(1234)
    @given(st.sets(elements=one_dim_random_strategy()))
    def test_sets(self, data):
        dump_a1 = dumps(data)
        dump_a2 = dumps(data)
        h_a1 = sha256(dump_a1).hexdigest()
        h_a2 = sha256(dump_a2).hexdigest()
       
        assert h_a1 == h_a2
    
    @seed(1234)
    @given(st.dictionaries(keys=st.text(), values=one_dim_random_strategy()))
    def test_dictionaries(self, data):
        dump_a1 = dumps(data)
        dump_a2 = dumps(data)
        h_a1 = sha256(dump_a1).hexdigest()
        h_a2 = sha256(dump_a2).hexdigest()
       
        assert h_a1 == h_a2

@seed(1234)
@given(st.integers())
def run(a):
    print(a)

run()



