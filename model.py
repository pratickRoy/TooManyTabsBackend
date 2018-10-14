
# coding: utf-8

# In[290]:


import io
import json
import gensim.downloader as api
import numpy as np
from sklearn.cluster import *


# In[76]:


with io.open('/Users/avirald/Desktop/final-input.json') as inp_f:
    INPUT_DATA = json.load(inp_f)

print(len(INPUT_DATA))

INPUT_DATA = [_ for _ in INPUT_DATA if 'text_content' in _]

print(len(INPUT_DATA))

WORD2VEC_MODEL_PATH = '/Users/avirald/Downloads/GoogleNews-vectors-negative300.bin'


# In[6]:

MODEL = 'glove-twitter-25'
print(api.load(MODEL, return_path=True))
word2vec_model = api.load(MODEL)
print(word2vec_model.most_similar('computer'))


# In[219]:


def doc2vec(doc):
    vectors = []
    for word in doc:
        if word in word2vec_model:
            vectors.append(word2vec_model[word])
        else:
            vectors.append(np.zeros(25))
    return np.mean(vectors, axis=0)
    # return np.concatenate([np.min(vectors, axis=0), np.max(vectors, axis=0)])


# In[220]:


print(doc2vec('the quick brown fox jumped over the lazy dog'))


# In[221]:


from scipy.cluster.vq import vq, kmeans2, whiten


# In[260]:


NON_CONTENT_FEATURES = ["p", "pre", "code", "video"]
def non_content_feature_vector(data):
    r = np.array([data.get(feature_name, 0) for feature_name in NON_CONTENT_FEATURES])
#     print(r)
    return r


# In[281]:


INPUT_DATA_VECS = np.array([
    np.concatenate([doc2vec(data['text_content'])])
    for data in INPUT_DATA])


# In[266]:


print(INPUT_DATA_VECS)
INPUT_DATA_VECS_WHITENED = whiten(INPUT_DATA_VECS)
print(INPUT_DATA_VECS_WHITENED)


# In[291]:


OUTPUT = SpectralClustering().fit(INPUT_DATA_VECS).labels_ #kmeans2(INPUT_DATA_VECS_WHITENED, 2, iter=1000)
OUTPUT_LABELS = OUTPUT#[1]
print(OUTPUT_LABELS)


# In[292]:


import collections
OUTPUT_GROUPS = collections.defaultdict(list)
for i, v in enumerate(OUTPUT_LABELS):
    OUTPUT_GROUPS[v].append(INPUT_DATA[i]['title'])
OUTPUT_GROUPS = {k: sorted(v) for k, v in OUTPUT_GROUPS.items()}


# In[293]:


import pprint
pprint.pprint(OUTPUT_GROUPS)


# In[106]:

