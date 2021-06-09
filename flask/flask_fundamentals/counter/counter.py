from typing import Counter
from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def home():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return render_template('index.html')

@app.route('/plus_two', methods=['POST'])
def plus_two():
    
    session['counter'] += 1
    return redirect('/')

@app.route('/destroy_session', methods=['POST', 'GET'])
def destroy():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)