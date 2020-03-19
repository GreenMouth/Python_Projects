# key is "animal_name"
# value is "location" 
# A dictionary (or list) declaration may break across multiple lines

zoo_animals = { 'Unicorn' : 'Cotton Candy House',
                'Sloth' : 'Rainforest Exhibit',
                'Bengal Tiger' : 'Jungle House',
                'Atlantic Puffin' : 'Arctic Exhibit',
                'Rockhopper Penguin' : 'Arctic Exhibit'}

# Removing the 'Unicorn' entry (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']

# Your code here!
zoo_animals['Rockhopper Penguin'] = 'Some Beautiful Location'
print(zoo_animals)

""" Removing item from a list """
backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove('dagger')
print(backpack)

""" Dictionary final practicce """

inventory = {
            'gold' : 500,
            'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
            'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
            }

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] = inventory['gold'] + 50

