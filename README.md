# 碼寶中級專題範例 - 發大財貨幣銀行

> 外幣是近幾年來逐漸熱門的投資工具，相對於股市的劇烈震盪，風險較低，不只是出國時的必備項目，也是投資的好工具。

## 專題作者

### Camille Tseng

[專題網站](https://cam-ille.github.io/)

## 主要功能

### 銀行

* 匯率查詢  
可查詢即時匯率

* 幣別匯率變動參數設定  
可設定 1.各種幣別的上下限範圍 2.每次變動的範圍

* 顧客交易紀錄  
可查詢 1.全部 2.不分客戶依區間查詢 3.個人交易紀錄

### 顧客

* 登入．註冊  
考生登入或註冊，無須設定密碼

* 買進/賣出  
模擬多人同時進行買賣各種貨幣

* 個人交易紀錄  
可查詢 1.個人所有交易紀錄 2.依區間查詢個人紀錄

## 測試方式

### 測試環境

| 項目 | 描述 |
| ------- | ------------ |
| 作業系統 | Windows 7/10 |
| Python 3 版本 | 3.7.3 |
| 終端機工具 | VS Code 整合式終端機 |

### 測試步驟

1. 切換到 code 資料夾  
\> cd micropyone.github.io\code 

1. 資料庫初始化  
\> python dbinit.py

1. 進入測驗中心  
\> python atestcenter.py

1. 參測考生登入  
\> python aexaminee.py