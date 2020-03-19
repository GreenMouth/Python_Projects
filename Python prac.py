names = ["Adam","Alex","Mariah","Martine","Columbus"]

for x in names:
    print x
	
webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

# Add your code below!
# Prints VALUE from key-value pair

for x in webster:
    print webster[x]


	a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for x in a:
    if x%2 == 0:
        print x
		

		
# Write your function below!

def fizz_count(x):
    count = 0
    for item in x:
        if item == "fizz":
            count = count + 1
    return count

x = ["fizz", "cat", "fizz", "fizz"]
counter = fizz_count(x)
print counter
    
#String Looping
for letter in "Codecademy":
    print letter
    
# Empty lines to make the output pretty
print
print

word = "Programming is fun!"

for letter in word:
    # Only print out the letter i
    if letter == "i":
        print letter
		
		
#Supermarket

prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

for key in prices:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]


total = 0
for key in prices:
    price = prices[key] * stock[key] 
    print price
    total = total + price

print "Our total worth is = "
print total







