import sqlite3

class StaffLogs:
    def __init__(self):
        self.conn = sqlite3.connect('stafflogs.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS stafflogs (sender text, action text, target text, date text)''')
        self.conn.commit()
    
    def add_log(self, sender, action, target, date):
        self.c.execute('''INSERT INTO stafflogs VALUES (?, ?, ?, ?)''', (sender, action, target, date))
        self.conn.commit()

stafflogs = StaffLogs()