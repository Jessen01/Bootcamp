# list1 = [5, 10, 15, 20, 25, 50, 20]
# if 20 in list1:
#     list1.pop(3)
#     list1.insert(3,200)
#     print(list1)


# Accept a number from the user and print its multiplication table

# numbers = range(1, 13)
# user_num = int(input("please enter a number: "))

# for number in numbers:
#   print(f"{number} x {user_num} = {number* user_num}")
#   print("\n")


# exercise 1
# myfavnum = {420,100}
# myfavnum.add(10)

# print(myfavnum)
# myfavnum.remove(100)

# friendnum = {500,600}
# newnum = myfavnum.union(friendnum)
# print(newnum)


# exercise 2
# Given a tuple which value is integers, is it possible to add more integers to the tuple?
# NO


# exercise 3
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]  # a list

# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("Kiwi")
# basket.insert(0,"Apples")
# print(basket)
# new = basket.count("Apples")
# print(new)
# basket.clear()
# print(basket)


# exercise 4
# Recap – What is a float? What is the difference between an integer and a float?
# Can you think of another way to generate a sequence of floats?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).


# A float is a number with decimal values
# Use the random.random() built it functions


# flist = []

# for i in range(1, 6):
#     i = i + 0.5
#     flist.append(i)
#     if i > 5:
#         break
#     flist.append(flist[-1] + 0.5)

# print(flist)


# exercise 5
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.


# for i in range(1,21):
#     print(i)


# for i in range(1,21):
#     if i % 2 == 0:
#      print(i)


# exercise 6
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.


# name = ''
# while name != "pragasen":
#     name = input("Whats your name?")


# exercise7

fav_fruits = input('Write your favourite fruits with a space in between ').split(' ')
fruit = input('Name any fruit: ')

if fruit in fav_fruits:
    print('You chose one of your favorite fruits! Enjoy')
else:
    print('You chose a new fruit. I hope you enjoy!')


# exercise8

# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

topping = ''
topping_list = []
while topping == '' or topping != 'quit':
    topping = input('Provide a pizza topping: ')
       print(f'Will add this ' + [topping])
    if topping != 'quit':
        topping_list.append(topping)
    else:
        print(f'Toppings: {" ".join(topping_list)}')
        print(f'Total Price: {10 + (len(topping_list) * 2.5)}')


# exercise9
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Ask a family the age of each person who wants a ticket.
# Store the total cost of all the family’s tickets and print it out.

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

# ages = input('Enter the ages of your family members separated by a comma: ').split(',')
# total_price = 0

# for age in ages:
#     age = int(age)
#     if age >=3 and age < 12:
#         total_price += 10
#     elif age >= 12:
#         total_price += 15
# else:
#     print(total_price)


# names = ['Abdul', 'Kumar', 'Rajen']
# allowed = []

# for name in names:
#     age = int(input(f'Whats your age {name}? '))
#     if age < 16 or age > 21:
#         allowed.append(name)
# else:
#     print(allowed)



# exercise 10
# Use the above list called sandwich_orders.
# Make an empty list called finished_sandwiches.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.

# sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

# finished_sandwiches = []
# for sandwich in sandwich_orders:
#     finished_sandwiches.append(sandwich)
# else:
#     print(f'Sandwiches made: {", ".join(finished_sandwiches)}')
#     print(finished_sandwiches)

# exercise 11


# Using the list sandwich_orders from the previous exercise, make sure the sandwich ‘pastrami’ appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.


# sandwich_orders.append(sandwich_orders[-1])
# sandwich_orders.append(sandwich_orders[-1])
# print(sandwich_orders)

# print('No pastrami available.')

# finished_sandwiches = []
# for sandwich in sandwich_orders:
#     if sandwich == 'Pastrami sandwich':
#         sandwich_orders.remove(sandwich)
#     else:
#         print(f'Making {sandwich}')
#         finished_sandwiches.append(sandwich)
# else:
#     print(f'Sandwiches made: {", ".join(finished_sandwiches)}')


# while sandwich == 'Pastrami sandwich' in sandwich_orders:
#     sandwich_orders.remove(sandwich)

    