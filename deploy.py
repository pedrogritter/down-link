from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('base.html')



if __name__ == '__main__':
    app.run(debug=True),  # Do not leave on on real situations