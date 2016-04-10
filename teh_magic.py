import nltk
import simplejson as json
from sklearn.naive_bayes import MultinomialNB

not_useful = {}
useful = {}

with file('output.txt') as f:
    data = json.loads(f.read())

featuresets = [({'text': data[i]['text']}, str(data[i]['useful'])) for i in range(len(data))]


print featuresets[0]

train_set = featuresets[:50]
test_set = featuresets[50:]

cl = nltk.NaiveBayesClassifier.train(train_set)
print "%.3f" % nltk.classify.accuracy(cl, test_set)
print cl.classify({'text':'Is this useful?'}) # get a confidence for the prediction
