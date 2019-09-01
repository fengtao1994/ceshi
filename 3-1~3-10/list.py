student=['jack','bob','Hary','Micle']
print(student)
print(student[0])   #索引从0开展   -1表示最后一个
print(student[-1])

'''
#当索引超出元素值时会报错 IndexError错误
print(student[4])
'''
#末尾添加元素 append 定义
student.append('51zxw')
print(student)

#指定位置添加  insert 使用索引定义
student.insert(0,'hello')
print(student)


#修改元素 使用索引修改
student[0]='No.1'
print(student)

#删除元素  末尾删除元素 pop定义
student.pop()
print(student)
#删除元素  位置删除 pop 索引控制
student.pop(0)
print(student)



