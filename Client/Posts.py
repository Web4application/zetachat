import sqlite3
import time

DB_FILE = "zetachat.db"
conn = sqlite3.connect(DB_FILE, check_same_thread=False)
c = conn.cursor()

def create_post(user, content, image=None):
    c.execute("INSERT INTO posts (user, content, image, likes, time) VALUES (?,?,?,?,?)",
              (user, content, image, 0, time.strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()

def get_posts():
    c.execute("SELECT user, content, image, likes, time FROM posts ORDER BY id DESC")
    rows = c.fetchall()
    posts = []
    for r in rows:
        posts.append({"user": r[0], "content": r[1], "image": r[2], "likes": r[3], "time": r[4], "comments": []})
    return posts
