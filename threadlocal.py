# -*- coding: utf-8 -*-
import threading

# 创建全局的threadlocal对象：
local_school = threading.local()

def process_student():
	# 获取当前线程关联的student
	std = local_school.student[0]
	print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name,age):
	# 绑定threadlocal的student
	local_school.student = (name,age)
	process_student()

t1 = threading.Thread(target = process_thread, args=('Alice','25'),name='Thread-A')
t2 = threading.Thread(target = process_thread, args=('Bob','25'),name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

# if __name__ == '__main__':
# 	main()		