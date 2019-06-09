import os

try:
    os.unlink('bank.db')
except:
    print('首次建檔')

import sqlite3
conn = sqlite3.connect('bank.db')
cur = conn.cursor()

def show_all_rows(all_rows):
    for row in all_rows:
        print(row)
    print()

# 匯率表
cur.execute('''CREATE TABLE CURRENCY_RATE(CURRENCY text,BUY_IN real,SOLD_OUT real)''')
cur.execute("INSERT INTO CURRENCY_RATE VALUES ('USD', 30.455, 31.094)")
cur.execute("INSERT INTO CURRENCY_RATE VALUES ('HKD',  3.761,  3.977)")
cur.execute("INSERT INTO CURRENCY_RATE VALUES ('EUR', 34.150, 35.490)")
cur.execute("INSERT INTO CURRENCY_RATE VALUES ('JPY',  0.269,  0.082)")
cur.execute("INSERT INTO CURRENCY_RATE VALUES ('CNY',  4.501,  4.633)")
conn.commit()

cur.execute("SELECT * FROM CURRENCY_RATE")
show_all_rows(cur.fetchall())

# 匯率設定
cur.execute("CREATE TABLE CURRENCY_RATE_SETTINGS(CURRENCY text,RANGE1 real,RANGE2 real,CHANGE_LIMIT real)")
cur.execute("INSERT INTO CURRENCY_RATE_SETTINGS VALUES ('USD', 29.100, 32.000, 0.1)")
cur.execute("INSERT INTO CURRENCY_RATE_SETTINGS VALUES ('HKD',  2.001,  4.001, 0.02)")
cur.execute("INSERT INTO CURRENCY_RATE_SETTINGS VALUES ('EUR', 34.100, 37.150, 0.3)")
cur.execute("INSERT INTO CURRENCY_RATE_SETTINGS VALUES ('JPY',  0.251,  0.321, 0.01)")
cur.execute("INSERT INTO CURRENCY_RATE_SETTINGS VALUES ('CNY',  4.321,  5.032, 0.03)")
conn.commit()

cur.execute("SELECT * FROM CURRENCY_RATE_SETTINGS")
show_all_rows(cur.fetchall())

# 顧客資料
cur.execute('''CREATE TABLE CUSTOMER (ID integer, ACCOUNT text, NAME text)''')
cur.execute("INSERT INTO CUSTOMER VALUES (1, 'camille', 'Camille')")
cur.execute("INSERT INTO CUSTOMER VALUES (2, 'chris', 'Chris Pine')")
cur.execute("INSERT INTO CUSTOMER VALUES (3, 'gal', 'Gal Gadot')")
cur.execute("INSERT INTO CUSTOMER VALUES (4, 'bill', 'Bill Gates')")
cur.execute("INSERT INTO CUSTOMER VALUES (5, 'steve', 'Steve Jobs')")
cur.execute("INSERT INTO CUSTOMER VALUES (6, 'tom', 'Tom Cruise')")
cur.execute("INSERT INTO CUSTOMER VALUES (7, 'anne', 'Anne Hathaway')")
cur.execute("INSERT INTO CUSTOMER VALUES (8, 'trump', 'Donald Trump')")
cur.execute("INSERT INTO CUSTOMER VALUES (9, 'mark', 'Mark Zuckerberg')")
conn.commit()

cur.execute("SELECT * FROM CUSTOMER")
show_all_rows(cur.fetchall())

# 交易紀錄
cur.execute('''CREATE TABLE RECORD (ID integer, ACCOUNT text, CURRENCY text, BUY_IN integer, SOLD_OUT integer, BALANCE integer, DATE_TIME text)''')
cur.execute("INSERT INTO RECORD VALUES (1, 'chris', 'USD', 10000, 0, 10000, '2017-10-01 00:01:02')")
cur.execute("INSERT INTO RECORD VALUES (2, 'gal', 'JPY', 50000, 0, 50000, '2017-10-01 10:19:55')")
cur.execute("INSERT INTO RECORD VALUES (3, 'camille', 'HKD', 30000, 0, 30000, '2019-05-01 09:31:43')")
cur.execute("INSERT INTO RECORD VALUES (4, 'bill', 'EUR', 70000, 0, 70000, '2019-05-01 15:36:27')")
cur.execute("INSERT INTO RECORD VALUES (5, 'steve', 'USD', 25000, 0, 25000, '2019-05-01 11:05:22')")
conn.commit()

cur.execute("SELECT * FROM RECORD")
show_all_rows(cur.fetchall())


conn.close()
