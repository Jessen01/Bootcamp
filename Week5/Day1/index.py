
# exercise 1

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
cat1 = Cat('Tom',4)
cat2 = Cat('Jerry',1)
cat3 = Cat('Pravin',3)
def oldest(c1,c2,c3):
    cats = [c1.age,c2.age,c3.age]
    return max(cats)
print(f'The oldest cat is {oldest(cat1,cat2,cat3)} years old.')




# exercise 2

class Dog:
    def __init__(self,name,height):
        self.name = name
        self.height = height

def bark(self):
    print(f"{self.name}goes woof woof")

    def jump(self):
        print(f'{self.name} jumps {self.height * 2} cm high!')


davids_dog = Dog('Rex', 50)
print(davids_dog.name)
print(davids_dog.height)
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog('Teacup', 20)
print(sarahs_dog.name)
print(sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(davids_dog.name)
else:
    print(sarahs_dog.name)
