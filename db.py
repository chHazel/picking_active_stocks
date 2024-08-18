import psycopg2
import datetime

def connection():
    conn = psycopg2.connect(
    database = "active_stocks", 
    user= "apple", 
    password= "123456",
    host= "localhost",
    port= "5432")
    return conn

def create_table():
    conn = connection()

    cur = conn.cursor()
    cur.execute("DROP TABLE active_stocks;")
    cur.execute(""" 
                CREATE TABLE IF NOT EXISTS active_stocks(
                symbol VARCHAR(10), 
                change FLOAT, 
                REL_VOLUMN FLOAT, 
                pe_ratio FLOAT, 
                date DATE NOT NULL,
                UNIQUE(symbol, date)
                );""")

    conn.commit()
    cur.close()
    conn.close()

def insert_data(symbol, change, rel_volumn, pe_ratio):
    conn = connection()

    cur = conn.cursor()

    cur.execute(""" 
        INSERT INTO active_stocks (symbol, change, rel_volumn, pe_ratio, date)
        VALUES (%s, %s, %s, %s, CURRENT_DATE)
        ON CONFLICT(symbol, date)
        DO NOTHING;""", (symbol, change, rel_volumn, pe_ratio))
    conn.commit()
    cur.close()
    conn.close()

def fetch_today_data():
    conn = connection()

    cur = conn.cursor()
    cur.execute("""SELECT * FROM active_stocks
                WHERE date = CURRENT_DATE""")
    rows = cur.fetchall()
    
    return rows

def fetch_five_days():
    conn = connection()
    cur = conn.cursor()
    cur.execute("""SELECT symbol, COUNT(*) AS count
                FROM active_stocks
                WHERE date >= CURRENT_DATE - INTERVAL '5 days'
                GROUP BY symbol
                ORDER BY count DESC
                limit 20;
                """)
    rows = cur.fetchall()
    return rows

def fetch_ten_days():
    conn = connection()
    cur = conn.cursor()
    cur.execute("""SELECT symbol, COUNT(*) AS count
                FROM active_stocks
                WHERE date >= CURRENT_DATE - INTERVAL '10 days'
                GROUP BY symbol
                ORDER BY count DESC
                limit 20;
                """)
    rows = cur.fetchall()
    return rows

def fetch_twenty_days():
    conn = connection()
    cur = conn.cursor()
    cur.execute("""SELECT symbol, COUNT(*) AS count
                FROM active_stocks
                WHERE date >= CURRENT_DATE - INTERVAL '20 days'
                GROUP BY symbol
                ORDER BY count DESC
                limit 20;
                """)
    rows = cur.fetchall()
    return rows