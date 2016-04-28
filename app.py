from flask import Flask, render_template, request
import naive_bayes_yelp as nb

app = Flask(__name__)
cl = nb.load_classifier()

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print request.form
        features = nb.get_features(request.form['review'])
        print features
        useful = cl.classify(features)
        print useful
        return render_template('app.html', useful=useful, review=request.form['review'])
    else:
        return render_template('app.html', useful=None, review='')



if __name__ == "__main__":
    app.run()
