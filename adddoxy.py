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
    parse = argparse.ArgumentParser(
        description="Automatically add C++ doxygen comment headers to class, struct, enum, function and member variable."
    )
    parse.add_argument("target", help="target directory or file path")
    args = parse.parse_args()

    for path in file_paths(args.target):
        c = generator.add_doxy_comment(path)
        f = open(path, "w")
        f.write(c)


if __name__ == "__main__":
    main()
