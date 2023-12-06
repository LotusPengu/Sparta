def write_to_file(file, order_item):
    try:
        with open(file, "a") as file:       # Append adds a new line, rather than replacing the text completely
            file.write(order_item + "\n")
    except FileNotFoundError:
        print("File cannot be found, please check path")