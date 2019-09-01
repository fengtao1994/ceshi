#Python的元组与列表类似，不同之处在于元组的元素一旦定义就不能修改。
# 元组使用小括号，列表使用方括号。元组参加很简单，只需要在括号中添加元素，并用逗号隔开即可
course=('Chinese','English','Math','computer')
print(course)
print(course[0]) #显示第一个元素
print(course[1:3]) #显示1到3不包含3元素
print(course[1:])#显示1之后的元素包含1
print(course[:1])#显示1之前不包含1

print(len(course))  #len表示元素个数
#要定义一个只有1个元素的元组，需要在元素后面加逗号，用来消除数学歧义
t=(1,)
print(t)

score=(21,33,44,33)  #max表示输出最大值
print(max(score))



