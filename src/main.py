import os
from datetime import timedelta

import sqlite
import time

import timeutils # self package
import sessions # self package
import mdfactory # self package
import path # self package

from flask import Flask, render_template, request, redirect, url_for, session

from werkzeug.utils import secure_filename

from flaskext.markdown import Markdown

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = os.urandom(24)
#app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)

Markdown(app)

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

basedir = os.path.abspath(os.path.dirname(__file__))
basedir = basedir + '/static/refs/'
moviedir = os.path.abspath(os.path.dirname(__file__)) + '/static/movies/'


@app.route('/')
def main():
    if 'username' in session.keys() and 'uid' in session.keys():
        return redirect(url_for('show_papers', username=session['username']))
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        users = sqlite.select_user(username)
        if len(users) == 0:
            return "Error! Cannot find this username!"
        else:
            if password == users[0][2]:
                session['uid'] = users[0][0]
                session['username'] = username
                return redirect(url_for('show_papers', username=username))
            else:
                return "Password error!"
    return "Error!"


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        users = sqlite.select_user(username)
        if len(users) != 0:
            return "Error! This username has been registered!"
        else:
            sqlite.add_user(username, password)
            return redirect(url_for('login'))
    return "Error!"


@app.route('/about', methods=['GET'])
def about():
    text = mdfactory.md2text('about')
    return render_template("about.html", text=text)


@app.route('/movies', methods=['GET'])
@app.route('/movies/', methods=['GET'])
def movie():
    movies = os.listdir(moviedir)
    return render_template("movie.html", movies=movies)


@app.route('/movies/<moviename>', methods=['GET'])
def watch_movie(moviename):
    moviepath = '/static/movies/' + moviename
    return render_template("watch_movie.html", name=moviename, path=moviepath)


@app.route('/delete', methods=['GET', 'POST'])
def delete_paper():
    if request.method == 'POST':
        fileid = request.form.get('fileid')
        if fileid is not None:
            paper = sqlite.select_paper(fileid)
            filename = paper[0][2]
            if os.path.exists(basedir+filename):
                os.remove(basedir+filename)
            sqlite.delete_paper(fileid)
        return redirect(url_for('show_papers', username=session['username']))


@app.route('/read/<paperid>', methods=['GET'])
def read_paper(paperid):
    paper_info = sqlite.select_paper(paperid)
    return render_template("read.html", paper=paper_info)


@app.route('/<username>/new', methods=['GET', 'POST'])
def add_paper(username):
    if request.method == 'GET':
        if username != session['username']:
            return redirect(url_for('login'))
        if username == session['username']:
            return render_template("add_paper.html", username=username)
    if request.method == 'POST':
        file = request.files.get('file')
        name = secure_filename(file.filename)
        file.save(basedir + name)
        desc = request.form.get('desc')
        cite = request.form.get('cite')
        sqlite.add_paper(session['uid'], name, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())), desc, cite, '')
        return redirect(url_for('show_papers', username=session['username']))


@app.route('/<username>')
@app.route('/<username>/')
def show_papers(username):
    if 'username' not in session.keys() or 'uid' not in session.keys() or username != session['username']:
        return redirect(url_for('login'))
    if username == session['username']:
        papers = sqlite.show_papers(session['uid'])
        temp = []
        for i in range(0, len(papers)):
            temp.append(list(papers[i]))
            temp[i][3] = timeutils.perform(temp[i][3])
            temp[i][2] = temp[i][2].split('.')[0]
        temp.reverse()
        return render_template("papers.html", papers=temp, username=username)




if __name__ == "__main__":
    app.run(debug=False, port=80, host='0.0.0.0')
