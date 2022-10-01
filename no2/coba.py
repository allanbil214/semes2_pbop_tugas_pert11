class ClassA(object):
   def __init__(self):
         pass
class ClassB(object):
   def __init__(self):
         pass
class ClassC(object):
    def __init__(self):
        self.object_b = ClassB()
    def perform(self):
        self.object_a = ClassA()