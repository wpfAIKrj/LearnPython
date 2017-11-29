# -*- coding: utf-8 -*-
import re

def regular():
	if re.match(r'^\d{3}\-\d{3,8}$','010-123456'):
		print('正则匹配成功')
	else:
		print('正则匹配失败')

	if re.match(r'^\d{3}\-\d{3,8}$','010 123456'):
		print('正则匹配成功')
	else:
		print('正则匹配失败')

def split():
	print('字符串空格分割',re.split(r'\s+','a  b     c'))
	print('字符串空格带符号分割',re.split(r'[\s\,\;]+','a,;; b;;;,     c'))

def main():
	#主函数
	regular()
	split()

if __name__ == '__main__':
	main()			