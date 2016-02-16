#!/usr/bin/python
# encoding: utf-8

import sys

from workflow import Workflow

log = None

def main(wf):
    import parser
    args = wf.args

    parser.process(wf, args)

if __name__ == '__main__':
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
