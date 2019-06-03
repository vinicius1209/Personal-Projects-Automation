import argparse
import sys
import os
import subprocess
from aFlask import FlaskProject
from aVue import VueProject
from aVenv import VenvProject
from aGitHub import GitRepo

path = "C:/Users/Vinícius Machado/Documents/GitHub/"

def create():   

    parser = argparse.ArgumentParser(description='Personal Projects Automation.')
    parser.add_argument('-p', metavar='Project Name', required=True, dest='proj_name', help='Define the Project Name')
    parser.add_argument('-g', metavar='GitHub', dest='github', action='store_const', const='', help='Create GitHub Repository')

    args = vars(parser.parse_args())
    
    requires = []
    proj_name = args['proj_name']
    isGit = args['github']

    full_path = path + proj_name

    print('\n***********************************\n')
    print('Project/Folder Name: {}'.format(proj_name))

    # Check if path + folder exists
    while check_path(full_path):
        new = input('Folder alredy exists:\n-> <new_name> or -x to exit: ')
        if new.upper() == '-X':
            sys.exit()
        full_path = path + new

    print("\n----------ROOT FOLDER---------\n")
    os.makedirs(full_path)
    print('Folder created!')

    print("\n------------FLASK-------------\n")
    FlaskProject(full_path)
    requires.append('FLASK')

    print("\n-------------VUE--------------\n")
    VueProject(full_path)
    requires.append('VUE')

    if isGit is not None:
        print("\n-----------GitHub-------------\n")
        GitRepo(proj_name)

    print("\n------------Venv--------------\n")
    VenvProject(proj_name, full_path, requires)
    
    print('\n***********************************\n')

    # Open VSC
    os.chdir(full_path)
    subprocess.Popen('code .', shell=True)


# Check if path alredy exists
def check_path(path):
    return os.path.isdir(path)


if __name__ == "__main__":
    create()

