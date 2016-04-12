import nltk
import simplejson as json
from sklearn.naive_bayes import MultinomialNB
from textstat.textstat import textstat
import pickle

# use textstat to pull out useful features from the text
def get_features(text):
    output = {}
    output['text'] = text
    output['syllables'] = textstat.syllable_count(text)
    output['lexicons'] = textstat.lexicon_count(text)
    output['sentences'] = textstat.sentence_count(text)
    output['smog'] = textstat.smog_index(text)
    return output

# pickles the classifier for future use, this will improve speeds when classfying user input
def save_classifier(classifier):
    with file('my_classifier.pickle', 'wb') as f:
        pickle.dump(classifier, f, -1)

# unpickles the classifier
def load_classifier():
    with file('my_classifier.pickle', 'rb') as f:
        return pickle.load(f)

with file('output.txt') as f:
    data = json.loads(f.read())

# extract the features from each line of data
featuresets = [(get_features(data[i]['text']), str(data[i]['useful'])) for i in range(len(data))]

n = len(featuresets) / 2
train_set = featuresets[:n]
test_set = featuresets[n:]

# train the classifier on the first half and test on the second half
cl = nltk.NaiveBayesClassifier.train(train_set)
print "%.3f" % nltk.classify.accuracy(cl, test_set)
