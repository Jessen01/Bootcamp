
# exercise 1

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# cat1 = Cat('Tom',4)
# cat2 = Cat('Jerry',1)
# cat3 = Cat('Pravin',3)
# def oldest(c1,c2,c3):
#     cats = [c1.age,c2.age,c3.age]
#     return max(cats)
# print(f'The oldest cat is {oldest(cat1,cat2,cat3)} years old.')




# exercise 2

# class Dog:
#     def __init__(self,name,height):
#         self.name = name
#         self.height = height

# def bark(self):
#     print(f"{self.name}goes woof woof")

# def jump(self):
#         print(f'{self.name} jumps {self.height * 2} cm high!')


# davids_dog = Dog('Rex', 50)
# print(davids_dog.name)
# print(davids_dog.height)
# davids_dog.bark()
# davids_dog.jump()

# sarahs_dog = Dog('Teacup', 20)
# print(sarahs_dog.name)
# print(sarahs_dog.height)
# sarahs_dog.bark()
# sarahs_dog.jump()

# if davids_dog.height > sarahs_dog.height:
#     print(davids_dog.name)
# else:
#     print(sarahs_dog.name)



# exercise3

# Exercise 3 : Who’s The Song Producer?
# Instructions
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# Create an object, for example:

# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])


# Then, call the sing_me_a_song method. The output should be:

# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven


class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        # for line in self.lyrics:
        #     print(line)
        list(map(lambda line: print(line), self.lyrics))


stairway = Song(["Theres a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()


# exercise 4

# Exercise 4 : Afternoon At The Zoo
# Instructions
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Example

# {
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }


# Create a method called get_groups that prints the animal/animals inside each group.

# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        grouped_animals = {}
        curr_group = []
        counter = 1

        for animal in sorted(self.animals):
            if not curr_group:
                curr_group.append(animal)
            elif animal[0] == curr_group[0][0]:
                curr_group.append(animal)
            else:
                if len(curr_group) == 1:
                    grouped_animals[counter] = curr_group[0]
                else:
                    grouped_animals[counter] = curr_group
                curr_group = [animal]
                counter += 1

        if len(curr_group) == 1:
            grouped_animals[counter] = curr_group[0]
        else:
            grouped_animals[counter] = curr_group

        return grouped_animals

    def get_groups(self):
        print(self.sort_animals())


ramat_gan_safari = Zoo('myzoo')
ramat_gan_safari.add_animal('Ape')
ramat_gan_safari.add_animal('Aardvark')
ramat_gan_safari.add_animal('Bear')
ramat_gan_safari.add_animal('Baboon')
ramat_gan_safari.add_animal('Eel')
ramat_gan_safari.add_animal('Giraffe')
ramat_gan_safari.add_animal('Zebra')
ramat_gan_safari.add_animal('Zebu')
ramat_gan_safari.get_groups()