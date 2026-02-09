import os
import sqlite3
import hashlib
import time


class Memory:
    """Manages the Collective Memory - Traumas and Instincts."""

    def __init__(self, db_path="data/database/memory.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        parent = os.path.dirname(self.db_path)
        if parent:
            os.makedirs(parent, exist_ok=True)
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        c = self.conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS traumas
                     (signature TEXT PRIMARY KEY, context TEXT, error_msg TEXT, attempts INTEGER, timestamp REAL)""")
        c.execute("""CREATE TABLE IF NOT EXISTS instincts
                     (id INTEGER PRIMARY KEY, type TEXT, blueprint TEXT, successes INTEGER DEFAULT 1)""")
        self.conn.commit()

    def sign(self, content):
        return hashlib.sha256(str(content).encode()).hexdigest()

    def check(self, sig):
        c = self.conn.cursor()
        c.execute("SELECT error_msg, attempts FROM traumas WHERE signature=?", (sig,))
        res = c.fetchone()
        if res:
            return False, f"Trauma detected: {res[0]} ({res[1]}x)"
        return True, "Safe"

    def record_failure(self, sig, ctx, err):
        c = self.conn.cursor()
        c.execute(
            """INSERT INTO traumas (signature, context, error_msg, attempts, timestamp)
                     VALUES (?, ?, ?, 1, ?)
                     ON CONFLICT(signature) DO UPDATE SET
                     attempts = attempts + 1, timestamp = ?""",
            (sig, ctx, str(err), time.time(), time.time()),
        )
        self.conn.commit()
