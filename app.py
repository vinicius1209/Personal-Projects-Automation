import sys
import os
import subprocess
from aFlask import FlaskProject
from aVue import VueProject
from aVenv import VenvProject
from aGitHub import GitRepo

path = "C:/Users/55479/Documents/GitHub/"

def create():   
    
    requires = []
    
    """
        <name> = project name
        <flask> = create flask tree
        <vue> = create stuffs for vue
    """
    arg_names = ['file', 'name', 'flask', 'vue']
    args_input = dict(zip(arg_names, sys.argv))
    folderName = args_input['name']

    full_path = path + folderName

    print('\n***********************************\n')
    print('Project/Folder Name: {}'.format(folderName))

    # Check if path + folder exists
    while check_path(full_path):
        new_folderName = input('Folder alredy exists:\n-> <new_name> or -x to exit: ')
        if new_folderName.upper() == '-X':
            sys.exit()
        full_path = path + new_folderName

    print("\n----------ROOT FOLDER---------\n")
    os.makedirs(full_path)
    print('Folder created!')

    if 'flask' in args_input:
        print("\n------------FLASK-------------\n")
        if args_input['flask'].upper() == 'FLASK':
            FlaskProject(full_path)
            requires.append('FLASK')

    if 'vue' in args_input:
        print("\n-------------VUE--------------\n")
        if args_input['vue'].upper() == 'VUE':
            VueProject(full_path)
            requires.append('VUE')

    print("\n-----------GitHub-------------\n")
    GitRepo(folderName)

    print("\n------------Venv--------------\n")
    VenvProject(folderName, full_path, requires)

    print('Well Done, Success!')
    print('\n***********************************\n')

    # Open VSC
    os.chdir(full_path)
    subprocess.Popen('code .', shell=True)


# Check if path alredy exists
def check_path(path):
    return os.path.isdir(path)


if __name__ == "__main__":
    create()

