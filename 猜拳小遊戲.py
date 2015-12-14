
# coding: utf-8

# In[ ]:

import random
猜拳=['剪刀','石頭','布']
while True:
    person=input("猜拳[請輸入放棄來投降]:")
    if person=='放棄':
        print("嫩逼")
        break
    elif person in 猜拳:
        a=random.choice(猜拳)
        print(a)
        if person==a:
            print("平局")
    else:
        print("你看得懂中文嗎??")

