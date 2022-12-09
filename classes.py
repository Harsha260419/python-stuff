class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(f"please welcome {self.name} who is here to talk with us about brain and reasons why you procrastinate and how to avoid it")      
p1 = Person("Mel Robbins")
print(p1.name)
p1.talk()