# -*- coding: utf-8 -*-

import re
import os
import headerfile as hf
import string_util as sutil
import function_util as futil


def add_doxy_comment(filepath):
    f = open(filepath, "r")
    header_code = f.read()

    for cobj in __generate_comment_objs(filepath, header_code):
        if hf.has_doxy_comment(cobj, header_code):
            old_doxy_comment = hf.extract_doxy_comment(cobj, header_code)

            if __need_to_change(cobj, old_doxy_comment):
                header_code = __insert_comment(cobj, header_code)
            else:
                continue
        else:
            header_code = __insert_comment(cobj, header_code)

    return header_code


def __generate_comment_objs(filepath, header_code):
    comment_objs = []

    comment_objs.append(__generate_file_doxy_comment(filepath))
    [
        comment_objs.append(__generate_class_doxy_comment(i))
        for i in hf.extract_classes(header_code)
    ]
    [
        comment_objs.append(__generate_enum_doxy_comment(i))
        for i in hf.extract_enums(header_code)
    ]
    [
        comment_objs.append(__generate_struct_doxy_comment(i))
        for i in hf.extract_structures(header_code)
    ]
    [
        comment_objs.append(__generate_member_var_doxy_comment(i))
        for i in hf.extract_member_vars(header_code)
    ]
    [
        comment_objs.append(__generate_function_doxy_comment(i))
        for i in hf.extract_functions(header_code)
    ]

    # add doxygen comment from end to start, because not to change line number.
    comment_objs.sort(key=lambda x: x["start"], reverse=True)

    return comment_objs


def __insert_comment(comment, data):
    start = comment["start"]
    before = sutil.before_line(start, data)

    if start == 0:
        return sutil.insert(start, data, comment["comment"])
    elif before[-1] == "{" or before[-1] == ":":
        return sutil.insert(start, data, comment["comment"])
    else:
        return sutil.insert(start, data, "\n" + comment["comment"])


def __generate_file_doxy_comment(filepath):
    base = os.path.basename(filepath)
    d = ""
    d += "/**\n"
    d += " * @file " + base + "\n"
    d += " *\n"
    d += " * @brief @todo\n"
    d += " */\n"
    return {"type": "file", "start": 0, "comment": d, "data": filepath}


def __generate_class_doxy_comment(match):
    data = match.group()
    indent = futil.extract_indent(data)
    m = re.search(r"(class\s+)(\w+)", data)
    name = m.groups()[1]

    d = ""
    d += indent + "/**\n"
    d += indent + " * @brief " + name + "は@todoのクラス。\n"
    d += indent + " *\n"
    d += indent + " * @todo\n"
    d += indent + " */\n"
    return {"type": "class", "start": match.start(), "comment": d, "data": data}


def __generate_struct_doxy_comment(match):
    data = match.group()
    indent = futil.extract_indent(data)
    m = re.search(r"(struct\s+)(\w+)", data)
    name = m.groups()[1]

    d = ""
    d += indent + "/**\n"
    d += indent + " * @brief " + name + "は@todoの構造体。\n"
    d += indent + " *\n"
    d += indent + " * @todo\n"
    d += indent + " */\n"
    return {"type": "struct", "start": match.start(), "comment": d, "data": data}


def __generate_enum_doxy_comment(match):
    data = match.group()
    indent = futil.extract_indent(data)
    m = re.search(r"(enum\s+)(\w+)", data)
    name = m.groups()[1]
    d = ""
    d += indent + "/**\n"
    d += indent + " * @brief " + name + "は@todoを示す列挙型。\n"
    d += indent + " *\n"
    d += indent + " * @todo\n"
    d += indent + " */\n"
    return {"type": "enum", "start": match.start(), "comment": d, "data": data}


def __generate_function_doxy_comment(match):
    data = match.group()
    comment = ""

    if futil.is_constructor(data):
        comment = __generate_constructor_doxy_comment(data)
    elif futil.is_destructor(data):
        comment = __generate_destructor_doxy_comment(data)
    elif futil.is_getter(data):
        comment = __generate_getter_doxy_comment(data)
    elif futil.is_setter(data):
        comment = __generate_setter_doxy_comment(data)
    else:
        comment = __generate_other_function_doxy_comment(data)

    return {
        "type": "function",
        "start": match.start(),
        "comment": comment,
        "data": data,
    }


def __generate_member_var_doxy_comment(match):
    d = ""
    data = match.group()
    indent = futil.extract_indent(data)
    d += indent + "/// @todo\n"
    return {"type": "member_var", "start": match.start(), "comment": d, "data": data}


def __need_to_change(new_doxy_comment_obj, old_doxy_comment):
    new_doxy_args = futil.extract_arg_vars(new_doxy_comment_obj["data"])
    for arg in new_doxy_args:
        arg_key = "\\a " + arg
        if arg_key not in old_doxy_comment:
            return True
    return False


def __generate_constructor_doxy_comment(data):
    indent = futil.extract_indent(data)

    args = futil.extract_arg_vars(data)
    args_detail = "@todo"
    args_detail += " ".join([" \\a " + i for i in args])

    c = ""
    c += indent + "/**\n"
    c += indent + " * @brief コンストラクタ\n"
    c += indent + " *\n"
    c += indent + " * " + args_detail + "\n"
    c += indent + " */\n"
    return c


def __generate_destructor_doxy_comment(data):
    indent = futil.extract_indent(data)

    args = futil.extract_arg_vars(data)
    args_detail = "@todo"
    args_detail += " ".join([" \\a " + i for i in args])

    c = ""
    c += indent + "/**\n"
    c += indent + " * @brief デストラクタ\n"
    c += indent + " *\n"
    c += indent + " * " + args_detail + "\n"
    c += indent + " */\n"
    return c


def __generate_getter_doxy_comment(data):
    indent = futil.extract_indent(data)

    gm = re.search(r"(get)(\w+)", data)
    upper_member = gm.groups()[1]
    lower_member = sutil.to_lower_camel(upper_member)
    setter_name = "set" + upper_member + "()"

    c = ""
    c += indent + "/**\n"
    c += indent + " * @brief " + lower_member + "のgetter\n"
    c += indent + " *\n"
    c += indent + " * \\a " + lower_member + "を取得する。\n"
    c += indent + " * \\sa " + setter_name + "\n"
    c += indent + " */\n"
    return c


def __generate_setter_doxy_comment(data):
    indent = futil.extract_indent(data)

    sm = re.search(r"(set)(\w+)", data)
    upper_member = sm.groups()[1]
    lower_member = sutil.to_lower_camel(upper_member)
    getter_name = "get" + upper_member + "()"

    c = ""
    c += indent + "/**\n"
    c += indent + " * @brief " + lower_member + "のsetter\n"
    c += indent + " *\n"
    c += indent + " * \\a " + lower_member + "を設定する。\n"
    c += indent + " * \\sa " + getter_name + "\n"
    c += indent + " */\n"
    return c


def __generate_other_function_doxy_comment(data):
    indent = futil.extract_indent(data)

    args = futil.extract_arg_vars(data)
    args_detail = "@todo"
    args_detail += " ".join([" \\a " + i for i in args])

    c = ""
    c += indent + "/**\n"
    c += indent + " * @brief @todo\n"
    c += indent + " *\n"
    c += indent + " * " + args_detail + "\n"
    c += indent + " */\n"
    return c


# add_doxy_comment("testdata/function.h")

# # print(__to_upper_camel('aaaaa'))
# # print(__to_upper_camel('Aaaaa'))
# # print(__to_lower_camel('aaaaa'))
# # print(__to_lower_camel('Aaaaa'))
