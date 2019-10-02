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




