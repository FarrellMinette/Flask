from flask import Flask, session, redirect, url_for, request
app = Flask(__name__)
app.secret_key = 'any random string'

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<b>' + \
            "<b><a href = '/logout'>click here to log out</a></b>"
    return "You are not logged in <b><a href = '/login'></b>" + \
        "click here to log in</b></a>" 

@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
   return '''
   <form action = "" method = "POST">
        <p><h3>Enter username</h3></p>
        <p><input type = 'text' name = 'username'/></p>
        <p><input type = 'submit' value = 'Submit'/></p>
    </form>
   '''

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug = True, port=5000) 