import json
import random
from random import Random
import csv


def get_cost(category):
    rand = Random()
    price = 0
    if category == 1:
        price = rand.uniform(10, 30)
    elif category == 2:
        price = rand.uniform(25, 50)
    elif category == 3:
        price = rand.uniform(45, 70)
    elif category == 4:
        price = rand.uniform(70, 150)
    else:
        price = rand.uniform(150, 300)

    return round(price, 2)


animal_list = []
with open("animal_list.txt", 'r') as file:
    for line in file:
        animal_list.append(line.strip('\n'))

city_names = ['Rome', 'London', 'Edinburgh', 'Barcelona', 'Lisbon', 'Paris', 'Athens', 'Reykjavik', 'Berlin', 'Dublin']
headers = ['Lodging', 'Lodging_type', 'located-at', 'Cost_person_night', 'Quality', 'Room_sizes']

quality_distribution = []
for i in range(5):
    for j in range(3):
        quality_distribution.append(i + 1)

types = ['hotel', 'hostel', 'youth_hostel', 'b_and_b', 'guesthouse', 'rural_house', 'apartment', 'eco_hotel', 'resort']

info = []

for city in city_names:
    hotel_names = []
    hotel_categories = []
    for i in range(15):
        rand = Random()
        number = rand.randint(0, len(types) - 1)
        hotel_category = types[number]
        number = rand.randint(0, len(animal_list) - 1)
        hotel_name = hotel_category.capitalize() + "_" + city + "_" + animal_list[number]
        hotel_names.append(hotel_name)
        hotel_categories.append(hotel_category)

    permutation = random.sample(quality_distribution, len(quality_distribution))
    for i in range(len(permutation)):
        cost = get_cost(permutation[i])
        hotel_info = (hotel_names[i], hotel_categories[i], city, cost, permutation[i], '1;2;3')
        info.append(hotel_info)

with open('hotels.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(info)
