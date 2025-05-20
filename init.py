from os import makedirs

from argparse import ArgumentParser

def init_readme(directory):
    filename = f"{ directory }/README.md"
    with open(filename,"w") as fp:
        fp.writelines(f"## {directory}")

def init_script(directory):
    filename = f"{ directory }/script.py"
    with open(filename,"w") as fp:
        fp.writelines("#!/usr/bin/env python")

if __name__ == "__main__":

    parser = ArgumentParser(
                prog='init',
                description='creating script boilerplate',
                epilog='good luck')

    parser.add_argument('group', nargs='?') 
    parser.add_argument('problem', nargs='?') 
    args = parser.parse_args()
    if not args.group:
        group = input("Write group of tasks name: ")
    else:
        group = args.group
    if not args.problem:
        directory = input("Write problem name: ")
    else:
        directory = args.directory
    directory = f"./{ group }/{ directory }"
    makedirs(directory, exist_ok=True)

    init_readme(directory)
    init_script(directory)
