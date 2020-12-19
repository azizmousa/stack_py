from Node import Node


class Stack:

	def __init__(self):
		self.__top = None
		self.__size = 0

	def push(self, value):
		n = Node(value)
		n.next_ptr = self.__top
		self.__top = n
		self.__size +=1


	def pop(self):
		if self.__size > 0:
			self.__top = self.__top.next_ptr
			self.__size -= 1

	def get_top(self):
		if self.__size > 0:
			return self.__top.value
		else:
			return None

	def size(self):
		return self.__size