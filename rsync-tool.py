import os

os.system("clear")
initial_dir = "/mnt/"
# initial_dir = "/Volumes/Data/"

# find first dir to copy from
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

    copy_dir = copy_dir[:-1]
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

os.chdir(initial_dir)
copydir = '"'+get_copy_dir(initial_dir)+'"'
os.chdir(initial_dir)
pastedir = '"'+get_paste_dir(initial_dir)+'"'
os.chdir(initial_dir)

os.system("clear")

command = "rsync -rv --progress "+copydir+' '+pastedir
print(command)
os.system(command)

exit()