from flask import Flask, render_template
import sqlite3


app = Flask(__name__)


def get_db_conn():
    conn = sqlite3.connect('database_db')
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id: int):
    conn = get_db_conn()
    post = conn.execute('SELECT * FROM posts WHERE id=?', (post_id,)).fetchone()
    return post

@app.route('/')
def index():
    conn = get_db_conn()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    return render_template('index.html', posts=posts)


@app.route('/posts/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)


if __name__ == '__main__':
    app.run()
