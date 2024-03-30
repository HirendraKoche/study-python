"""
    Purpose: Learn various operators for Python
"""

def get_areaoftriangle(base, height):
    return 0.5 * base * height

def main():
    v_base = input("Base: ")
    v_height = input("Height: ")
    try:
        v_base = float(v_base)
        v_height = float(v_height)
        print("Area of Triangle =", get_areaoftriangle(v_base, v_height))
    except ValueError:
        print(v_base, "or", v_height, "is not number or deciaml")

main()
