#!/usr/bin/python3

import re
from libretranslatepy import LibreTranslateAPI
from html import escape

lt = LibreTranslateAPI("http://127.0.0.1:5000")

result_pattern = r"\<description\>(.*)\<\/description\>"
pattern = re.compile (result_pattern)

with open("juice.xml", "rt") as file_read:
    with open("juice_out.xml", "wt") as file_write:
        for line in file_read:
            res = re.search(pattern, line)
            if res is not None:
                new_string = escape(lt.translate(res.groups(0)[0], "en", "pt"))
                old_string = res.string.split(">")[1].split("<")[0]
                print("old:" + old_string)
                print("new:" + new_string)
                subs = line.replace(old_string, new_string)
                file_write.write(subs.strip())
                print("result:" + subs)
            else:
                file_write.write(line)
