#!/usr/bin/python3
"""
Inheriting from base class
methods:
__init__(self, width, height, x=0, y=0, id=None)
"""
from models.base import Base


class Rectangle(Base):
	"""
	Class that inherits from base class
	"""

	def __init__(self, width, height, x=0, y=0, id=None):
		self.__width = width
		self.__height = height
		self.__x = x
		self.__y = y
		super().__init__(id)

	@property
	def width(self):
		"""Retrieve the width."""
		return self.__width

	@width.setter
	def width(self, value):
		"""Sets the width to a value."""
		if type(value) is not int:
			raise TypeError("width must be a integer")
		if value < 0:
			raise ValueError("width must be >= 0")
		self.__width = value

	@property
	def height(self):
		"""Retrieve the height."""
		return self.__height

	@height.setter
	def height(self, value):
		"""Sets the height to a value."""
		if type(value) is not int:
			raise TypeError("height must be an integer")
		if value < 0:
			raise ValueError("height must be >= 0")
		self.__height = value

	@property
	def x(self):
		"""Retrieve the x."""
		return self.__x

	@x.setter
	def x(self, value):
		"""Sets the x to a value."""
		if type(value) is not int:
			raise TypeError("x must be an integer")
		if value < 0:
			raise ValueError("x must be >= 0")
		self.__x = value

	@property
	def y(self):
		"""Retrieve the y."""
		return self.__y

	@y.setter
	def y(self, value):
		"""Sets the y to a value."""
		if type(value) is not int:
			raise TypeError("y must be an integer")
		if value < 0:
			raise ValueError("y must be >= 0")
                self.__y = value
