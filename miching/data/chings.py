import os
import pickle


current_dir = os.path.dirname(os.path.realpath(__file__))

class Chings:

    def __init__(self, filename):
        self.filename = filename
        self.__data = None
    
    def __getitem__(self, key):
        if self.__data is None:
            # print('load data from {}'.format(self.filename))
            with open(os.path.join(current_dir, self.filename), 'rb') as rf:
                self.__data = pickle.load(rf)
        return self.__data[key]


horoscopes = Chings('horoscopes.pkl')

iching_txt = Chings('iching_zh.pkl')

hexagrams = Chings('hexagrams.pkl')
