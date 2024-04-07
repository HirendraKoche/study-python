"""
    Study list in python.
"""

# Create empty list
v_lst1 = []
v_lst2 = list()

# Unpacking list
v_country = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
ge, fr, bg, sw, *sc, es = v_country
print(f"{ge}, {fr}, {bg}, {sw}, {sc}, {es}")

# Slicing list
v_country = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
print(v_country[1:4])
print(v_country[1::])
print(v_country[::-1])  # print list in reverse order
print(v_country[::2])  # Skip one item in-between. 
 
# Modifying list
print(v_country)
v_country[3] = "India"
print(v_country)
v_country[4] = "UK"
print(v_country)

# Checking Item in list
is_ukexist = "uk".casefold() in map(str.casefold, v_country)
print(is_ukexist)

# Addding item to list
v_country.append("Ireland")
print(v_country)

# Removing item from list
try:
    v_country.remove("India")
    print(v_country)
except ValueError:
    print(f"Item does not exist in {v_country}")

# Removing item using pop()
v_country.pop() # By default remove last item. Accept index to remove item from specific index.
print(v_country)

# Deleting range of items from list
del v_country[1:4]
print(v_country)
del v_country  # delete complete list
try:
    print(v_country)
except NameError as e:
    print(e)

# Clearing list
v_country = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
print(v_country)
v_country.clear()    # Only removes all item of list. Does not delete the list itself.
print(v_country)

# Copy list
v_country = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
v_countrycopy = v_country
print(v_countrycopy)

# Sorting list
v_country.sort()
print(v_country)

# Exercise
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min = ages[0]
max = ages[-1]
print(f"Min = {min} \nMax = {max}")

ages.extend([min, max])
print(ages)