class Employee(object):
	'''Class for all employees'''
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
	def displayEmployee(self):
		print("Name : ", self.name,  ", Salary: ", self.salary)
emp1 = Employee("Rahul",10000)
emp2=  Employee("Mahesh",10200)
emp2.bonus=1000 # objects are dynamic in nature will not effect emp1

print(emp1.__doc__)
emp1.displayEmployee()
print(emp2.bonus)
# print(emp1.bonus) will generate Attribute error employee object does not have attribute bonus

