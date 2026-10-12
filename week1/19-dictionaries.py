city_by_name = {"Isa": "Nijkerk", "Sara": "Hoevelaken", "Jane": "NYC", "Ninke": "Amsterdam"}

print(city_by_name["Isa"])
print(city_by_name["Sara"])
print(city_by_name["Jane"])
print(city_by_name["Ninke"])

for name in city_by_name:
    print(f"{name} lives in {city_by_name[name]}")

for name, city in city_by_name.items():
    print(f"{name} lives in {city}")