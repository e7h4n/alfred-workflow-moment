#!/usr/bin/python
# encoding: utf-8

import arrow
from dateutil import tz
import time
import moment_format
from ast import parse as parseAST
from ast import ASTSyntaxError

def add_item(wf, title, desc):
    wf.add_item(title, arg = title, subtitle = desc, valid = True)

def process(wf, args):
    log = wf.logger

    try:
        ast = parseAST(args)
    except ASTSyntaxError as e:
        log.debug('opps')
        wf.send_feedback()
        return

    target_time = arrow.now()

    presetFormat = None

    for func in ast:
        funcName = func[0]
        args = []
        if len(func) > 1:
            args = func[1:]

        if funcName == 'reset':
            if len(args) > 0:
                try:
                    target_time = arrow.get(args[0]).to('local')
                except ValueError:
                    target_time = arrow.get(args[0] / 1000).to('local')
            else:
                target_time = arrow.now()
            continue

        if funcName == 'set':
            params = {}
            if args[0] == 'timezone':
                timezone = str(abs(int(args[1]))) + ':00'
                if abs(args[1]) < 10:
                    timezone = '0' + timezone

                if args[1] < 0:
                    timezone = '-' + timezone
                else:
                    timezone = '+' + timezone

                log.debug(timezone)
                target_time = target_time.to(timezone)

            else:
                params[args[0]] = int(args[1])
                target_time = target_time.replace(**params)
            continue

        if funcName == 'shift':
            params = {}
            params[args[1] + 's'] = int(args[0])
            target_time = target_time.replace(**params)
            continue

        if funcName == 'start_of':
            target_time = target_time.floor(args[0])
            continue

        if funcName == 'end_of':
            target_time = target_time.ceil(args[0])
            continue

        if funcName == 'format' and len(args) > 0:
            presetFormat = ' '.join(args)

    if presetFormat is not None:
        add_item(wf, target_time.format(presetFormat), presetFormat)
    else:
        # Add an item to Alfred feedback
        timestamp = str(int(time.mktime(target_time.datetime.timetuple()) * 1e3 + target_time.datetime.microsecond / 1e3))
        wf.add_item(timestamp, subtitle = u'Timestamp, ' + target_time.humanize(), arg = timestamp, valid = True)

        formats = moment_format.load_format(wf)
        if len(formats) == 0:
            add_item(wf, target_time.format('YYYY-MM-DD HH:mm:ss ZZ'), 'Standard format, you can use "format-moment" to add your format.')
        else:
            for formatStr in formats:
                value = target_time.format(formatStr)
                wf.add_item(value, subtitle = 'Saved format: "' + formatStr + '"', arg = value, valid = True)

    # Send output to Alfred
    wf.send_feedback()
