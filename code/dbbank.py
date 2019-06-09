class DB:
    def __init__(self):
        self.conn = None
        self.cur = None
        self.title_side = '-'*12

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
        return False

    def open(self):
        """ 開啟資料庫連線
        """
        if self.conn is None:
            import sqlite3
            self.conn = sqlite3.connect('bank.db')
            self.cur = self.conn.cursor()
        return True

    def close(self):
        """ 關閉資料庫連線
        """
        if self.conn is not None:
            self.conn.close()
            self.conn = None
        return True

    def get_max_id(self, arg_table):
        """ 取得資料最新編號
        """
        self.cur.execute("SELECT MAX(ID) FROM {}".format(arg_table))
        return self.cur.fetchone()[0] + 1

    def list_all_currency(self):
        """ 匯率表
        """
        import random
        self.cur.execute("SELECT * FROM CURRENCY_RATE")
        all_rows = self.cur.fetchall()
        for row in all_rows:
            currency = row[0]
            # SELECT
            self.cur.execute("SELECT * FROM CURRENCY_RATE_SETTINGS WHERE CURRENCY=?",(currency,))
            currency_set = self.cur.fetchone()
            set_limit = currency_set[3]
            # range1
            set_range1 = currency_set[1]
            range1 = row[1]
            range1_top = range1 + set_limit
            range1_bottom = range1 - set_limit
            if range1_top > set_range1:
                range1_top = set_range1
            changed_range1=round(random.uniform(range1_bottom, range1_top),3)
            # range2
            set_range2 = currency_set[2]
            range2 = row[2]
            range2_top = range2 + set_limit
            range2_bottom = range2 - set_limit
            if range2_top > set_range2:
                range2_top = set_range2
            changed_range2=round(random.uniform(range2_bottom, range2_top),3)
            # UPDATE
            self.cur.execute("UPDATE CURRENCY_RATE SET BUY_IN=?, SOLD_OUT=? WHERE CURRENCY=?",(changed_range1,changed_range2, currency))


        self.cur.execute("SELECT * FROM CURRENCY_RATE")
        all_rows = self.cur.fetchall()
        for row in all_rows:
            print(row)
        return all_rows

    def list_currency_settings(self):
        """ 匯率設定表
        """
        self.cur.execute("SELECT * FROM CURRENCY_RATE_SETTINGS")
        all_rows = self.cur.fetchall()
        for row in all_rows:
            print(row)
        return all_rows

    def insert_or_update_currency_rate(self, currency, set_range1, set_range2, change_limit):
        """ 增修匯率
        """
        self.cur.execute("SELECT COUNT(*) FROM CURRENCY_RATE_SETTINGS WHERE CURRENCY=?", (currency,))
        count_result = self.cur.fetchone()[0]
        if count_result == 0:
            self.cur.execute("INSERT INTO CURRENCY_RATE_SETTINGS (?, ?, ?, ?)", 
                (currency, set_range1, set_range2, change_limit))
        elif count_result > 0:
            self.cur.execute("UPDATE CURRENCY_RATE_SETTINGS SET RANGE1=?, RANGE2=?, CHANGE_LIMIT=? WHERE CURRENCY=?", (set_range1, set_range2, change_limit, currency))
        return self.conn.commit()

    def list_all_customer(self):
        """ 顧客資料
        """
        self.cur.execute("SELECT * FROM CUSTOMER")
        all_rows = self.cur.fetchall()
        for row in all_rows:
            print(row)
        print()

    def check_if_customer_enrolled(self, arg_account):
        """ 檢查是否註冊
        """
        self.cur.execute("SELECT COUNT(*) FROM CUSTOMER WHERE ACCOUNT=?", (arg_account,))
        if self.cur.fetchone()[0] == 1:
            return True
        else:
            return False

    def insert_or_update_customer(self, account_id, action):
        """ 增修顧客
        """
        data_ok = True
        full_name = input('全名: ')
        if full_name == 'q':
            return False
        else:
            data_ok = False

        # 資料無誤，准許註冊            
        if data_ok:
            if action == 'insert':
                customer_max_id = self.get_max_id('CUSTOMER')
                self.cur.execute("INSERT INTO CUSTOMER VALUES (?, ?, ?)", 
                    (customer_max_id, account_id, full_name))
            elif action == 'update':
                self.cur.execute("UPDATE CUSTOMER SET NAME=? WHERE ACCOUNT=?", 
                    (full_name, account_id))
            self.conn.commit()
            return True
        else:
            return False

    def get_other_customer(self):
        """ 查詢其他顧客資訊
        """
        self.cur.execute("SELECT ACCOUNT FROM CUSTOMER WHERE ID>1")
        other_customer_info = self.cur.fetchall()
        return other_customer_info
                        
    def get_customer_info(self, account):
        """ 查詢顧客資訊
        """
        self.cur.execute("SELECT * FROM CUSTOMER WHERE ACCOUNT=?", (account,))
        customer_info = self.cur.fetchone()
        return customer_info

    def insert_record(self, account, currency, buy_in, sold_out, balance, date):
        """ 增修紀錄
        """
        record_max_id = self.get_max_id('RECORD')
        self.cur.execute("INSERT INTO RECORD VALUES (?, ?, ?, ?, ?, ?, ?)", 
            (record_max_id, account, currency, buy_in, sold_out, balance, self.get_date()))
        return self.conn.commit()

    def random_records(self, account, currency, buy_in, sold_out, balance, date):
        record_max_id = self.get_max_id('RECORD')
        self.cur.execute("INSERT INTO RECORD VALUES (?, ?, ?, ?, ?, ?, ?)",(record_max_id, account, currency, buy_in, sold_out, balance, self.get_date()))
        return self.conn.commit()

    def list_record_by_account(self, account):
        """ 個人交易紀錄查詢
        """
        account_like = ''.join(('%', account, '%'))
        self.cur.execute("SELECT * FROM RECORD WHERE ACCOUNT LIKE ?", (account_like,))
        all_rows = self.cur.fetchall()
        if len(all_rows) > 0:
            for row in all_rows:
                print(row)
        else:
            print(account, '查無紀錄')

    def get_date(self):
        from datetime import datetime
        date_time=datetime.now()
        return date_time.strftime("%Y-%m-%d %H:%M:%S")

    def get_latest_balance(self, account, currency):
        self.cur.execute("SELECT BALANCE FROM RECORD WHERE ACCOUNT=? AND CURRENCY=? AND DATE_TIME < ? ORDER BY DATE_TIME DESC LIMIT 1 OFFSET 0",
            (account,currency[0],self.get_date()))
        balance=self.cur.fetchone()
        if balance is not None:
            return balance[0]
        else:
            return 0

    def all_records(self):
        self.cur.execute("SELECT * FROM RECORD")
        all_rows = self.cur.fetchall()
        for row in all_rows:
            print(row)
        return all_rows

    def records_date(self, date):
        self.cur.execute("SELECT * FROM RECORD WHERE DATE_TIME>=?",(date,))
        records=self.cur.fetchall()
        return records