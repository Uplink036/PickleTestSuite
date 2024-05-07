import logging
import pickle

logger = logging.getLogger(__name__)

def pickle_saver(data,func,protocol="DEFAULT_PROTOCOL"):
    pickle_object = pickle.dumps(data, protocol=pickle.HIGHEST_PROTOCOL)
    with open(f'{func}.pkl', 'wb') as f:
        f.write(pickle_object)


def test():
    data = {'a': 1, 'b': 2, 'c': 3}
    pickle_saver(data,'test_pickle')


if __name__ == '__main__':
    test()
