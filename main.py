class Calculator:
	def __init__(self):
		self.operator = ""
		self.rezultat = ""
		
	def add(self, a, b):
		self.rezultat = a + b
		
	def divide(self, a, b):
		self.rezultat = a / b
		
	def get_rezultat(self):
		return self.rezultat
		
	def set_operator(self, operator):
		self.operator = operator
		
instance = Calculator()
instance.divide(2, 4)
instance.get_rezultat()