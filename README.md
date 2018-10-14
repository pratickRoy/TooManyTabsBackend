# too-many-tabs (Chrome Extension)

## What is this?

**too-many-tabs** (or **TooManyTabs** if you so prefer) is a Chrome extension that solves the very common
problem of having too many tabs open in browsers that most knowledge workers (including developers face.)

Behold:

![](toomanytabs.png) 

With this many tabs open, when I get to work, I feel less like a Software Developer, and more like an archeologist, sifting through
layers of tabs and trying to guess what I'll need and what I won't.

With **TMT**, no more.

- **too-many-tabs**'s Smart Shuffle feature regroups tabs by context and content. So when you're at work, you can hide those Reddit tabs, and really *really* focus on your work.
- Blazing fast full text search with lemmatization ensures you won't open a tenth copy of the `scikit-learn` documentation. Did the tab mention `classification`,
`classifying` or `classified`? You don't need to care, because **TMT**'s lemmatization handles that.
- Stop clicking to bookmark or close tabs. Do it in bulk with **TMT**'s convenient UI. 
- Designed for privacy - the model used for **TMT** fits entirely on your local machine and works efficiently on it too. 
No need to sell your data to marketers :)

**TMT** was built as a hack by [aviraldg](https://github.com/aviraldg) and [pratickRoy](https://github.com/pratickRoy) at [InOut 5.0](https://hackinout.co).

## Usage Instructions

```
# In the extension repo:
yarn install
yarn run dev
# Head over to Chrome, open the Extensions page and click on "Load Unpacked Extension"
# Then, select the dev folder. Restart your browser qfor it to take affect.
# Make sure you're also running the server, which you can do by:
python app.py
```

(install dependencies as appropriate)

## Models Used

- `kmeansclustering` and `commons` contains our initial attempts and building and training the model. We had to discard that version because it was too slow and did not give ideal reesults.
This model was built using K-Means Clustering and average of Word2vec vectors for text feature embedding.
- `model.py` contains another (unsuccessful) attempt with Spectral Clustering and Word2vec vectors for text feature embedding.
- `final_model.py` contains the finally used model, which uses K-Means clustering and tf-idf for document representation. This seemed to give acceptable results.

Sample model input data was previously part of the repo but was scrubbed to remove personal information.