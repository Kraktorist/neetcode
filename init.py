from os import mkdir, getenv

from argparse import ArgumentParser

def init_readme(directory):
    filename = f"{ directory }/README.md"
    with open(filename,"w") as fp:
        fp.writelines("## ")

def init_script(directory):
    filename = f"{ directory }/script.py"
    with open(filename,"w") as fp:
        fp.writelines("#!/usr/bin/env python")

if __name__ == "__main__":

    parser = ArgumentParser(
                prog='init',
                description='creating script boilerplate',
                epilog='good luck')

    parser.add_argument('directory', nargs='?', default=getenv('QUESTION')) 
    args = parser.parse_args()
    print(args)
    if not args.directory:
        directory = input("Write directory name: ")
    else:
        directory = args.directory
    directory = f"./{ args.directory }"
    print(directory)
    mkdir(directory)

    init_readme(directory)
    init_script(directory)
