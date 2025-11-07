import sqlite3
import time

DB_FILE = "zetachat.db"
conn = sqlite3.connect(DB_FILE, check_same_thread=False)
c = conn.cursor()

def send_message(sender, receiver, message):
    c.execute("INSERT INTO messages (sender, receiver, message, time) VALUES (?,?,?,?)",
              (sender, receiver, message, time.strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()

def get_messages(user1, user2):
    c.execute("""
        SELECT sender, message, time FROM messages
        WHERE (sender=? AND receiver=?) OR (sender=? AND receiver=?)
        ORDER BY id ASC
    """, (user1, user2, user2, user1))
    rows = c.fetchall()
    return [{"sender": r[0], "message": r[1], "time": r[2]} for r in rows]
