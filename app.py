from flask import flash, Flask, render_template, request, url_for, redirect
import sqlite3


app = Flask(__name__)
app.config['SECRET_KEY'] = 'test12345'


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


@app.route('/posts/new', methods=['POST', 'GET'])
def new():
    if request.method == 'GET':
        return render_template('new.html')
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title or not content:
            flash('Please fill in all fields')
        else:
            conn = get_db_conn()
            conn.execute('INSERT INTO posts (title, content) VALUES (?,?)', (title, content))
            conn.commit()
            flash('文章发布成功')
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
