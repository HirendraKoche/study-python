# Color Generator Module
import random as rd
import string as st

# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each)
def rgb_color_gen():
    rgb = str(rd.randint(0,255)) + "," + str(rd.randint(0,255)) + "," + str(rd.randint(0,255))
    return f"rgb({rgb})"

# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f.
def list_of_hexa_colors(num: int) -> list:
    char = st.digits + 'abcdef'
    hex_list = ['#' + "".join(rd.choices(char, k=6)) for _ in range(num)]
    return hex_list

# Write a function list_of_rgb_colors which returns any number of RGB colors in an array
def list_of_rgb_colors(num: int) -> list:
    rgb_list = [rgb_color_gen() for _ in range(num)]
    return rgb_list

# Write a function generate_colors which can generate any number of hexa or rgb colors
def generate_colors(format: str, num: int) -> list:
    if format.casefold == 'hexa'.casefold:
        return list_of_hexa_colors(num)
    elif format.casefold == 'rgb'.casefold:
        return list_of_rgb_colors(num)
    else:
        print("Color format must be one of 'rgb' or 'hexa'.")
