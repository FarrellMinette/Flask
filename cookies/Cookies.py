from flask import Flask, render_template, request, make_response
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/setcookie', methods = ['POST'])
def setcookie():
   user = request.form['nm']
   resp = make_response(render_template('readcookie.html'))
   resp.set_cookie('username', user)
   return resp

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('username')
   return '<h1>Username: '+name+'</h1>'

if __name__ == '__main__':
    app.run(debug = True, port=4000) 