

# from typing import AsyncGenerator


# class Employee : 
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary

#     def increment_sal(self, amount):
#         self.salary+=amount

# jack = Employee("Jack", 21, 20000)
# jack.increment_sal()

# tom = Employee("Tom", 21, 20000)
# tom.increment_sal()

















class Person():
	
	# Constructor
	def __init__(self, name):
		self.name = name

	# To get name
	def getName(self):
		return self.name

	# To check if this person is an employee
	def isEmployee(self):
		return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

	# Here we return true
	def isEmployee(self):
		return True

# Driver code
emp = Person("Jack") # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Tom") # An Object of Employee
print(emp.getName(), emp.isEmployee())




print("This is new")








