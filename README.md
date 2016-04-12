# symmetrical-octo-palm-tree
Our Yelp Dataset Challenge Contestant

Our project currently has a few dependencies that are not included in default python.  They are nltk, sklearn, simplejson, mrjob, and textstat.  Each of these must be installed via pip first.

There is a 100,000 line json file containing data from the Yelp Dataset Reviews, called output.txt, included in the project.  This data was gathered by running the command "python preprocessing.py yelp_reviews.json > output.txt"  yelp_reviews.json is not included in our project as it is 1.9 GB of data.  If you want it, you can find it on the Yelp Dataset Challenge website.

In order to test the project, simply run the command "python naive_bayes_yelp.py" It may take between 10 to 30 minutes to run.  This file contains code to extract features from the reviews and then train and test a naive bayes classifier on the data.  The output is the accuracy of the classifier on the test set.  When we ran this, we received an accuracy of .993. We plan on pickling this classifier and using it in order to classify user input in the final product.
