class Parent_1:
    def parent_1_message1(self):
        print("This is parent One class")

class Parent_2:
    def parent_2_message1(self):
        print("This is parent Two class")

class Child1(Parent_1,Parent_2):
       def child1_message1(self):
        print("This is Child1 class")

class Child2(Parent_1):
       def child2_message1(self):
        print("This is Child2 class")

c_1 = Child1()
c_1.parent_1_message1()
c_1.parent_2_message1()


