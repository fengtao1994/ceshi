#Python提供了for循环和while循环（没有do..while循环）
#for 循环  遍历打印全部数组
student=['ja','bob','ma','mic']
for stu in  student:            #赋值到 stu
    print(stu)                  #平行打印全部

#计算1+2+3+...10的值
#Python 提供一个range()函数，可以生成一个整数序列，比如range(10)生成的序列是从0开始小于10的整数

sum=0
for i in range(11):
    sum=sum+i
print(sum)                   #不平行打印最后，注意逻辑关系

#while循环：只要条件满足，就一直循环下去，条件不满足时退出循环
n=10
while n>0:
    n=n-1
    print(n)
print('over !')



