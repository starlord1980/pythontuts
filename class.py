#!/usr/bin/env python3
#this is a demo of classes

class ClassName:
	pass

instance = ClassName()
class Students:
		def __init__(emp, name, age, pos):
			emp.name = name
			emp.age = age
			emp.pos = pos
		def displayEmployee(self):
			return("Employee name is " + emp1.name + " who is " + str(emp1.age) + " and is a " + emp1.pos)


emp1 = Students("Bob", 12, "Carpenter")
emp2 = Students("Bella", 22, "Bobsledder")
print (emp1.name)
print (emp1.age)
print (emp1.pos)

print(emp1.displayEmployee())
