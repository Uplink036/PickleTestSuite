import os
import pickle
import platform
import sys
import pytest
import hypothesis
from hashlib import sha256
from pickle import loads, dumps, PicklingError
from hypothesis import given, seed, strategies as st
from hypothesis.strategies import composite
from logger import save_unpickled_test
from logger import unpack_and_compare_single_test, get_os_and_version
from decimal import *

logger = True

@composite
def one_dim_random_strategy(draw):
    result = []
    result.append(draw(st.integers()))
    result.append(draw(st.floats()))
    result.append(draw(st.text()))
    result.append(draw(st.binary()))
    result.append(draw(st.booleans()))
    result.append(draw(st.just(None)))
    result.append(draw(st.just(Ellipsis)))
    result.append(draw(st.just(NotImplemented)))
    result.append(draw(st.complex_numbers()))

    ret = draw(st.sampled_from(result))
    return ret

class TestPickle:
    @seed(1234)
    @given(st.just(None))
    def test_none(self, data):
        try:
            dump_a1 = dumps(data)
            dump_a2 = dumps(data)
        except PicklingError as e:
            print(f"Error in pickling: {data} - error: {e}")
            return

        try:
            h_a1 = sha256(dump_a1).hexdigest()
            h_a2 = sha256(dump_a2).hexdigest()
        except Exception as e:
            print(f"Error in hashing: {data} - error: {e}")
            return

        assert h_a1 == h_a2
        if logger:
            save_unpickled_test(data)

    @seed(1234)
    @given(st.booleans())
    def test_booleans(self, data):
        try:
            dump_a1 = dumps(data)
            dump_a2 = dumps(data)
        except PicklingError as e:
            print(f"Error in pickling: {data} - error: {e}")
            return

        try:
            h_a1 = sha256(dump_a1).hexdigest()
            h_a2 = sha256(dump_a2).hexdigest()
        except Exception as e:
            print(f"Error in hashing: {data} - error: {e}")
            return

        assert h_a1 == h_a2
        if logger:
            save_unpickled_test(data)

    @seed(1234)
    @given(st.just(Ellipsis))
    def test_ellipsis(self, data):
        try:
            dump_a1 = dumps(data)
            dump_a2 = dumps(data)
        except PicklingError as e:
            print(f"Error in pickling: {data} - error: {e}")
            return

        try:
            h_a1 = sha256(dump_a1).hexdigest()
            h_a2 = sha256(dump_a2).hexdigest()
        except Exception as e:
            print(f"Error in hashing: {data} - error: {e}")
            return

        assert h_a1 == h_a2
        if logger:
            save_unpickled_test(data)

    @seed(1234)
    @given(st.just(NotImplemented))
    def test_notimplemented(self, data):
        try:
            dump_a1 = dumps(data)
            dump_a2 = dumps(data)
        except PicklingError as e:
            print(f"Error in pickling: {data} - error: {e}")
            return

        try:
            h_a1 = sha256(dump_a1).hexdigest()
            h_a2 = sha256(dump_a2).hexdigest()
        except Exception as e:
            print(f"Error in hashing: {data} - error: {e}")
            return

        assert h_a1 == h_a2
        if logger:
            save_unpickled_test(data)

    @seed(1234)
    @given(st.integers())
    def test_integers(self, data):
        try:
            dump_a1 = dumps(data)
            dump_a2 = dumps(data)
        except PicklingError as e:
            print(f"Error in pickling: {data} - error: {e}")
            return

        try:
            h_a1 = sha256(dump_a1).hexdigest()
            h_a2 = sha256(dump_a2).hexdigest()
        except Exception as e:
            print(f"Error in hashing: {data} - error: {e}")
            return

        assert h_a1 == h_a2
        if logger:
            save_unpickled_test(data)

    @seed(1234)
    @given(st.floats())
    def test_floats(self, data):
        try:
            dump_a1 = dumps(data)
            dump_a2 = dumps(data)
        except PicklingError as e:
            print(f"Error in pickling: {data} - error: {e}")
            return

        try:
            h_a1 = sha256(dump_a1).hexdigest()
            h_a2 = sha256(dump_a2).hexdigest()
        except Exception as e:
            print(f"Error in hashing: {data} - error: {e}")
            return

        assert h_a1 == h_a2
        if logger:
            save_unpickled_test(data)

    @seed(1234)
    @given(st.complex_numbers())
    def test_complex_numbers(self, data):
        try:
            dump_a1 = dumps(data)
            dump_a2 = dumps(data)
        except PicklingError as e:
            print(f"Error in pickling: {data} - error: {e}")
            return

        try:
            h_a1 = sha256(dump_a1).hexdigest()
            h_a2 = sha256(dump_a2).hexdigest()
        except Exception as e:
            print(f"Error in hashing: {data} - error: {e}")
            return

        assert h_a1 == h_a2
        if logger:
            save_unpickled_test(data)

    @seed(1234)
    @given(st.text())
    def test_text(self, data):
        try:
            dump_a1 = dumps(data)
            dump_a2 = dumps(data)
        except PicklingError as e:
            print(f"Error in pickling: {data} - error: {e}")
            return

        try:
            h_a1 = sha256(dump_a1).hexdigest()
            h_a2 = sha256(dump_a2).hexdigest()
        except Exception as e:
            print(f"Error in hashing: {data} - error: {e}")
            return

        assert h_a1 == h_a2
        if logger:
            save_unpickled_test(data)

    @seed(1234)
    @given(st.binary())
    def test_binary(self, data):
        try:
            dump_a1 = dumps(data)
            dump_a2 = dumps(data)
        except PicklingError as e:
            print(f"Error in pickling: {data} - error: {e}")
            return

        try:
            h_a1 = sha256(dump_a1).hexdigest()
            h_a2 = sha256(dump_a2).hexdigest()
        except Exception as e:
            print(f"Error in hashing: {data} - error: {e}")
            return

        assert h_a1 == h_a2
        if logger:
            save_unpickled_test(data)

    @seed(1234)
    @given(st.lists(st.integers(min_value=0, max_value=255)))
    def test_bytearrays(self, data):
        c = bytearray(data)
        try:
            dump_a1 = dumps(data)
            dump_a2 = dumps(data)
        except PicklingError as e:
            print(f"Error in pickling: {data} - error: {e}")
            return

        try:
            h_a1 = sha256(dump_a1).hexdigest()
            h_a2 = sha256(dump_a2).hexdigest()
        except Exception as e:
            print(f"Error in hashing: {data} - error: {e}")
            return

        assert h_a1 == h_a2
        if logger:
            save_unpickled_test(data)

    @seed(1234)
    @given(st.tuples(st.integers(), st.floats(), st.text(), st.binary(), st.booleans()))
    def test_tuples(self, data):
        try:
            dump_a1 = dumps(data)
            dump_a2 = dumps(data)
        except PicklingError as e:
            print(f"Error in pickling: {data} - error: {e}")
            return

        try:
            h_a1 = sha256(dump_a1).hexdigest()
            h_a2 = sha256(dump_a2).hexdigest()
        except Exception as e:
            print(f"Error in hashing: {data} - error: {e}")
            return

        assert h_a1 == h_a2
        if logger:
            save_unpickled_test(data)

    @seed(1234)
    @given(st.lists(elements=one_dim_random_strategy()))
    def test_lists(self, data):
        try:
            dump_a1 = dumps(data)
            dump_a2 = dumps(data)
        except PicklingError as e:
            print(f"Error in pickling: {data} - error: {e}")
            return

        try:
            h_a1 = sha256(dump_a1).hexdigest()
            h_a2 = sha256(dump_a2).hexdigest()
        except Exception as e:
            print(f"Error in hashing: {data} - error: {e}")
            return

        assert h_a1 == h_a2
        if logger:
            save_unpickled_test(data)


    @seed(1234)
    @given(st.sets(elements=one_dim_random_strategy()))
    def test_sets(self, data):
        try:
            dump_a1 = dumps(data)
            dump_a2 = dumps(data)
        except PicklingError as e:
            print(f"Error in pickling: {data} - error: {e}")
            return

        try:
            h_a1 = sha256(dump_a1).hexdigest()
            h_a2 = sha256(dump_a2).hexdigest()
        except Exception as e:
            print(f"Error in hashing: {data} - error: {e}")
            return

        assert h_a1 == h_a2
        if logger:
            save_unpickled_test(data)

    @seed(1234)
    @given(st.dictionaries(keys=st.text(), values=one_dim_random_strategy()))
    def test_dictionaries(self, data):
        try:
            dump_a1 = dumps(data)
            dump_a2 = dumps(data)
        except PicklingError as e:
            print(f"Error in pickling: {data} - error: {e}")
            return

        try:
            h_a1 = sha256(dump_a1).hexdigest()
            h_a2 = sha256(dump_a2).hexdigest()
        except Exception as e:
            print(f"Error in hashing: {data} - error: {e}")
            return

        assert h_a1 == h_a2
        if logger:
            save_unpickled_test(data)

    @seed(1234)
    @given(st.recursive(one_dim_random_strategy(), lambda children: st.lists(children)))
    def test_recursive_lists(self, data):
        try:
            dump_a1 = dumps(data)
            dump_a2 = dumps(data)
        except PicklingError as e:
            print(f"Error in pickling: {data} - error: {e}")
            return

        try:
            h_a1 = sha256(dump_a1).hexdigest()
            h_a2 = sha256(dump_a2).hexdigest()
        except Exception as e:
            print(f"Error in hashing: {data} - error: {e}")
            return

        assert h_a1 == h_a2
        if logger:
            save_unpickled_test(data)

    @seed(1234)
    @given(st.recursive(one_dim_random_strategy(), lambda children: st.frozensets(children)))
    def test_recursive_sets(self, data):
        try:
            dump_a1 = dumps(data)
            dump_a2 = dumps(data)
        except PicklingError as e:
            print(f"Error in pickling: {data} - error: {e}")
            return

        try:
            h_a1 = sha256(dump_a1).hexdigest()
            h_a2 = sha256(dump_a2).hexdigest()
        except Exception as e:
            print(f"Error in hashing: {data} - error: {e}")
            return

        assert h_a1 == h_a2
        if logger:
            save_unpickled_test(data)

    @seed(3124)
    @given(st.recursive(one_dim_random_strategy(), lambda children: st.dictionaries(keys=st.text(), values=children)))
    def test_recursive_dictionaries(self, data):
        try:
            dump_a1 = dumps(data)
            dump_a2 = dumps(data)
        except PicklingError as e:
            print(f"Error in pickling: {data} - error: {e}")
            return

        try:
            h_a1 = sha256(dump_a1).hexdigest()
            h_a2 = sha256(dump_a2).hexdigest()
        except Exception as e:
            print(f"Error in hashing: {data} - error: {e}")
            return

        assert h_a1 == h_a2
        if logger:
            save_unpickled_test(data)

    def test_pickle_from_other_version(self, protocol=pickle.DEFAULT_PROTOCOL,os_type=False,version_number=False):

        #If os is not given, we will use the running os and version
        running_os_type,running_version_number = get_os_and_version()
        if not os_type:
            os_type = running_os_type
        if not version_number:
            version_number = running_version_number

        log_destination = f"logs/{os_type}/{version_number}/protocol_{protocol}"
        # Check if the file exists
        if not os.path.exists(log_destination):
            # One can argue we should throw an error here.
            return
        # Checking how many test cases we have for the protocol
        count = 0
        for file in os.listdir(log_destination):
            count += 1
        count = count // 2

        for i in range(count):
            unpack_and_compare_single_test(i,protocol)

    def test_floating_point(self):
        '''Test to see how well the pickle handles extreme floatingpoint accuracy'''
        getcontext().prec = 309
        a = Decimal(2)**Decimal(0.5)
        b = Decimal(2.2250738585072014e-308)
        c = a+b
        c1 = pickle.dumps(a)
        s1 = sha256(c1).hexdigest()

        c2 = pickle.dumps(c)
        s2 = sha256(c2).hexdigest()

        assert s1 != s2

if __name__ == '__main__':
    pytest.main()
    print(st.recursive(st.integers(), lambda children: st.frozensets(children)).example())
