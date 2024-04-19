# # Exercises: Day 14

# from functools import reduce

# countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# cap_countries = map(lambda country: country.upper(), countries)
# for country in cap_countries:
#     print(country)

# largest_name = reduce(lambda x, y: x if len(x) > len(y) else y, names)
# print(largest_name)

# even_num = filter(lambda x: True if x % 2 == 0 else False, numbers)
# for num in list(even_num):
#     print(num)

# # Closures
# def capitalize():
#     def f_upper(list_lt):
#         return [x.upper() for x in list_lt]
#     return f_upper

# cap = capitalize()
# print(cap(names))

# # Decorators

# def capitalize_1(func):
#     def wrapper(list_lt):
#         f_list = func(list_lt)
#         return [x.upper() for x in f_list]
#     return wrapper

# @capitalize_1
# def cap(list_lt):
#     return list_lt

# print(cap(countries))


# def even_gt_fifty(func):
#     def wrapper(list_lt):
#         f_list = func(list_lt)
#         f_filter = filter(lambda x: True if x % 2 == 0 else False, f_list)
#         return list(f_filter)
#     return wrapper
  
# @even_gt_fifty
# def get_even(list_lt):
#     return [x for x in list_lt if x > 50]

# print(get_even(range(101)))

# # Use map to create a new list by changing each number to its square in the numbers list
# sq_number = map(lambda x: x**2, numbers)
# print(list(sq_number))

# # Use map to change each name to uppercase in the names list
# upper_name = map(lambda name: name.upper(), names)
# print(list(upper_name))

# # Use filter to filter out countries containing 'land'.
# country_land = filter(lambda name: True if name.find("land") != -1 else False, countries)
# print(list(country_land))

# # Use filter to filter out countries having exactly six characters.
# country = filter(lambda name: True if len(name) == 6 else False, countries)
# print(list(country))

# # Use filter to filter out countries containing six letters and more in the country list.
# country = filter(lambda name: True if len(name) >= 6 else False, countries)
# print(list(country))

# # Use filter to filter out countries starting with an 'E'
# country_land = filter(lambda name: True if name.startswith("E") else False, countries)
# print(list(country_land))

# list_st = countries + names + numbers


# # Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
# def get_str(func):
#     def wrapper(list_lt):
#         f_list = func(list_lt)
#         return [item for item in f_list if isinstance(item, str)]
#     return wrapper

# @get_str
# def get_string_lists(list_lt):
#     return list_lt

# print(get_string_lists(list_st))

# # Use reduce to sum all the numbers in the numbers list.
# sum_num = reduce(lambda x, y: x+y, numbers)
# print(sum_num)

# # Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
# country_list = reduce(lambda x, y: x+", "+y, countries)
# print(country_list)

# # Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
# from data.countries import countries as ctr

# def get_pattern(func):
#     def wrapper(list_lt, ptr):
#         f_list = func(list_lt)
#         return [item for item in f_list if item.find(ptr) != -1]
#     return wrapper

# @get_pattern
# def categorize_countries(list_lt):
#     return list_lt

# print(categorize_countries(ctr, "stan"))

# # Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter

# def get_isd_dic(list_lt) -> dict:
#     ctr = {}
#     for item in list_lt:
#         ptr = item[:3]
#         ctr[ptr] = item
#     return ctr

# print(get_isd_dic(countries).items())

# Sort countries by name, by capital, by population
def sort_by_name(list_lt: list, reverse: bool = False) -> list:
    cs_lt = sorted(list_lt, key=lambda item: item["name"], reverse=reverse)
    return cs_lt

def sort_by_capital(list_lt: list, reverse: bool = False) -> list:
    cs_lt = sorted(list_lt, key=lambda item: item["capital"], reverse=reverse)
    return cs_lt

def sort_by_population(list_lt: list, reverse: bool = False) -> list:
    cs_lt = sorted(list_lt, key=lambda item: item["population"], reverse=reverse)
    return cs_lt

from data.countriesdata import countries_data
import json 

with open("sorted_coutry_data.json", "w") as data_file:
    json.dump(sort_by_population(countries_data, reverse=True), data_file, indent=2)