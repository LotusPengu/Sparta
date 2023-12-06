import csv

"""
def read_csv(csvfile):
    try:
        with open(csvfile, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')

        # print(csvreader)

            iterable_csv = iter(csvreader)      # Allows us to iterate on the object directly
            next(iterable_csv)

            for row in csvreader:
                print(row)
                # print(line[-1])         # reading in just the last column

    except:
        print("An exception has occurred")

read_csv("user_details.csv") """

def read_csv(csvfile):
    try:
        with open(csvfile, newline = '') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')

            list_csv_data = list(csvreader)
            print(list_csv_data)
            print(type(list_csv_data))

    except:
        print("An exception has occurred")

read_csv("user_details.csv")

