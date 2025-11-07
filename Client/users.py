import sqlite3
import time

DB_FILE = "zetachat.db"
conn = sqlite3.connect(DB_FILE, check_same_thread=False)
c = conn.cursor()

def login_user(username, password):
    c.execute("SELECT password FROM users WHERE username=?", (username,))
    row = c.fetchone()
    if row and row[0] == password:
        return True
    return False

def signup_user(username, password):
    c.execute("SELECT username FROM users WHERE username=?", (username,))
    if c.fetchone():
        return False
    avatar = f"https://i.pravatar.cc/50?img={hash(username)%70 + 1}"
    c.execute("INSERT INTO users (username,password,avatar,bio) VALUES (?,?,?,?)",
              (username, password, avatar, "New user bio"))
    conn.commit()
    return True

def get_user(username):
    c.execute("SELECT username, avatar, bio FROM users WHERE username=?", (username,))
    row = c.fetchone()
    if not row:
        return {}
    return {"username": row[0], "avatar": row[1], "bio": row[2], "friends": [], "requests": []}

def accept_request(current_user, friend):
    # For simplicity, just a placeholder
    return True
