from flask import Flask, request, render_template
import json
import pickle
import nltk
import string
import re
#from nltk.classify import NaiveBayesClassifier


app = Flask(__name__)

#preprocess the text
def preprocess(sentence):
    nltk.download('stopwords')
    nltk.download('punkt')
    def build_bow_features(words):
        return {word:True for word in words}

    sentence = sentence.lower()
    sentence = sentence.replace('\n','')
    useless = nltk.corpus.stopwords.words("english") + list(string.punctuation)
    wordlist = [word for word in nltk.word_tokenize(sentence) if word not in useless]
    stemmed_words = [nltk.stem.SnowballStemmer('english').stem(word) for word in wordlist]
    Bow = (build_bow_features(stemmed_words))
    print(Bow)
    return Bow

#load the trained model and do prediction
def predict (txt):
	
	prediction = model.classify(txt)
	return prediction

#return the prediction 
def submit_txt(txt):
	txt = preprocess(txt)
	status = predict(txt)
	if status==4 :
		return 'Positive'
	if status==0 :
		return 'Negative'
	return 'FAIL'
	
@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		details = request.form	
		if details['form_type'] == 'submit_txt':
			return submit_txt(details['txt'])
	return render_template('interface.html')

if __name__ == '__main__':
	model = pickle.load(open('SentimentAnalysisModel2.pkl', 'rb'))
	app.run(host='0.0.0.0')
	
	
	
	
	
