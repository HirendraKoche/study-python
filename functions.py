# Declare a function add_two_numbers. It takes two parameters and it returns a sum
def add_two_numbers(x, y):
    return x + y


# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
from math import pi
def area_of_circle(r):
    return pi * r ** 2


# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    sum = 0
    for x in args:
        sum += x
    return sum


# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(cel):
    return (cel * 9/5) + 32


# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer
def check_season(month: str):
    autumn_tp = ('September', 'October', 'November')
    winter_tp = ('December', 'January', 'February')
    spring_tp = ('March', 'April', 'May')
    summer_tp = ('June', 'July', 'August')

    if month in autumn_tp:
        return 'Autumn'
    elif month in winter_tp:
        return 'Winter'
    elif month in spring_tp:
        return 'Spring'
    elif month in summer_tp:
        return 'Summer'
    else:
        return None
    

# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(y, b, x=1):
    return (y - b) / x


# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number
def evens_and_odds(n: int):
    evens = 0
    odds = 0
    for x in range(n+1):
        if x % 2 == 0:
            evens += 1
        else:
            odds += 1
    return f"The number of odds are {odds}.\nThe number of evens are {evens}"


# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(n):
    fac = 1
    for x in range(1, n+1):
        fac *= x
    return fac


# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(par):
    if len(par) == 0:
        return True
    else:
        return False


import statistics
# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(l_list):
    return statistics.mean(l_list)

def calculate_median(l_list):
    return statistics.median(l_list)

def calculate_mode(l_list):
    return statistics.mode(l_list)

def calculate_range(l_list):
    return max(l_list) - min(l_list)

def calculate_variance(l_list):
    return statistics.variance(l_list)

def calculate_std(l_list):
    return statistics.stdev(l_list)


# Write a function called is_prime, which checks if a number is prime
def is_prim(num):
    result = True
    if num > 1:
        for x in range(2, (num//2 + 1)):
            if num % x == 0:
                result = False
                break
    return result


# Write a functions which checks if all items are unique in the list.
def is_unique(list_lt) -> bool:
    for x in list_lt:
        if list_lt.count(x) > 1:
            return False
    else:
        return True


# Write a function which checks if all the items of the list are of the same data type
def is_sametype(list_lt) -> bool:
    list_fst_it_type = type(list_lt[0])
    for x in list_lt[1:]:
        if list_fst_it_type != type(x):
            return False
    else:
        return True


# Write a function which check if provided variable is a valid python variable
def is_identifier(str_st: str) -> bool:
    return str_st.isidentifier()


# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
def most_spoken_languages(list_lt: list, count: int) -> list:
    lang = []
    lang_count = {}

    for x in list_lt:   # Create list of languages spoken
        lang += x["languages"]

    lang_set = set(lang)    # Get unique languages

    for x in sorted(lang_set):  # Create dictionary of languages with its count
        lang_count[x] = lang.count(x)  

    lang_count = sorted(lang_count.items(), key=lambda item: item[1], reverse=True) # Sort disctionary in reverse order based on count
    return lang_count[:count]


# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
def most_populated_countries(list_lt: list, count: int) -> list:
    contr_pop = {}
    for x in list_lt:   # Create dictionary of countries with its population
        contr_pop[x['name']] = x['population']

    result = sorted(contr_pop.items(), key=lambda item: item[1], reverse=True)  # Sort disctionary in reverse order based on population
    return result[:count]
