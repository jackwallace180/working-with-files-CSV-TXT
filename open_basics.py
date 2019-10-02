# here we will define our oepn/close functions

def open_read_file(file):

    try:
        openedfile = open(file, 'r')
        file_lines_list = openedfile.readlines()
        # print(file_lines_list)

        for line in file_lines_list:
            print(line.rstrip('\n'))
        openedfile.close()  # this closes your file otherwise file is locked and cant be changed


    except FileNotFoundError as errmsg:
        print('dont worry file was not found but thats ok atleast you tried :)') #prints string when error occurs
        print(errmsg) #prints error message from FileNotFoundError
        raise    #prints actual error

def open_read_file_using_with(file):

    try:
        with open(file, 'r') as open_read_file:
            for line in open_read_file.readlines():
                print(line.rstrip('\n'))
    except FileNotFoundError as errmsg:
        print('file cannot be found :(')
    finally:
            print('\n Execution completed')

def write_to_file(file, order_item):
    try:
        with open(file, 'a') as opened_file:
            opened_file.write('\n' + order_item)

    except FileNotFoundError:
        print('File not found oh dear')




