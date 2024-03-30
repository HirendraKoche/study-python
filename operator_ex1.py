"""
    Purpose: Learn various operators for Python
"""

def get_areaoftriangle(base, height):
    return 0.5 * base * height

def get_perimeteroftriangle(side_a, side_b, side_c):
    return side_a + side_b + side_c

def main():
    v_base = input("Base: ")
    v_height = input("Height: ")
    v_side_a = input("Side A length: ")
    v_side_b = input("Side B length: ")
    v_side_c = input("Side C length: ")
    try:
        v_base, v_height = float(v_base), float(v_height)
        v_side_a, v_side_b, v_side_c = int(v_side_a), int(v_side_b), int(v_side_c)
        print("Area of Triangle =", get_areaoftriangle(v_base, v_height))
        print("Perimeter of Triangle =", get_perimeteroftriangle(v_side_a, v_side_b, v_side_c))
    except ValueError:  
        print("One of the provided inputs is not number or deciaml")

try:
    main()
except KeyboardInterrupt:
    print("\nUser terminated execution")
finally:
    print("Good Bye!")
