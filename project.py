# coding=gbk
import random
secret = random.randint(1,100)
guess = 0
tries = 0
print "�������֣�����7�λ���"
while guess != secret and tries < 7:
    guess = input("����һ������")
    if guess <secret:
        print "̫С"
    elif guess >secret:
        print "̫��"
    tries = tries + 1
if guess == secret:
    print "�¶���"
    num = str(tries)
    print '���õ���'+num+'�λ���'
else:
    print "��û�¶�"
    print  "������"
raw_input("���س�����")

