class Parent(object):

	def override(self):
		print "Parent override()"

	def implicit(self):
		print "Parent implicit()"

	def altered(self):
		print "Parent altered()"

class Child(Parent):

	def override(self):
		print "Child override()"

	def altered(self):
		print "Child, before parent altered()"
		super(Child, self).altered()
		print "Child, after parent altered()"


parent = Parent()
child = Child()

parent.implicit()
# Implicit Inheritance
child.implicit()
print "\n"
parent.override()
# Override Explicitly
child.override()
print "\n"
parent.altered()
# inherits altered function from parent class with super
child.altered()