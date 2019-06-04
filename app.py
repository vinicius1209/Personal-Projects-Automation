import argparse
from automation import ProjectAutomation

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Personal Projects Automation.')
    parser.add_argument('-p', metavar='Project Name', required=True, dest='proj_name', help='Define the Project Name')
    parser.add_argument('-f', metavar='Flask', dest='flask', action='store_const', const='', help='Create Flask Structure')
    parser.add_argument('-v', metavar='Vue', dest='vue', action='store_const', const='', help='Add Vue to Flask Structure')
    parser.add_argument('-g', metavar='GitHub', dest='github', action='store_const', const='', help='Create GitHub Repository')

    args = vars(parser.parse_args())

    ProjectAutomation(args)
