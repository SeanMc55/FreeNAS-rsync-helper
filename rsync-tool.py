import os

os.system("clear")
initial_dir = "/mnt/"

quick_list = [\
    "",\
    "",\
    "",\
    ""\
        ]

def get_copy_dir(initial_dir):
    copy_dir = [initial_dir]
    found = False
    while found == False:
        new_dir = ''
        dirs = os.listdir()

        dirs = sorted(dirs)
        index = 1
        for i in dirs:
            print("{} {}".format(index, i))
            index += 1
        
        print('')
        dir_selection = input("What directory to select: ")
        if dir_selection == 'done':
            found = True
            break
        selection = int(dir_selection)-1
        next_lvl = dirs[selection]
        copy_dir.append(next_lvl)
        copy_dir.append("/")

        for entry in copy_dir:
            new_dir = new_dir + entry
        
        os.system("clear")
        print("Current Directory: "+new_dir)
        print('')
        os.chdir(new_dir)

    os.system("clear")
    print('')
    print("Send")
    print(" 1) the directory (without /)")
    print(" 2) the files (with /)")
    choice = input(": ")
    if choice == "1":
        copy_dir = copy_dir[:-1]
        for entry in copy_dir:
            new_dir = new_dir + entry
        return new_dir
    if choice == "2":
        for entry in copy_dir:
            new_dir = new_dir + entry
        return new_dir
    
def get_paste_dir(initial_dir):
    paste_dir = [initial_dir]
    found = False
    while found == False:
        new_dir = ''
        dirs = os.listdir()

        dirs = sorted(dirs)
        index = 1
        for i in dirs:
            print("{} {}".format(index, i))
            index += 1
        
        print('')
        dir_selection = input("What directory to select: ")
        if dir_selection == 'done':
            found = True
            break
        selection = int(dir_selection)-1
        next_lvl = dirs[selection]
        paste_dir.append(next_lvl)
        paste_dir.append("/")

        for entry in paste_dir:
            new_dir = new_dir + entry
        
        os.system("clear")
        print("Current Directory: "+new_dir)
        print('')
        os.chdir(new_dir)

    for entry in paste_dir:
        new_dir = new_dir + entry
    return new_dir

# get the directories to copy from
os.chdir(initial_dir)
copydir = '"'+get_copy_dir(initial_dir)+'"'

os.system("clear")

#pick from quick list or choose directory
choice = input("Do you want to use a quick destination? (y/n): ")
if choice == 'y':
    index = 1
    for i in quick_list:
        print("{} {}".format(index, i))
        index += 1
    print('')
    selection = input("Which quick destination would you like to use?: ")
    selection = int(selection)-1
    pastedir = quick_list[selection]
    pastedir = '"'+pastedir+'"'
else:
    # get the directories to copy to
    os.chdir(initial_dir)
    pastedir = '"'+get_paste_dir(initial_dir)+'"'

os.system("clear")
print("Do you want to")
print("1) copy")
print("2) move")
print("3) rsync")
choice = input (": ")

# go through the choices
if choice == '1':
    print('')
    print("Send")
    print(" 1) the directory")
    print(" 2) the files")
    choice2 = input(": ")
    if choice2 == "1":
        command = "cp -Rvp "+copydir+' '+pastedir
    if choice2 == "2":
        pastedir = pastedir[:-2]
        command = "cp -Rvp "+copydir+'* '+pastedir+'"'

if choice == '2':
    print('')
    print("Send")
    print(" 1) the directory")
    print(" 2) the files")
    choice2 = input(": ")
    if choice2 == "1":
        command = "mv -rvn "+copydir+' '+pastedir
    if choice2 == "2":
        pastedir = pastedir[:-2]
        command = "mv -rvn " + copydir + '* ' + pastedir + '"'

if choice == '3':
    # command = "rsync -rvA --progress "+copydir+' '+pastedir
    command = "rsync -rvpEt --progress "+copydir+' '+pastedir

os.system("clear")
print(command)
print('')
os.system(command)

exit()