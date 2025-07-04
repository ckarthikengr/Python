import flask as Flask

'''
It creates an instance of the Flask class, which is the WSGI application.
'''

## WSGI applicatio
app = Flask.Flask(__name__)

@app.route('/')
def welcome():
    return "<html><h1>Welcome to the Flask application!</h1><p>This is a simple web application built with Flask.</p></html>"

@app.route('/index')
def index():
    return "Welcome to the Index page!"

if __name__ == '__main__':
    '''
    It runs the Flask application.
    '''
    app.run(debug=True) 
    ##s// debug=True enables the debug mode, which will reload the server automatically when you make changes to the code.
    # app.run(host='0.0.0.0', port=5000)
    # debug is optional, but it is useful during development.