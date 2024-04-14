# List comprehension
# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
output = [x for x in numbers if x >= 0]
print(output)

# # Flatten the following list of lists of lists to a one dimensional list
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
output = [item for list1 in list_of_lists for list2 in list1 for item in list2]
print(output)

# Using list comprehension create the following list of tuples:
output = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(output)

# Flatten the following list to a new list
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [ [country.upper(), country[:3].upper(), city.upper()] for country_city in countries for country, city in country_city]
print(output)

# Change the following list to a list of dictionaries
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output = [ " ".join(name) for fullname in names for name in fullname]
print(output)

# Write a lambda function which can solve a slope or y-intercept of linear functions
linear_solver  = lambda x1, y1, x2, y2, slope=True: (y2-y1)/(x2-x1) if slope else y1 - ((y2 - y1) / (x2 - x1)) * x1
print(linear_solver(2,8,9,10))

get_evens = lambda r: [i for i in range(r+1) if i % 2 == 0]
print(get_evens(100))

get_odds = lambda r: [i for i in range(r+1) if i % 2 != 0]
print(get_odds(100))
