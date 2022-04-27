import os


def format_city_instance(city_info, city_slots):
    result = '(' + city_info[0] + ' of City\n'
    for i in range(len(city_info)):
        if i > 0:
            if type(city_info[i]) is list:
                aux = ''
                for j in range(len(city_info[i])):
                    aux += city_info[i][j] + ' '
                result += '(' + city_slots[i] + ' ' + aux + ')\n'
            else:
                result += '(' + city_slots[i] + ' ' + city_info[i] + ')\n'

    result += ')'
    return result


city_info = ['Mataro', 'Spain', ['Sagrada_Familia', 'La_Boqueria']]
city_slots = ['City', 'is-in', 'has-access-to']

res = format_city_instance(city_info, city_slots)
definstance = '(definstances cities\n'
definstance += res
definstance += ')'
print(definstance)
