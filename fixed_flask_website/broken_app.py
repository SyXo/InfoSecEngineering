from flask import Flask, render_template, redirect, request, make_response
import random

app = Flask('SocialGoo')

passwords = {'josh': '1234',
			 'jane': 'pass'}

logged_in = {}

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/login', methods=["GET"])
def login():
	return render_template('login.html')

@app.route('/login-submit', methods=["GET"])
def login_submit():
	global logged_in
	u = request.args.get('username')
	p = request.args.get('password')
	if u in passwords:
		if p == passwords[u]:
			resp = make_response('<a href="/profile/'+u+'">Click to continue to your profile</a>')
			logged_in[u] = str(random.randint(0,10))
			resp.set_cookie('username', u)
			resp.set_cookie('rand', logged_in[u])
			return resp
		else:
			return "Wrong password for " + u
	else:
		return "Username not found"

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


