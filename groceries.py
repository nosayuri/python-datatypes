print ("Noemi Higashi - Products Exercise")
space = """
-----------------------
"""
print (space)

products = [

    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

print ("Checkpoint 1 - Printing Products".upper())
print (space)

print ("Challenge #1 - Print all products")
print(products)
print (space)

print ("Challenge #2 - Print the first product")
first_product = products[0]
#print (type(first_product)) #returns the data type
print (first_product)
print (space)

print ("Challenge #3 - Print the name of the first product")
print (first_product["name"]) #ex3
print (space)

print ("Challenge #4 - Print the number of products")
print ("There are", len(products), "products")
#another Operations
#>> product_count_message = ("There are "+ str(len(products)) + " products")
#>> print (product_count_message)
print (space)

print ("Challenge #5 - Print the name of each product")
#as we loop each item "p" in a list of items "products", print the item "p"
for p in products: #created the variable p
    print ("- " + str(p["name"]))
print (space)

print ("Challenge #6 - Print in alphabetical order the name of each product")
def sort_by_name(p):
    return p["name"]

products_sorted = sorted(products, key=sort_by_name)
for p2 in products_sorted:
    print ("- " + str(p2["name"]))
print (space)

print ("Challenge #7 - Print in alphabetical order the name of each product, and include its price rounded to two decimal places")
for p2 in products_sorted:
    print ("- " + str(p2["name"]) + " ($"+ str("{0:.2f}".format((p2["price"])))+")")
print (space)

print ("Checkpoint 2 - Printing Departments".upper())
print (space)

print ("Challenge #8 - Print the number of unique departments")

def dpt_name (products):
    return products ["department"]
products2 = sorted (products, key=dpt_name)

for d in products2:
    print (d["department"])
#can't turn this output into a list
#problem with Keys/Value attributes into a list of dictionaries, and set
