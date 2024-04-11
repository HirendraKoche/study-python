import functions as f
import countriesdata as cd

print("Most Spoken languages")
for lang in f.most_spoken_languages(cd.countries_data, 10):
    print(f"{lang[0]} = {lang[1]}")

print("\nMost populated contries")
for country in f.most_populated_countries(cd.countries_data, 10):
    print(f"{country[0]} = {country[1]}")
