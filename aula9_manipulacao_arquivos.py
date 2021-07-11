
def file_write(text,file_name='file', ext='txt'):
    try:
        file_name = file_name + '.' + ext
        file = open(file_name,'r');
        content = file.read()
        print('Use the option "2. Update File"')

    except:
        if (file_name[-3].isalnum()) and (ext[-3:].isalnum()):
            file = open(file_name, 'w')
            file.write(text + '\n')
            file.close()
            print('File \"{}\" created!'.format(file.name))

def file_update(text,file_name='file'):
    try:
        # isalnum (verify if exist caracters alfanumerics
        if (file_name.isalnum()):

            test = open(file_name[0:-3] + '.' + file_name[-3:], 'r')
            if test != '':
                test = open(file_name[0:-3] + '.' + file_name[-3:], 'a')
                test.write(text + '\n')
                test.close()
                print('File updated \"{}\"'.format(test.name))
            else:
                print('File doesnt exist!')
        else:
            print('File didn\'t create. \nName violation!')
    except:
        print('File not found')

def read_file(file_name):
    try:
        test= open(file_name,'r')
        content = test.read()
        test.close()
        print(content)
    except:
        print('File not found!')

def calc_average(file_name):
    try:
        file = open(file_name,'r')
        content = file.read().split('\n')
        file.close()
        school_md = []
        for x in content:
            if len(x) > 0:
                school_grades = x.split(',')
                student = school_grades[0] # log student
                school_grades.pop(0) # exclude student
                # function lambda to compute mean
                avg = lambda  school_grades : sum([int(i) for i in school_grades])/(len(school_grades)-1)
                # creates dictionary with name and average of each student
                school_md.append({student:round(avg(school_grades),2)})


        return school_md
    except:
        return 'Error (File not found or File is bad formatted)'

def move_file(file_name,new_place):
    import shutil
    try:
        shutil.move(file_name,new_place)
        print('File moved')
    except:
        print('Error - Place not found, File not found..')

def copy_file(file_name,new_place):
    import shutil
    try:
        shutil.copy(file_name, new_place)
        print('File copied')
    except:
        print('Error - Place not found, File not found..')

if __name__ == '__main__':
    option= 0
    equals = 50
    print('\n')
    while option != 'e':
        print('='* equals + 'MENU' + '='* equals)
        print('1. Create File')
        print('2. Update File')
        print('3. Read File')
        print('4. Average - It is need a file with names and numbers..')
        print('5. Move File')
        print('6. Copy File')
        print('e. Exit Program')
        print('='* equals + 'END' + '='* equals)
        option = input('Choose option: ')
        if (option == '1'):
            file_name = input('File name to create: ')
            ext_name = input('Extension file: ')
            text = input('Add text to initial: ')
            file_write(text,file_name,ext_name)
        elif (option == '2'):
            print('Note the file name has to inform with extension without point')
            file_name = input('File name to update: ')
            text = input('Add text the file: ')
            file_update(text,file_name)
        elif (option == '3'):
            file_name = input('File name to read: ')
            read_file(file_name)
        elif (option == '4'):
            file_name = input('File name to average: ')
            print(calc_average(file_name))
        elif (option == '5'):
            file_name = input('File to move: ')
            new_place = input('Way new file: ')
            move_file(file_name,new_place)
        elif (option == '6'):
            file_name = input('File to copy: ')
            new_place = input('Way copy: ')
            copy_file(file_name, new_place)
        elif option != 'e':
            print('Invalid option!')
        else:
            option = 'e'
    else:
        print('You exited the program!')


