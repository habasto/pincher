import sqlite3
from datetime import datetime

DB_FILE = "pincher_data.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS process_stats (
            ts TEXT,
            pid INTEGER,
            user TEXT,
            usr REAL,
            system REAL,
            cpu REAL,
            vsz INTEGER,
            rss INTEGER,
            mem REAL,
            command TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_stat(stat):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        INSERT INTO process_stats 
        (ts, pid, user, usr, system, cpu, vsz, rss, mem, command)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        datetime.now().isoformat(),
        stat["pid"],
        stat["user"],
        stat["usr"],
        stat["system"],
        stat["cpu"],
        stat["vsz"],
        stat["rss"],
        stat["mem"],
        stat["command"]
    ))
    conn.commit()
    conn.close()
