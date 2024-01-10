#!/usr/bin/python3
"""this 10-square"""
Rectangle =__import__("9-rectangle").Rectangle


class Square(Rectangle):
	"""this is the square class that inherits from the class Rectangle"""
	def __init__(self, size):
		super().__init__(size, size)

s = Square(13)

print(s)
print(s.area())