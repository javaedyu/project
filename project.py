# coding=gbk
import random
secret = random.randint(1,100)
guess = 0
tries = 0
print "来猜数字！你有7次机会"
while guess != secret and tries < 7:
    guess = input("输入一个数字")
    if guess <secret:
        print "太小"
    elif guess >secret:
        print "太大"
    tries = tries + 1
if guess == secret:
    print "猜对了"
    num = str(tries)
    print '你用掉了'+num+'次机会'
else:
    print "你没猜对"
    print  "你输了"
raw_input("按回车结束")

