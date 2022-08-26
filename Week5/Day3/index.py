# exercise 1

  # def mynumber (number):
  #   "this is my comment"

  #   print("hello")
  #   print(mynumber.__doc__)





 # exercise2

class Currency:
  def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

#Your code starts HERE


    
# Using the code above, implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.
# >>> c1 = Currency('dollar', 5)
# >>> c2 = Currency('dollar', 10)
# >>> c3 = Currency('shekel', 1)
# >>> c4 = Currency('shekel', 10)

# >>> str(c1)
# '5 dollars'

# >>> int(c1)
# 5

# >>> repr(c1)
# '5 dollars'

# >>> c1 + 5
# 10

# >>> c1 + c2
# 15

# >>> c1 
# 5 dollars

# >>> c1 += 5
# >>> c1
# 10 dollars

# >>> c1 += c2
# >>> c1
# 20 dollars

# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>





class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __add__ (self,other):
      if (isinstance(other,int)):
        return self.amount + other
      else:
        return self.amount


    def __iadd__(self,other):
      self.value = self.__add__(other)
      return self



c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
# c3 = Currency('shekel', 1)
# c4 = Currency('shekel', 10)


print(c1+5) 
print(c1+c2)
c1+=c2














