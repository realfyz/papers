import sqlite3
import os


'''
Database name: Papers
Database file: ./db/Papers
Tables' name: user, paper
Fields (* is primary key):
    user
        | *id | username | password |
    paper
        | *id | userid | filename | time | desc | cite | path |
'''


basedir = os.path.abspath(os.path.dirname(__file__)) + '/db'


def init_db():
    conn = sqlite3.connect(basedir+'/Papers')
    conn.close()


# ---------- paper table operations ----------
def show_papers(userid):
    ret = []
    conn = sqlite3.connect(basedir+'/Papers')
    c = conn.cursor()
    for row in c.execute("SELECT * FROM paper WHERE userid = ?", [userid]):
        ret.append(row)
    return ret


def add_paper(userid, filename, time, desc, cite, path):
    conn = sqlite3.connect(basedir+'/Papers')
    c = conn.cursor()
    info = (userid, filename, time, desc, cite, path)
    c.execute('INSERT INTO paper (userid, filename, time, desc, cite, path) VALUES (?,?,?,?,?,?)', info)
    conn.commit()
    conn.close()


def delete_paper(paperid):
    conn = sqlite3.connect(basedir + '/Papers')
    c = conn.cursor()
    c.execute('DELETE FROM paper WHERE id = ?', [paperid])
    conn.commit()
    conn.close()


def select_paper(paperid):
    ret = []
    conn = sqlite3.connect(basedir + '/Papers')
    c = conn.cursor()
    for row in c.execute('SELECT * FROM paper WHERE id = ?', [paperid]):
        ret.append(row)
    return ret


# ---------- user table operations ----------
def add_user(username, password):
    conn = sqlite3.connect(basedir + '/Papers')
    c = conn.cursor()
    data = (username, password)
    c.execute('INSERT INTO user (username, password) VALUES (?,?)', data)
    conn.commit()
    conn.close()


def select_user(username):
    ret = []
    conn = sqlite3.connect(basedir + '/Papers')
    c = conn.cursor()
    for row in c.execute('SELECT * FROM user WHERE username = ?', [username]):
        ret.append(row)
    return ret
