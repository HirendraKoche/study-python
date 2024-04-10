# Create empty tuple
v_countries = ()
v_countries = tuple()

# Create a tuple containing names of your sisters and your brothers
v_sister = ("Radha", "Chichi", "Tendi", "Sisi")
v_brother = ("Chicha", "Tendu", "Soso")
v_siblings = v_sister + v_brother

# How many siblings do you have
print(f"Total Siblings = {len(v_siblings)}")

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
v_family = ("Pipi", "Momo") + v_siblings
print(f"Family = {v_family}")

# Unpack siblings and parents from family_members
v_parents, v_sib = v_family[0:2], v_family[2:]
print(f"{v_parents}\n{v_sib}")

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp
v_fruits = ("f_item1", "f_item2", "f_item3")
v_vegetables = ("v_item1", "v_item2", "v_item3")
v_animal = ("a_item1", "a_item2", "a_item3")
v_food_stuff_tp = v_fruits + v_vegetables + v_animal
print(f"v_food_stuff_tp = {v_food_stuff_tp}")

# Change the about food_stuff_tp tuple to a food_stuff_lt list
v_food_stuff_lt = list(v_food_stuff_tp)
print(f"v_food_stuff_lt = {v_food_stuff_lt}")

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list
v_mid = []
v_food_stuff_lt_len = len(v_food_stuff_lt)
if v_food_stuff_lt_len % 2 == 0:
    v_mid = v_food_stuff_lt[int(v_food_stuff_lt_len / 2 - 1) :  int(v_food_stuff_lt_len/2 + 1)]
else:
    v_mid = v_food_stuff_lt[v_food_stuff_lt_len // 2]
print(v_mid)

# Slice out the first three items and the last three items from food_staff_lt list
print(v_food_stuff_lt[:3])
print(v_food_stuff_lt[-3:])

del v_food_stuff_tp

v_nordic_countries_tp = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

if "Estonia" in v_nordic_countries_tp:
    print("Estonia exist in v_nordic_countries_tp")
if "Iceland" in v_nordic_countries_tp:
    print("Iceland exist in v_nordic_countries_tp")