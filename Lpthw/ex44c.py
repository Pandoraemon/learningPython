class Parent(object):
    
    def altered(self):
        print " PARENT"

class Child(Parent):
    
    def altered(self):
        print "CHILD"
        super(Child,self).altered()
        print "ChILD, afert parent"

dad = Parent()
son = Child()

dad.altered()
son.altered()
