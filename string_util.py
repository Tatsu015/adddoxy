# -*- coding: utf-8 -*-


def insert(pos, s, x):
    return x.join([s[:pos], s[pos:]])


def to_upper_camel(s):
    if len(s) == 0:
        return s
    if len(s) == 1:
        return s.upper()

    return s[0].upper() + s[1:]


def to_lower_camel(s):
    if len(s) == 0:
        return s
    if len(s) == 1:
        return s.lower()

    return s[0].lower() + s[1:]


def before_line(pos, data):
    return before_line_obj(pos, data)["data"]


def before_line_obj(pos, data):
    end = data.rfind("\n", 0, pos)
    if end == -1:
        return {"start": 0, "end": 0, "data": ""}

    start = data.rfind("\n", 0, end)
    if start == -1:
        return {"start": 0, "end": end, "data": data[:end]}

    return {"start": start, "end": end, "data": data[start:end]}
