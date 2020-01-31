from flask import Flask,render_template,url_for,request,redirect
from database import *

app = Flask(__name__)

@app.route('/')
def open():
    return render_template("openpage.html")

@app.route('/sign_up', methods=['GET','POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        add_user(request.form['firstname'],request.form['lastname'],
            request.form['username'],request.form['password'],
            request.form['media'],request.form['song'],
            request.form['member'],request.form['album'],
            request.form['opinion'])
        return redirect(url_for('log_in'))

@app.route('/log_in', methods=["GET","POST"])
def log_in():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        if checkUser(request.form['username'],request.form['password']):
            return redirect(url_for('home'))
        else:
            return render_template('login.html')

@app.route('/home')
def home():
     return render_template('homepage.html')

@app.route('/harrystyles')
def harry():
     return render_template('harry.html')

@app.route('/liampayne')
def liam():
     return render_template('liam.html')

@app.route('/louistomlinson')
def louis():
     return render_template('louis.html')

@app.route('/niallhoran')
def niall():
     return render_template('niall.html')

@app.route('/zaynmalik')
def zayn():
     return render_template('zayn.html')

@app.route('/onedirection')
def oned():
     return render_template('oned.html')

@app.route('/spotifyh')
def spotifyh():
     return render_template('spotifyh.html')

@app.route('/spotifyli')
def spotifyli():
     return render_template('spotifyli.html')

@app.route('/spotifylo')
def spotifylo():
     return render_template('spotifylo.html')

@app.route('/spotifyn')
def spotifyn():
     return render_template('spotifyn.html')

@app.route('/spotifyz')
def spotifyz():
     return render_template('spotifyz.html')

@app.route('/spotifyone')
def spotifyone():
     return render_template('spotifyone.html')

@app.route('/profile' ,methods=["GET","POST"])
def gotoprofile():
    if request.method =="GET":
        return render_template('gotoprofile.html')
    else:
        name = request.form['search']
        return render_template('profile.html',user=query_user(name))

@app.route('/profile/<string:name>')
def profile(name):
    user = query_user(name)
    return render_template('profile.html',user=user)

if __name__ == '__main__':
    app.run(debug=True)