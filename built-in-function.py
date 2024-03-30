"""
    Purpose: Study built-in functions.
"""

def get_len(v_str: str):
    return len(v_str)

def get_type(v_input):
    try:
        if int(v_input):
            return "Number"
    except ValueError:
        try:
            if float(v_input):
                return "Decimal"
        except ValueError:
            if isinstance(v_input, str):
                return "String"
        
def main():
    v_str = input("Provide sample string: ")
    len_v_str = get_len(v_str)
    type_v_str = get_type(v_str)
    print("Length of string", v_str, "is", len_v_str)
    print("Type of string", v_str, "is", type_v_str)

main()
