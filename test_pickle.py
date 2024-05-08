import pickle
import os
import pytest
import platform
import sys
from logger import unpack_and_compare_single_test, get_os_and_version
from hashlib import sha256

class TestPickle:
    def test_pickle(self):
        data = {'a': 1, 'b': 2, 'c': 3}
        with open('data.pickle', 'wb') as f:
            pickle.dump(data, f)
        with open('data.pickle', 'rb') as f:
            data = pickle.load(f)
        assert data == {'a': 1, 'b': 2, 'c': 3}

    def test_pickle_from_other_version(self, protocol=pickle.DEFAULT_PROTOCOL,os_type=False,version_number=False):

        #If os is not given, we will use the running os and version
        running_os_type,running_version_number = get_os_and_version()
        if not os_type:
            os_type = running_os_type
        if not version_number:
            version_number = running_version_number

        # Checking how many test cases we have for the protocol
        count = 0
        for file in os.listdir(f"logs/{os_type}/{version_number}/protocol_{protocol}"):
            count += 1
        count = count // 2

        for i in range(count):
            unpack_and_compare_single_test(i,protocol)

if __name__ == '__main__':
    pytest.main()
