from flask import Flask, request, render_template
import json

app = Flask(__name__)

def submit_txt(txt):
	status = "success"
	return status
	
@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		details = request.form	
		if details['form_type'] == 'submit_txt':
			return submit_txt(details['txt'])
	return render_template('interface.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0')
	
	
	
	
	
