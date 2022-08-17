# sample_dict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }

# print(sample_dict['class']['student']['marks']['history'])


sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys_to_remove = ["name", "salary"]

for m in keys_to_remove:
    sample_dict.pop(m)
print(sample_dict)

# exercise1

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# x = zip(keys,values)
# print(set(x))

# exercise2

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0

for i in family.values():
    if i >=3 and i < 12:
        total_cost += 10
    elif i >= 12:
        total_cost += 15
else:
    print(total_cost)


# exercise 3

brand = { 
"name": "Zara",
"creation_date": 1975,
"creator_name": "Amancio Ortega Gaona",
"type_of_clothes":['men', 'women', 'children', 'home'],
"international_competitors": ['Gap', 'H&M', 'Benetton'] ,
"number_stores": 7000 ,
"major_color": {
    "France": "blue", 
    "Spain": "red", 
    "US": ['pink', 'green']
}
}

# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values). ok
# 3. Change the number of stores to 2. ok
# 4. Print a sentence that explains who Zaras clients are.
# 5. Add a key called country_creation with a value of Spain. ok
# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
# 7. Delete the information about the date of creation.
# 8. Print the last international competitor.
# 9. Print the major clothes colors in the US.
# 10. Print the amount of key value pairs (ie. length of the dictionary).
# 11. Print the keys of the dictionary.
# 12. Create another dictionary called more_on_zara with the following details:
# creation_date: 1975 
# number_stores: 10 000

brand['number_stores'] = 2
# print(f'{brand["name"]} makes clothes for {", ".join(brand["type of clothes"])}.')
print(f)
brand['country_creation'] = 'Spain'
if brand.get('international_competitors'):
    brand['international_competitors'].append('Desigual')
del brand['creation_date']





