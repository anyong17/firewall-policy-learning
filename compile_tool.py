#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import py_compile

if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] == "-h":
        usage = "Usage:" + sys.argv[0] + " python_file"
        print usage
        sys.exit()

    py_file = sys.argv[1]
    py_compile.compile(py_file)
