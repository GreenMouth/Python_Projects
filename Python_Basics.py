
# Author: Prashant Shinde

print('Hello World')

x = 1
if x > 0:
    print('X is greater than 0')
else:
    print('x is less than 0')

# VARIABLES: use lower case becasue python class are defined using capital word
age = 1.5 # dont need to define a datatype
print(type(age))
#str(), int(), flaot()
number = float(1) # casting
print(type(number))
number_and_age = (number, age) # tuple
print(number_and_age)

# list, tuple, dictionary, frozenset, set
# mutable: can be changed (list)
our_list = ["a","b","c", 1.5] # list with multiple datatypes
print(our_list)
# Immutable: can not be changed (tuple)
our_tuple = ("a", "b", "c", 1.5)
print('Tuple Count:', len(our_tuple))
print(our_tuple)
our_dictionary = {"Name":"Prashant", "School":"Georgia Tech"}
print(our_dictionary)
print('Name in our_dictionary is:', our_dictionary['Name'])
our_set = {"one", "two", "three", "two"} # sets are defined same as dictionary but are unordered
print(our_set) # sets are useful to do unions, intersection, etc.
our_frozenset = frozenset(our_set) # frozenset are Immutable, sets are mutable
print(our_frozenset)
# Analogy = tuple : list :: frozenset: set (different applications of mutable and Immutable objects)

# NUMBERS
import math
x = 1
y = 1.5
z = 2+3j # real & complex variable
print(type(z)) # <type 'complex'>
result = x * y # +, -, /, *, %
print(result)
print(math.ceil(y)) # lowest INT higher than y

# LISTS (heterogeneoud data allowed, keeps order, mutable = changable (append, etc.))
our_list = ["a", "b", "c", 1, 1.5]
print(type(our_list))
print(our_list[0])
our_list.insert(0, "First_Element") # INSERT takes 2 elements vs APPEND takes only 1 element
print('Inserted', our_list)
our_list.remove('First_Element') # REMOVE vs POP
print('Removed:', our_list)
our_list.pop(len(our_list) - 1) # last element of list will be removed
print('POP:', our_list)
nested_list = [[1,2,3], "a", "b"]
print('nested_list:', nested_list)
print('nested_list type:', type(nested_list))

# STRINGS (is made up of an array of elements): String delimiter is "" or ''
string_a = "Shinde"
print(len(string_a))
print(string_a[0])
print('Upper:', string_a.upper())
print('Upper:', string_a.lower())
string_b = "Prashant, Shinde, Georgia Tech"
print(string_b.split(","))

# TUPLES ()
tuple_a = ('cat', 'dog', 'mouse') # use tuple instead of  list if you don't want to update any value
try:
    tuple_a.append('A')
except:
    print('Tuple is Immutable object; can not append new values')
