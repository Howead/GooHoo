from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def welcome():
	if request.method == 'POST':
		session['username'] = request.form['username']
		return redirect(url_for('search'))
	if 'username' in session:
		return redirect(url_for('search'))
	return render_template('welcome.html')

@app.route("/search")
def search():
	return render_template('search.html')

@app.route("/Profiles")
def Profiles():
	return render_template('Profiles')

@app.route("/Amanage")
def Amanage():
	return render_template('Amanage')

@app.route("/History")
def History():
	return render_template('History')

@app.route("/profile")
def profile():
	if 'username' in session:
		return render_template('profile.html')
	return redirect(url_for('welcome'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('welcome'))

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('welcome'))

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == "__main__":
    app.run()