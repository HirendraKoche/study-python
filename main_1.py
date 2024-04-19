import functions as f
import data.countriesdata as cd
from modules.userid import *
from modules.gencolor import generate_colors

print("Most Spoken languages")
for lang in f.most_spoken_languages(cd.countries_data, 10):
    print(f"{lang[0]} = {lang[1]}")

print("\nMost populated contries")
for country in f.most_populated_countries(cd.countries_data, 10):
    print(f"{country[0]} = {country[1]}")

print(random_user_id())
print(user_id_gen_by_user())

print(generate_colors('hexa', 5))
print(generate_colors('rgb', 5))
