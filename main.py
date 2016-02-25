#!/usr/bin/python
# encoding: utf-8

import sys

from workflow import Workflow

log = None

def main(wf):
    import parser
    import moment_format
    args = wf.args
    if len(args) == 0:
        return

    action = args[0]

    if action == 'parse':
        parser.process(wf, args[1:])
    elif action == 'format':
        moment_format.process(wf, args[1:])
    elif action == 'addFormat':
        moment_format.add_format(wf, args[1:])
    elif action == 'delFormat':
        moment_format.del_format(wf, args[1:])

if __name__ == '__main__':
    wf = Workflow()
    wf.data_serializer = 'json'
    log = wf.logger
    sys.exit(wf.run(main))
