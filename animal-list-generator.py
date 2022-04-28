with open('animal-dataset.json', 'r') as file:
    data_set = json.load(file)

animal_list = []
for element in data_set['results']:
    name = element['name']
    animal_name = name.replace(" ", "_")
    animal_list.append(animal_name)

with open("animal_list.txt", 'w') as file:
    for animal in animal_list:
        print(animal, file=file)