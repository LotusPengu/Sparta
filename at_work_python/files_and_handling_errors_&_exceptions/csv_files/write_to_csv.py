import csv

def transform_user_details(csvfile):
    new_user_data = []

    try:
        with (open(csvfile, newline = '') as csvfile):
            csvreader = csv.reader(csvfile, delimiter=',')

            for user in csvreader:
                temp_list = []
                temp_list.append(user[1])
                temp_list.append(user[2])
                temp_list.append(user[4])
                new_user_data.append(temp_list)

    except:
        print("An exception has occurred")

    return new_user_data