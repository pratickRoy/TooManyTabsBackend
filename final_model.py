
# coding: utf-8

import string
import collections
import nltk
from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from pprint import pprint

nltk.download('stopwords')
nltk.download('punkt')

def process_text(text, stem=True):
    text = text.translate(str.maketrans('','',string.punctuation))
    tokens = word_tokenize(text)

    if stem:
        stemmer = PorterStemmer()
        tokens = [stemmer.stem(t) for t in tokens]

    return tokens


def cluster(texts, clusters=3):
    vectorizer = TfidfVectorizer(tokenizer=process_text,
                                 stop_words=stopwords.words('english'),
                                 max_df=0.6,
                                 min_df=0,
                                 lowercase=True)

    tfidf_model = vectorizer.fit_transform(texts)
    print(tfidf_model)
    km_model = KMeans(n_clusters=clusters)
    km_model.fit(tfidf_model)
    # print(vectorizer.get_feature_names())

    clustering = collections.defaultdict(list)

    for idx, label in enumerate(km_model.labels_):
        clustering[label].append(idx)

    classes = [0]*len(texts)

    for cls, values in clustering.items():
        # c = None
        for index in values:
            classes[int(index)] = int(cls)
            # if not c:
            #     c = collections.Counter(process_text(texts[index]))
            # else:
            #     c = collections.Counter(process_text(texts[index]))

        # print(sorted([(v, k) for k, v in c.items() if len(k) > 5], reverse=True)[:5])
        # print([_ for _ in sorted(c.items(), key=lambda x: x[1], reverse=True) if len(_[0]) > 5][:5])


    return classes
