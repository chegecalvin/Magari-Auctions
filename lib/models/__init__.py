import sqlite3

CONN = sqlite3.connect('auction.db')
CURSOR = CONN.cursor()
