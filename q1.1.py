class Parent(object):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

class Child(Parent):
	def __init__(self,a,b,c):
		super().__init__(a,b,c)
	def area(self):
 		s=(self.a+self.b+self.c)/2
 		area=(s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
 		return area


area = Child(4,8,10)
print(area.area())
