import pickle
import os
import pytest
import platform
import sys

class TestPickle:
    def test_pickle(self):
        data = {'a': 1, 'b': 2, 'c': 3}
        with open('data.pickle', 'wb') as f:
            pickle.dump(data, f)
        with open('data.pickle', 'rb') as f:
            data = pickle.load(f)
        assert data == {'a': 1, 'b': 2, 'c': 3}

if __name__ == '__main__':
    print(os.name)
    print(sys.version)
    pytest.main()
