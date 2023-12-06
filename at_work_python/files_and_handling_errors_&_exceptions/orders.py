try:
    file = open("order.txt")
except FileNotFoundError as error_msg:
    print("There path does not point to a file")
    print(error_msg)
    raise
except:
    print("There has been a different type of error! PANIC!")

