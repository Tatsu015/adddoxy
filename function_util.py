# -*- coding: utf-8 -*-

import re


def is_constructor(func_str):
    tmp = func_str.strip()
    tmp = tmp.split("(")[0]
    tmps = tmp.split(" ")

    if tmps[0] == "explicit":
        return True
    if len(tmps) == 1:
        name = tmps[0]
        # remove destructor pattern
        if not is_destructor(name):
            return True
    return False


def is_destructor(func_str):
    tmp = func_str.strip()
    if tmp[0] == "~":
        return True
    else:
        return False


def is_setter(func_str):
    tmp = func_str.split("(")[0]
    if re.search(r"set\w+", tmp):
        return True
    else:
        return False


def is_getter(func_str):
    tmp = func_str.split("(")[0]
    if re.search(r"get\w+", tmp):
        # remove singletone getInstace function.
        if 'getinstance' in tmp.lower():
            return False
        return True
    else:
        return False


def extract_arg_vars(func_str):
    if "(" not in func_str:
        return []
    if ")" not in func_str:
        return []

    tmp = func_str.split("(")[1].split(")")[0]
    args = tmp.split(",")

    arg_vars = []
    for arg in args:
        var = arg.split(" ")[-1]
        if var == "":
            continue
        else:
            arg_vars.append(var)
    return arg_vars


def extract_indent(func_str):
    indent = ""
    for s in func_str:
        if s != " ":
            return indent
        else:
            indent += " "
    return indent
