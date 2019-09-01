import random
#生成随机数
answer=random.randint(1,100)
#玩家输入数值
n=int(input('Please input num (1-100):'))
#判断输入数字大小
while n!=answer:
    if n>answer:
        n = int(input('输入数字大于它请重新输入：'))
    elif n<answer:
        n = int(input('输入数字小于它请重新输入：'))
#输入答案正确，游戏结束
print('输入答案正确，游戏结束')