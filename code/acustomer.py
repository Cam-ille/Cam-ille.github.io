# aguest.py
from dbbank import DB

class Customer:
    def __init__(self):
        self.menu_title = '投資人'
        self.account = ''
        self.menu = {
            'a':'登入．註冊',
            'b':'買進/賣出',
            'c':'個人交易紀錄',
            'q':'離開',
        }
        self.menu_func = {
            'a': lambda c, s: self.login_or_enroll(c, s),
            'b': lambda c, s: self.currency_buy_sell(c, s),
            'c': lambda c, s: self.currency_transaction_record(c, s)
        }
        self.divider = '='*20

    def show_menu(self, account=''):
        """ 主選單
        """
        print(self.divider)
        if self.account == '':
            print(self.menu_title, '尚未登入')
        else:
            print(self.menu_title, self.account)
        print(self.divider)
        for fid, fname in self.menu.items():
            print('%s:%s' % (fid, fname))
        print(self.divider)
        opt = input('請選擇: ').lower()
        if opt in self.menu.keys():
            return opt, self.menu[opt]
        else:
            return '', '無此功能！'

    def login_or_enroll(self, db, func_title):
        """ 登入．註冊
        """
        account_input = input('請輸入帳號: ')
        if db.check_if_customer_enrolled(account_input):
            self.account = account_input
            print(db.get_customer_info(self.account))
        else:
            if db.insert_or_update_customer(account_input, 'insert'):
                print('註冊成功')

    def currency_buy_sell(self, db, func_title):
        """ 買進賣出
        """
        import random
        while True:
            print('幣別  ',' 買入 ',' 賣出')
            currency=db.list_all_currency()
            opt=input('Which currency? (1.美元 2.港幣 3.歐元 4.日圓 5.人民幣 exit.離開):')
            if opt == 'exit':
                break
            else:
                currency_code = currency[int(opt)-1]
                buy=currency_code[2]
                sold=currency_code[1]
                buy_in=0
                sold_out=0
                choose=input('1.BUY IN  2.SOLD OUT:')
                balance = db.get_latest_balance(self.account, currency_code)
                print('BALANCE:',balance)
                if choose=='1':
                    money=int(input('How much(use NTD)?'))
                    buy_in= money//buy
                    balance=balance+buy_in
                    print('BUY:',buy_in)
                elif choose=='2':
                    money=int(input('How much?'))
                    sold_out= money
                    balance=balance-sold_out
                    if balance<0:
                        print('餘額不足')
                        break
                    else:
                        print('SOLD:',sold_out)
                db.insert_record(self.account, currency[int(opt)-1][0], buy_in, sold_out, balance, db.get_date())
                # 1. 從其他顧客中任選一些，範圍從1~n-1
                # 1.1 選的方式，先將所有顧客帳號查詢出來，放在一個 tuple or list
                # 1.2 承上，再做隨機取樣，sample(other_customers, randint(1, n-1))
                # 2. 假設9個裡面取出5個
                # 2.1 這5個，逐一讀取每個 account，然後幫他亂數決定要買或要賣
                # 2.2 先做到一次買賣一種貨幣
                # 2.3 買的部分範圍自訂，賣的部分範圍最高要限定目前該貨幣的餘額
                # 2.4 可以考慮，亂數範圍，以10或50或100取整
                # 2.5 如果完成，再回頭調整成可以一次買賣多種貨幣
                list_other_customers=db.get_other_customer()
                n = len(list_other_customers)
                # 先用3個以內測試驗算，等沒問題後再將 3 改成 n
                other_customers=random.sample(list_other_customers,random.randint(1, n))
                # print(other_customers)
                for customer in other_customers:
                    print(customer[0])
                    choose=random.choice(['buy in','sold out'])
                    opt = random.choice(['1','2','3','4','5'])
                    currency_code = currency[int(opt)-1]
                    buy=currency_code[2]
                    sold=currency_code[1]
                    if choose=='buy in':
                        money=random.randint(10,100000)
                        buy_in= money//buy
                        balance=balance+buy_in
                        print('BUY:',buy_in)
                    elif choose=='sold out':
                        money=random.randint(10,balance)
                        sold_out= money
                        balance=balance-sold_out
                        if balance<0:
                            print('餘額不足')
                            break
                        else:
                            print('SOLD:',sold_out)
                    db.random_records(customer[0], currency_code[0], buy_in, sold_out, balance, db.get_date())
                print()
        return func_title

    def currency_transaction_record(self, db, func_title):
        """ 交易紀錄 
            1. 查詢個人所有紀錄
            2. 依區間查詢個人紀錄
        """
        import datetime
        current_date = datetime.date.today()
        while True :
            subopt = input('1.查詢個人所有紀錄  2.依區間查詢個人紀錄(exit.離開): ')
        # 1. 最近一月、最近一季、最近半年、最近一年
        # 2. 輸入前後日期條件
        # 上述方法都要用 BETWEEN 語法
        # SELECT * FROM RECORD WHERE DATE_TIME BETWEEN ? AND ?
            if subopt == 'exit':
                break
            elif subopt=='1':
                db.list_record_by_account(self.account)
            elif subopt=='2':
                while True:
                    opt = input('1.最近一月 2.最近一季 3.最近半年 4.最近一年 5.輸入日期(exit.離開):')
                    days_opts = (30,90,180,365)
                    if opt == 'exit':
                        break
                    elif opt =='5':
                        date1=input('請輸入之前日期')
                        date2=input('請輸入最近日期')
                        db.account_input_date(self.account,date1,date2)
                    else:
                        days=days_opts[int(opt)-1]
                        date_ago=current_date - datetime.timedelta(days=days)
                        db.records_date(date_ago,current_date,self.account)
        return func_title

# entry point
with DB() as db:
    acustomer = Customer()
    while True:
        func_id, func_name = acustomer.show_menu()
        if func_id == 'q':
            break
        elif func_id == '':
            print(func_name)
        else:
            if acustomer.account == '':
                func_id = 'a'
                print('請先登入或註冊')
            acustomer.menu_func[func_id](db, func_name)
        print()
