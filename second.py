# -*- coding: utf-8 -*-
class Student(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return 'Student object (name:%s)' % self.name

def main():
	#主函数
	print(Student('Wang'))

if __name__ == '__main__':
	main()		