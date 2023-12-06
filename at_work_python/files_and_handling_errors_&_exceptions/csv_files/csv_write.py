import csv
from write_to_csv import transform_user_details
"""
def write_to_csv(csvfile):

    with open('user_details.csv', 'r') as csvfile:
        original = csvfile.read()
    with open('new_user_data.csv', 'a') as csvfile2:
        csvfile2.write('\n')
        csvfile2.write(original)
"""

def create_new_user_data_csv(old_user_data, new_file_name):

    new_user_data = transform_user_details(old_user_data)

    try:
        with open(new_file_name, 'w', newline='') as new_file_name:
            csv_writer = csv.writer(new_file_name)
            csv_writer.writerow(new_user_data)

    except FileNotFoundError:
        print("The file has not been found")

create_new_user_data_csv("user_details.csv", "new_user_data2")
