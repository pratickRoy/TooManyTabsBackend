from gensim.models import KeyedVectors
import nltk
from nltk.tokenize import word_tokenize
import numpy as np

# load the google word2vec model
filename = '../commons/GoogleNews-vectors-negative300.bin'
print("train begin")
model = KeyedVectors.load_word2vec_format(filename, binary=True)
print("train end")


def transform(string):

    avg_word_vector = np.asarray([0.0 for _ in range(300)])

    if not isinstance(string, str):
        return avg_word_vector

    words = string.replace("\n", " ").split()

    for word in words:
        vector = get_vector_for_word(word)
        if vector is not None:
            for i, point in enumerate(vector):
                value = avg_word_vector[i] + vector[i]/len(words)
                avg_word_vector[i] = value
    return avg_word_vector


def get_vector_for_word(word):
    if word in model.vocab:
        return model.word_vec(word)
    else:
        return None
