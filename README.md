# 碼寶中級專題範例 - 多益單字測驗

> TOEIC多益是一種英文檢定，考試內容範圍以職場商業英語為主。許多大學商管科系及研究所會將多益成績列為畢業門檻之一。而且不少公司徵才需要考量英語能力時，亦會參考採認多益成績。本專題旨在開發一個多益單字挑戰測驗系統，用以練習及強化多益單字能力

## 專題作者

### Bug 老師

[專題網站](https://micropyone.github.io/)

## 主要功能

### 測驗中心

* 單字建檔查詢  
可新增、修改、刪除及查詢單字，並可列出全部單字

* 選擇題型設定  
可設定 3.三選一 4.四選一 5.五選一

* 填充題型設定  
可設定 1.提示首字母 2.提示首尾字母

* 參測考生列表  
列出全部考生

* 測驗成績統計  
統計測驗人數及平均分數，並可列出全部考生的測驗紀錄

* 個人成績查詢  
查詢單一考生的測驗紀錄

### 參測考生

* 登入．註冊  
考生登入或註冊，無須設定密碼

* 選擇題測驗  
依測驗中心選擇題型設定進行測驗

* 填充題測驗  
依測驗中心填充題型設定進行測驗

* 個人成績查詢  
列出個人全部測驗紀錄

* 個人資料修改  
可修改全名、性別及出生年

* 亂數播放單字  
提供自行練習記憶單字

## 測試方式

### 測試環境

| 項目 | 描述 |
| ------- | ------------ |
| 作業系統 | Windows 7/10 |
| Python 3 版本 | 3.7.3 |
| 終端機工具 | ConEmu / VS Code 整合式終端機 |

### 測試步驟

1. 切換到 code 資料夾  
\> cd micropyone.github.io\code 

1. 資料庫初始化  
\> python dbinit.py

1. 進入測驗中心  
\> python atestcenter.py

1. 參測考生登入  
\> python aexaminee.py