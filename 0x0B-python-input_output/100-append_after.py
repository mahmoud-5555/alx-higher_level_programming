#!/usr/bin/python3
"""my module"""


def append_after(filename="", search_string="", new_string=""):
	"""insert the string after any search_string"""
	res = ''
	content = ''
	with open(filename, 'w+',encoding='UTF8') as the_file:

		content = the_file.read()
		index = content.find(search_string)
		last= 0
		
		while index != -1:
			res += content[last : index + 1] + new_string
			last = index
			index = content[last:].find(search_string)
		