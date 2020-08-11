# -*- coding: utf-8 -*-

import os
import glob
import generator
import argparse


def file_paths(path):
    if os.path.isfile(path):
        return [path]

    paths = glob.glob(path + "/**.h", recursive=True)
    return paths


def main():
    parser = argparse.ArgumentParser(
        description="Automatically add C++ doxygen comment headers to class, struct, enum, function and member variable."
    )
    parser.add_argument("target", help="target directory or file path")
    parser.add_argument("--dry", help="Dry run adddoxy command", action="store_true")
    args = parser.parse_args()

    for path in file_paths(args.target):
        c = generator.add_doxy_comment(path)
        if args.dry:
            print("<<<<< " + path + " >>>>>")
            # print(c)
        else:
            f = open(path, "w")
            f.write(c)


if __name__ == "__main__":
    main()
