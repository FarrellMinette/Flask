from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

# Application
## Create app - home page
@app.route('/')
def hello_world():
   return 'Home page'

# Routing, URL building
## Create a function and add it to new route
@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s' %guest

@app.route('/user/<name>')
def hello_user(name):
    if name=='admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


# Variables
## Takes part of url as input to variable which is then passed back
### Strings
@app.route('/<name>')
def return_name(name):
    return 'Hello from %s' %name

### Integers
@app.route('/ID/<int:id>')
def return_id(id):
    return 'ID number %d' %id

### Floats
@app.route('/amount/<float:amount>')
def return_amount(amount):
    return 'Amount in account: %f' %amount

@app.route('/success/<name>')
def login_success(name):
   return 'Welcome %s' %name

@app.route('/login', methods = ['POST','GET'])
def login():
    if request.method=='POST':
        user = request.form['nm']
        return redirect(url_for('login_success',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('login_success',name = user))

# Web Templating
@app.route('/hello/<user>/<int:marks>')
def hello_name(user, marks):
   return render_template('hello.html', name = user, mark = marks)

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('results.html', result = dict)

# JavaScript
@app.route("/javascript")
def index():
   return render_template("index.html")



## Run app: 
### Debug enabled:reloads with changes
### Port set to 3000
if __name__ == '__main__':
    app.run(debug = True, port=3000) 