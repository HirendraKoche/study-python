"""
    develop to study strings
"""

from math import pi as PI

# String Formating 1
v_fname = "Hirendra"
v_lname = "Koche"
print(f"My name is %s %s" %(v_fname, v_lname))

# String formating 2
v_radias = 10
v_areaofcircle = PI * v_radias**2
print(f"Area of circle with radia %d is %.2f" %(v_radias, v_areaofcircle))

# New String formating
a = 7
b = 3
print("{} + {} = {}".format(a, b, a+b))
print("{} - {} = {}".format(a, b, a-b))
print("{} * {} = {}".format(a, b, a*b))
print("{} / {} = {:.2f}".format(a, b, a/b))

# Radia of circle with new formating
v_radias = 20
print("Area of circle with radias {} is {:.2f}".format(v_radias, PI*v_radias**2))

# String interpolation
a = 7
b = 3
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b:.2f}")
print(f"{a} ** {b} = {a**b}")

# Radius of circle with string interpolation
v_radias = 10
print(f"Area of circle with radias {v_radias} is {PI*v_radias**2 :.2f}")

# String as sequence of charectors
v_lang = "Python"
print(v_lang[-1])

# String slicing
v_lang = "Python"
print(v_lang[::-1])

# String Methods
v_lang = "      hirendra koche is a programmer.        "
print(v_lang.capitalize())
print(v_lang.count('ny'))
print(v_lang.casefold().endswith('y'))
print(v_lang.title())
print(v_lang.strip())


# Exersize String
v_strlist = ["Thrity", "Days", "Of", "Python"]
v_strlist2 = ["Coding", "For", "All"]
print(" ".join(v_strlist))
print(" ".join(v_strlist2))

v_company = " ".join(v_strlist2)
print(len(v_company))
print(v_company.upper())
print(v_company.lower())
print(v_company.capitalize())
print(v_company.title())
print(v_company.swapcase())
print(v_company.split()[0])
print(v_company.index("Coding"))
print(v_company.find("Coding"))
print(v_company.count("Coding"))
print(v_company.replace("Coding","Python"))
print(v_company.replace("All", "Everyone"))
print(v_company.split())
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))
print(v_company[0])
print(v_company.__len__()-1)
print(v_company[-1])
print(v_company[10])

v_str = "Python For Everyone"
v_stracr = "".join([x[0] for x in v_str.split()])
print(v_stracr)

v_str = "Coding For All"
v_stracr = "".join([x[0] for x in v_str.split()])
print(v_stracr)

print(v_str.index("F"))

v_str = "Coding For All People"
print(v_str.rfind("l"))

v_str = "You cannot end a sentence with because because because is a conjunction"

v_strslic = v_str[v_str.index("because"):v_str.rindex("because")+len("because")]
print(v_strslic)

print("Coding For All".startswith("Coding"))
print("30DaysOfPython".isidentifier())
print("{}".format("thirty_days_of_python").isidentifier())

radius = 10
area = PI * radius ** 2
print(f"The area of a circle with radius {radius} is {area:.2f} meters square.")

a = 8
b = 6
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b :.2f}")
print(f"{a} % {b} = {a%b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} ** {b} = {a**b}")