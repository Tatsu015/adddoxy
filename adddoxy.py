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
    parser.add_argument(
        "--export", help="Export doxygen comment csv list", action="store_true"
    )
    args = parser.parse_args()

    buf = ""
    for path in file_paths("testdata/org"):
        buf += generator.export_doxy_comment(path)
    f = open("result.csv", "w")
    f.write(buf)
    exit(0)

    for path in file_paths(args.target):
        if args.export:
            generator.export_doxy_comment(path)
            continue

        c = generator.add_doxy_comment(path)
        if args.dry:
            print("<<<<< " + path + " >>>>>")
            print(c)
        else:
            f = open(path, "w")
            f.write(c)


if __name__ == "__main__":
    main()
