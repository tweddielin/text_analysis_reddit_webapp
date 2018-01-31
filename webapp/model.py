from gensim.models import Doc2Vec
import os
import re

MODELDIR = os.getcwd() + "/webapp/static/model/reddit_doc2vec.model"

model = Doc2Vec.load(MODELDIR)

def find_most_similar_topic(post, topn):
    post = re.sub(r'\W+|\d+', ' ', post).lower().split()
    return model.docvecs.most_similar([model.infer_vector(post)], topn=topn)

def find_most_similar(word, topn):
    word = word.lower()
    return model.most_similar(word, topn=topn)

def fine_most_similar_words(words, topn):
	words = re.sub(r'\W+|\d+', ' ', words).lower().split()
	vec = model.infer_vector(words)
	return model.similar_by_vector(vec, topn)
