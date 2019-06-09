"""
題目：奇偶秘差 (APCS-1060304-1)
輸入：任意數 n
處理：產生 n 個數值，範圍 10 的 12~15 次方
(+3) 分別計算奇位數和及偶位數和
(+1) 奇位數和相減偶位數和，取絕對值，即為秘密差
輸出：
(+1) 數字、奇位數和、偶位數和、秘密差
(+2) 最大及最小秘密差的數值
"""
import random
n=int(input('n:'))
for i in range(n):
    number = str(random.randint(10**12,10**15))
    print(number)
    number1 = number[0::2]
    number2 = number[1::2]
    sum1 = 0
    sum2 = 0
    for c in number1:
        sum1 += int(c)
    for c in number2:
        sum2 += int(c)
    print(sum1, sum2)
    print(abs(sum1-sum2))