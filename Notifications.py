import sqlite3
import time

DB_FILE = "zetachat.db"
conn = sqlite3.connect(DB_FILE, check_same_thread=False)
c = conn.cursor()

def get_notifications(user):
    c.execute("SELECT message FROM notifications WHERE user=? ORDER BY id DESC", (user,))
    rows = c.fetchall()
    return [r[0] for r in rows]

def add_notification(user, message):
    c.execute("INSERT INTO notifications (user, message, time) VALUES (?,?,?)",
              (user, message, time.strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
