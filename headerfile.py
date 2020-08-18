# -*- coding: utf-8 -*-

import re
import os
import string_util as sutil


def extract_classes(header_code):
    r = re.compile(r"(?=.*class)(?!.*;).*")
    classes = re.finditer(r, header_code)
    return classes


def extract_structures(header_code):
    r = re.compile(r"(?=.*struct).*")
    classes = re.finditer(r, header_code)
    return classes


def extract_enums(header_code):
    r = re.compile(r"\senum\s\w+")
    enums = re.finditer(r, header_code)
    return enums


def extract_functions(header_code):
    r = re.compile(r".*\(.*\).*;")
    functions = re.finditer(r, header_code)
    return functions


def extract_member_vars(header_code):
    r = re.compile(r".*_;")
    functions = re.finditer(r, header_code)
    return functions


def has_doxy_comment(target, header_code):
    if len(header_code) < 14:
        return False

    if target["type"] == "file":
        if header_code[:13] == "/**\n * @file ":
            return True
        else:
            return False

    if target["type"] == "member_var":
        before = sutil.before_line(target["start"], header_code)
        if "///" in before:
            return True
        else:
            return False

    s = target["start"] - 1
    if header_code[s - 3 : s + 1] == " */\n":
        return True
    else:
        return False

    return False


def extract_doxy_comment_obj(target, header_code):
    file_head_comment = "/**\n * @file "
    if len(header_code) < len(file_head_comment):
        return {"type": "file", "start": 0, "end": 0, "comment": ""}

    if target["type"] == "file":
        if header_code[:13] == file_head_comment:
            end_key = " */"
            end = header_code.find(end_key) + len(end_key)
            return {
                "type": "file",
                "start": 0,
                "end": end,
                "comment": header_code[0:end],
            }

    if target["type"] == "member_var":
        before = sutil.before_line_obj(target["start"], header_code)
        if "///" in before["data"]:
            return {
                "type": "member_var",
                "start": before["start"],
                "end": before["end"],
                "comment": before["data"].replace("/// ", ""),
            }

    end = target["start"] - 1
    if header_code[end - 3 : end + 1] == " */\n":
        start = header_code.rfind("/**\n", 0, end)
        return {
            "type": "function",
            "start": start,
            "end": end,
            "comment": header_code[start:end],
        }

    return None


def extract_doxy_brief(target):
    if target["type"] == "member_var":
        buf = target["comment"].replace("///", "").strip()
        return buf

    r = re.compile(r"\s@brief.*")
    brief = re.search(r, target["comment"])
    if brief:
        s = brief.group().replace("@brief", "").strip()
        return s
    return ""


def extract_doxy_brief_detail(target):
    ls = target["comment"].split("\n")
    buf = ""
    if len(ls) > 3:
        for l in ls[3:-2]:
            l = l.strip()[2:]
            buf += l.strip() + "\\n"
    return buf


# print(before_line(5, 'aaaaa\nbbb'))
# print(before_line(6, 'aaaaa\nbbb'))
# print(before_line(7, 'aaaaa\nbbb'))

# d = '/**\n * @file function.h\n *\n * @brief @todo\n */\n#ifndef GTGFUNCTION_H'
# c = extract_doxy_comment_obj({'start':0, 'type':'file'},d)
# d = '/**\n * @brief Struct1は@todoの構造体\n *\n * @todo\n */\nstruct Struct1{\n  /// @todo\n  int header_code_;\n};'
# c = extract_doxy_comment_obj({'start':0, 'type':'struct'},d)

# d = 'private:\n  /// @todo\n  QString name_;'
# c = extract_doxy_comment_obj({'start':25, 'type':'member_var'},d)

# d = '  /**\n   * @brief @todo\n   *\n   * @todo \a a  \a b\n   */\n  int func(int a, int b);'
# c = extract_doxy_comment_obj({'start':55, 'type':'function'},d)

# print(c)
