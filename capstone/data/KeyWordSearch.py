from gensim.models import Word2Vec
import itertools


def keyword_search(keyword):
    model = Word2Vec.load('keywordSearchModel.model')
    result_array = model.wv.most_similar(keyword)
    result_array = list(itertools.chain.from_iterable(result_array))
    del result_array[1:20:2]
    del result_array[4:10]
    return result_array
