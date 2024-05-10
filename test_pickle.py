import pickle
import pytest
import random
from hashlib import sha256
from pickle import dumps, PicklingError
from hypothesis import settings, given, seed, strategies as st
from hypothesis.strategies import composite
from logger import save_unpickled_test,clean_folder
from classes_functions import *
from decimal import *

settings.register_profile("first", max_examples=100, deadline=None)
settings.load_profile("first")

logger = True

@composite
def one_dim_random_strategy(draw):
    result = []
    result.append(draw(st.integers()))
    result.append(draw(st.floats(allow_nan=False)))
    result.append(draw(st.text()))
    result.append(draw(st.booleans()))
    result.append(draw(st.binary()))
    result.append(draw(st.just(None)))
    result.append(draw(st.just(Ellipsis)))
    result.append(draw(st.just(NotImplemented)))
    result.append(draw(st.complex_numbers(allow_nan=False)))

    ret = draw(st.sampled_from(result))
    return ret

# @composite
# def two_dim_random_strategy(draw):
#     result = []
#     result.append(draw(st.integers()))
#     result.append(draw(st.floats(allow_nan=False)))
#     result.append(draw(st.text()))
#     result.append(draw(st.booleans()))
#     result.append(draw(st.binary()))
#     result.append(draw(st.just(None)))
#     result.append(draw(st.just(Ellipsis)))
#     result.append(draw(st.just(NotImplemented)))
#     result.append(draw(st.complex_numbers(allow_nan=False)))
#     result.append(draw(st.lists(elements=one_dim_random_strategy())))
#     result.append(draw(st.sets(elements=one_dim_random_strategy())))
#     result.append(draw(st.dictionaries(keys=st.text(), values=one_dim_random_strategy())))
#     result.append(draw(st.tuples(st.integers(), st.floats(allow_nan=False), st.text(), st.booleans())))


#     ret = draw(st.sampled_from(result))
#     return ret

class TestPickle:
    @seed(1)
    @given(st.just(None))
    def test_none(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="None", protocol=i)

    @seed(2)
    @given(st.booleans())
    def test_booleans(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(h_a1, comment="Boolean", protocol=i)

    @seed(3)
    @given(st.just(Ellipsis))
    def test_ellipsis(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="Ellipsis", protocol=i)

    @seed(4)
    @given(st.just(NotImplemented))
    def test_notimplemented(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="NotImplemented", protocol=i)

    @seed(5)
    @given(st.integers())
    def test_integers(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="Integer",json_data = str(data), protocol=i)

    @seed(6)
    @given(st.floats(allow_nan=False))
    def test_floats(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(h_a1, comment="Float",json_data = str(data), protocol=i)

    @seed(7)
    @given(st.complex_numbers(allow_nan=False))
    def test_complex_numbers(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="Complex", protocol=i)

    @seed(8)
    @given(st.text())
    def test_text(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="String", protocol=i)

    @seed(9)
    @given(st.binary())
    def test_binary(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="Bytes", protocol=i)

    @seed(10)
    @given(st.lists(st.integers(min_value=0, max_value=255)))
    def test_bytearrays(self, data):
        c = bytearray(data)
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="Bytearray", protocol=i)

    @seed(11)
    @given(st.tuples(st.integers(), st.floats(allow_nan=False), st.text(), st.booleans()))
    def test_tuples(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="Tuple", protocol=i)

    @seed(12)
    @given(st.lists(elements=one_dim_random_strategy()))
    def test_lists(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="List", protocol=i)


    @seed(13)
    @given(st.sets(elements=one_dim_random_strategy()))
    def test_sets(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="Set", protocol=i)

    @seed(14)
    @given(st.dictionaries(keys=st.text(), values=one_dim_random_strategy()))
    def test_dictionaries(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="Dictionary", protocol=i)

    @seed(15)
    @given(st.recursive(one_dim_random_strategy(), lambda children: st.lists(children)))
    def test_recursive_lists(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="Recursive List", protocol=i)

    @seed(16)
    @given(st.recursive(one_dim_random_strategy(), lambda children: st.frozensets(children)))
    def test_recursive_sets(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="Recursive Set", protocol=i)

    @seed(17)
    @given(st.recursive(one_dim_random_strategy(), lambda children: st.dictionaries(keys=st.text(), values=children)))
    def test_recursive_dictionaries(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="Recursive Dictionary", protocol=i)
    @seed(18)
    @given(st.sampled_from([add_function, is_prime, tri_recursion, get_lengths]))
    def test_functions(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="Function", protocol=i)
    @seed(19)
    @given(st.sampled_from([Student, Person, Temperature]))
    def test_classes(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="Class", protocol=i)

    @seed(20)
    @given(st.sampled_from([Student("Tobias", 21), Person("Oliver", 21), Temperature(37)]))
    def test_instances(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="Instance", protocol=i)

    def test_floating_point(self):
        '''Test to see how well the pickle handles extreme floatingpoint accuracy'''
        getcontext().prec = 309
        a = Decimal(2)**Decimal(0.5)
        b = Decimal(2.2250738585072014e-308)
        c = a+b
        c1 = dumps(a)
        s1 = sha256(c1).hexdigest()

        c2 = dumps(c)
        s2 = sha256(c2).hexdigest()

        assert s1 != s2

if __name__ == '__main__':
    clean_folder()
    pytest.main()
