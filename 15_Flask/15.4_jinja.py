### building  url dynamically
### Variable Rule
### Junja 2 Template Engine

### Jinja2 template engine 
'''
{{ }} expression is used to evaluate the expression and print the result
{% %} statement is used to execute the conditional statement, for loop, etc.
{# #} comment is used to write comments in the template

'''
from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<html><h1>Welcome to the Flask application!</h1><p>This is a simple web application built with Flask.</p></html>"

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        science = float(request.form['Science'])
        maths = float(request.form['Maths'])
        c = float(request.form['C'])
        datascience = float(request.form['DataScience'])
        avg_score = (science + maths + c + datascience) / 4
        return redirect(url_for('successres',score=avg_score))
    else:
        return render_template('getresult.html')
    

## Variable Rule
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"

    exp={'score': score, 'result': res}

    return render_template('result1.html', results=exp)


@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result1.html', results=score)


@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"

    exp={'score': score, 'result': res}

    return render_template('result1.html', results=exp)

@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result.html', results=score)

if __name__ == '__main__':
    app.run(debug=True)
