# UserID module

import random as rd
import string as st

# Writ a function which generates a six digit/character random_user_id
def random_user_id():
    char = st.ascii_lowercase + st.digits
    return ''.join(rd.sample(char, 6))

# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user() -> list:
    n_char = int(input("Enter number of characters: "))
    n_id = int(input("Number of IDs required: "))
    char = st.ascii_lowercase + st.digits
    ids_lt = ["".join(rd.choices(char, k=n_char)) for _ in range(n_id)]
    return ids_lt
