#!/usr/bin/python3

# This file is part of Project Babel.
# Copyright 2021 Graham Shaw
# Redistribution and modification are permitted within the terms of the
# BSD-3-Clause licence as defined by v3.4 of the SPDX Licence List.

import os
import re
import json

def to_pathname(textid):
    pathname = 'raw/'
    if textid >= 10000:
        pathname += '%d/' % (textid // 10000)
    if textid >= 1000:
        pathname += '%d/' % ((textid // 1000) % 10)
    if textid >= 100:
        pathname += '%d/' % ((textid // 100) % 10)
    pathname += '%d/' % ((textid // 10) % 10)
    pathname += '%d/' % textid
    pathname += '%d-h/' % textid
    pathname += '%d-h.htm' % textid
    return pathname

files = {}
for root, dirnames, filenames in os.walk('raw'):
    for filename in filenames:
        m = re.match('([0-9]+)-h.html?', filename)
        if m:
            textid = int(m.group(1))
            pathname = os.path.join(root, filename)
            if pathname == to_pathname(textid):
                files[textid] = pathname

print(json.dumps(files))
