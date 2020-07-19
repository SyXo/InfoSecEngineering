#Issues fixed:
  # 1. Password complexity
  # 2. Password form visibility
  # 3. User list extraction
  # 4. Cookie login confirmation
  # 5. Cookie identifiation numbers
  # 6. Cookie expiration
  # 7. HTTP method for login-submit
  # 8. Logout feature absent

from flask import Flask, render_template, redirect, request, make_response
import random

app = Flask('SocialGoo')

passwords = {'josh': 'ubuVVSVWDMR@8!FJ',
			 'jane': '2J~=33eKFA>hByxb'}

logged_in = {}

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/login', methods=["GET"])
def login():
	return render_template('login.html')

@app.route('/login-submit', methods=["POST"])
def login_submit():
	global logged_in
	u = request.form['username']
	p = request.form['password']
	if u in passwords:
		if p == passwords[u]:
			resp = make_response('<a href="/profile/'+u+'">Click to continue to your profile</a> <br> <a href=/logout>Logout</a></br>')
			logged_in[u] = str(random.randint(0, 999999))
			resp.set_cookie('username', u, max_age = 100000)
			resp.set_cookie('rand', logged_in[u], max_age = 100000)
			return resp
		else:
			return "Error: Incorrect username / password"
	else:
		return "Error: Incorrect username / password"

@app.route('/profile/<username>')
def profile(username):
	login_username = request.cookies.get('username')
	login_rand = request.cookies.get('rand')
	if login_username is None and login_rand is not None and logged_in[login_username] == login_rand:
		return redirect('/login')
	elif login_username == username:
		return "Here is your private profile, " + username + "!"
	else:
		return "Here is the public profile of " + username + "!"

@app.route('/logout')
def logout():
    resp = make_response('You have been logged out <br> <a href=/>Home</a></br>')
    resp.set_cookie('username', max_age = 0)
    resp.set_cookie('rand', max_age = 0)
    return resp


