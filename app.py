import pyrebase

config = {
    "apiKey": "AIzaSyCr16ZqUe9Kjq4i3fAQW4-Eaia8YrLPMe8",
    "authDomain": "test36-19e13.firebaseapp.com",
    "databaseURL": "https://test36-19e13.firebaseio.com",
    "projectId": "test36-19e13",
    "storageBucket": "test36-19e13.appspot.com",
    "messagingSenderId": "256948904233",
    "appId": "1:256948904233:web:6cb13d36b62c1cb1679738",
    "measurementId": "G-K1TKKWQ5QJ"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

# db.child("names").push({"names":"Bhumi"})
# db.child("names").update({"names":"Bhumika"})
# db.child("names").child("name").update({"name":"Bhumika"})

# users = db.child("names").child("name").get()
# print(users.key())
# db.child("names").child("names").remove()
# db.child("names").remove()

from flask import Flask, render_template, request, session, url_for, redirect

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        db.child("todo").push(email)
        todo = db.child("todo").get()
        to = todo.val()
        return render_template('index.html',t=to.values())
    return render_template('index.html')

@app.route('/navigate1')
def navigate1():
    return render_template('navigate1.html')

if (__name__ == '__main__'):
    app.run(debug=True)