import io
import json
import gensim.downloader as api
import numpy as np

with io.open('../kmeansclustering/sample_json.json') as inp_f:
    INPUT_DATA = json.load(inp_f)

print(len(INPUT_DATA))

INPUT_DATA = [_ for _ in INPUT_DATA if 'text_content' in _]

print(len(INPUT_DATA))

WORD2VEC_MODEL_PATH = '/Users/avirald/Downloads/GoogleNews-vectors-negative300.bin'

word2vec_model = api.load('word2vec-google-news-300')
word2vec_model.most_similar('computer')