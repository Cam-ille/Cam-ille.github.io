# abank.py
from dbbank import DB
class Bank:
    def __init__(self):
        self.menu_title = '銀行'
        self.menu = {
            'a':'匯率查詢',
            'b':'幣別匯率變動參數設定',
            'c':'顧客交易紀錄',
            'q':'離開',
        }
        self.menu_func = {
            'a': lambda c, s: self.exchange_rate_inquiry(c, s),
            'b': lambda c, s: self.parameter_setting(c, s),
            'c': lambda c, s: self.guest_transaction_record(c, s)
        }
        self.divider = '='*20

    def show_menu(self):
        """ 主選單
        """
        print(self.divider)
        print(self.menu_title)
        print(self.divider)
        for fid, fname in self.menu.items():
            print('%s:%s' % (fid, fname))
        print(self.divider)
        opt = input('請選擇: ').lower()
        if opt in self.menu.keys():
            return opt, self.menu[opt]
        else:
            return '', '無此功能！'

    def exchange_rate_inquiry(self, db, func_title):
        """ 匯率查詢
        """
        print('幣別  ',' 買入 ',' 賣出')
        db.list_all_currency()
        return func_title

    def parameter_setting(self, db, func_title):
        """ 幣別匯率變動參數設定
            1. 設定各種幣別的上下限範圍
            2. 設定每次變動的範圍
        """
        import random
        while True:
            currency=db.list_currency_settings()
            subopt = input('1.美元 2.港幣 3.歐元 4.日圓 5.人民幣 exit.離開: ')
            if subopt == 'exit':
                break
            else:
                set_range1 = float(input('請輸入上限範圍: '))
                set_range2 = float(input('請輸入下限範圍: '))
                change_limit= float(input('請輸入變動幅度: '))
                
                if set_range2>set_range1:
                    continue
                else:
                    db.insert_or_update_currency_rate(currency[int(subopt)-1][0],set_range2, set_range1, change_limit)            
        return func_title

    def guest_transaction_record(self, db, func_title):
        """ 顧客交易紀錄
            1. 預設可以查詢全部
            2. 不分客戶依區間查詢
            3. 查詢個人交易紀錄
                3a. 查詢個人所有紀錄
                3b. 依區間查詢個人紀錄
        """
        while True:
            import datetime
            current_date = datetime.date.today()
            # db.list_all_customer()
            # db.all_records()
            subopt = input('1.依區間查詢 2.查詢個人交易紀錄 exit.離開: ')
            if subopt == 'exit':
                break
            else:
                if subopt=='1':
                    opt = input('1.最近一月 2.最近一季 3.最近半年 4.最近一年(exit.離開):')
                    days=(30,90,180,360)
                    if opt == 'exit':
                        break
                    else:
                        days=days[int(opt)-1]
                        date_ago=current_date - datetime.timedelta(days)
                    db.records_date(date_ago,current_date)
                else:
                    while True:
                        account = input('請輸入帳號 (exit.離開): ')
                        if account == 'exit':
                            break
                        else:
                            db.list_record_by_account(account)
            print('-'*60)
        return func_title

# entry point
with DB() as db:
    abank = Bank()
    while True:
        func_id, func_name = abank.show_menu()
        if func_id == 'q':
            break
        elif func_id == '':
            print(func_name)
        else:
            abank.menu_func[func_id](db, func_name)
        print()
