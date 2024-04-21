import pickle 

class TestPickle:
    def test_pickle(self):
        data = {'a': 1, 'b': 2, 'c': 3}
        with open('data.pickle', 'wb') as f:
            pickle.dump(data, f)
        with open('data.pickle', 'rb') as f:
            data = pickle.load(f)
        assert data == {'a': 1, 'b': 2, 'c': 3}