"""def open_and_print_contents_of_file(file):
    try:
        file = open(file, "r")  # "r" means it will read the file but not overwrite it
        list_of_order_items = file.readlines()

        # print (list_of_order_items

        for line in list_of_order_items:
            print(line.rstrip("\n"))

        file.close()

    except FileNotFoundError:
        print("This path does not print to a file")
    finally:
        print("\nConnection to file closed and execution has finished")

open_and_print_contents_of_file("order.txt") """

def open_and_print_contents_of_file(file):
    try:
        with open(file, "r") as file:       # prepares the file for communication
            list_of_order_items = file.readlines()

        # print (list_of_order_items

        for line in list_of_order_items:
            print(line.rstrip("\n"))

    except FileNotFoundError:
        print("This path does not print to a file")
    finally:
        print("\nConnection to file closed and execution has finished")

open_and_print_contents_of_file("")