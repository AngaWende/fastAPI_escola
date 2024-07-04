import os, sqlite3

def get_db():
    db_path = os.path.join(os.path.dirname(__file__),'..','shared', 'escola.db')
    conn = sqlite3.connect(db_path)
    try:
        yield conn
    finally:
        conn.close()