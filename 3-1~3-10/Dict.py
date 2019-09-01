student={1:'jack',2:'bob',3:'marry',4:'micle'} #定义键值对
print(student[3])

student[5]='51zxw'#增加键值对
print(student)

#修改键值
student[2]='harry'
print(student)

#删除键值 del
del student[1]
print(student)

#清空字典键值，只清空字典里的值
student.clear()
print(student)
'''
#彻底删除字典，打印会报错
del student
print(student)
'''





