from gensim.models import Word2Vec
sentence = input()
model = Word2Vec(sentences, min_count=1, size=100)
vocab = model.vocab.keys()
wordsInVocab = len(vocab)
print (model.similarity('post', 'book'))
 
 
import numpy as np
 
def sent_vectorizer(sent, model):
    sent_vec = np.zeros(100)
    numw = 0
    for w in sent:
        try:
            sent_vec = np.add(sent_vec, model[w])
            numw+=1
        except:
            pass
    return sent_vec / np.sqrt(sent_vec.dot(sent_vec))
 
V=[]
for sentence in sentences:
    V.append(sent_vectorizer(sentence, model))
 
from numpy import dot
from numpy.linalg import norm
results = [[0 for i in range(len(V))] for j in range(len(V))] 
 
for i in range (len(V) - 1):
    for j in range(i+1, len(V)):
           results[i][j] = dot(V[i],V[j])/norm(V[i])/norm(V[j])
 
 
print (results)
