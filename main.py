import argparse
import os
import csv


def format_instance(instance_info, class_slots):
    result = '(' + instance_info[0] + ' of ' + class_slots[0] + '\n'
    for i in range(len(instance_info)):
        if i > 0:
            val = instance_info[i].split(';')
            if len(val) > 1:
                aux = ''
                for j in range(len(val)):
                    aux += val[j] + ' '
                result += '(' + class_slots[i] + ' ' + aux + ')\n'
            else:
                result += '(' + class_slots[i] + ' ' + val[0] + ')\n'

    result += ')'
    return result


parser = argparse.ArgumentParser(description="Transform a CSV file with data to CLIPS code for instance creation")
parser.add_argument('--file', metavar='Files', nargs='+', help="files to be processed")
args = parser.parse_args()

current_path = os.getcwd() + os.sep

file_list = args['file']

for file in file_list:
    info_to_print = ''
    with open(current_path+file, newline='') as csvfile:
        instance_reader = csv.reader(csvfile)
        slots = instance_reader.__next__()
        info_to_print += '(definstances ' + file[:-4] + '\n'
        for instance in instance_reader:
            info_to_print += format_instance(instance, slots)
        info_to_print += ')'
    with open(file[:-4] + '.clp', 'w') as output_:
        print(info_to_print, file=output_)



