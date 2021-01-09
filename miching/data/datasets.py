import os
import json
import jieba
from itertools import islice
from gensim.models import Word2Vec


def stop_words(file = None):
    if file is None:
        current_dir = os.path.dirname(os.path.realpath(__file__))
        file = os.path.join(current_dir, 'stopwords.txt')
    with open(file, 'r', encoding='utf8') as rf:
        lines = rf.readlines()
        return [line.replace('\n', '').strip() for line in lines]


class Word2VecModel:

    def __init__(self, path, batch_size = 128, output = 'model/word_embeddings.model'):
        self.path = path
        self.batch_size = batch_size
        self.output = output
        self.model = Word2Vec(size=300, window=5, min_count=1, workers=4)

    def batch_data(self):
        stopwords = stop_words()
        with open(self.path, 'r', encoding = 'utf8') as rf:
            while True:
                sentences = []
                lines = list(islice(rf, self.batch_size))
                if not lines: break
                for line in lines:
                    title = json.loads(line)['title'].strip().lower()
                    words = jieba.lcut(title)
                    sentences.append([word for word in words if word not in stopwords])
                yield sentences

    def train(self):
        for sentences in self.batch_data():
            self.model.build_vocab(sentences, update=True)
        self.model.train(None, total_examples=self.model.corpus_count, epochs = 10)
        self.model.save(self.output)

    def restore(self, path=None):
        pass



# sentences = QACorpus('E:/java/other/iching/docs/chings/TaoTeChing.txt')
# model = Word2Vec(sentences = sentences, window=5, min_count=1, workers=4)
# print(model.wv['道德'])
# print(model.wv.most_similar('道德'))

model = Word2VecModel('E:/datasets/QA/webtext2019zh/web_text_zh_testa.json')
model.train()
