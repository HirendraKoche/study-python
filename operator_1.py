"""
    Purpose: Learn various operators for Python
"""

from math import pi as PI


def get_areaoftriangle(base, height):
    return 0.5 * base * height

def get_perimeteroftriangle(side_a, side_b, side_c):
    return side_a + side_b + side_c

def get_areaofcircle(radius):
    return round(PI * radius ** 2, 2)

def main():
    v_radius = input("Radius: ")
    try:
        v_radius = float(v_radius)
        print("Area of Circle = ", get_areaofcircle(v_radius))
    except ValueError:  
        print("One of the provided inputs is not number or deciaml")

try:
    main()
except KeyboardInterrupt:
    print("\nUser terminated execution")
finally:
    print("Good Bye!")
