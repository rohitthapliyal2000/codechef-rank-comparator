from flask import Flask, render_template
import driver as dr

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/compare_rank/<h1>/<h2>')
def compare_rank(h1,h2):
    return dr.driver_function(h1,h2)

if __name__ == '__main__':
    app.run(debug=True)
