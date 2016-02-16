import arrow
from dateutil import tz
import time
from ast import parse as parseAST
from ast import ASTSyntaxError

def add_item(wf, title, desc):
    wf.add_item(title, arg = title, valid = True)

def process(wf, args):
    log = wf.logger

    try:
        ast = parseAST(args)
    except ASTSyntaxError as e:
        log.debug('opps')
        wf.send_feedback()
        return

    wf.logger.debug(ast)
    target_time = arrow.now()

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

    # Add an item to Alfred feedback
    add_item(wf, str(int(time.mktime(target_time.datetime.timetuple()) * 1e3 + target_time.datetime.microsecond / 1e3)), 'timestamp')
    add_item(wf, target_time.humanize(), 'humanize')
    add_item(wf, target_time.format('YYYY-MM-DD HH:mm:ss ZZ'), 'YYYY-MM-DD HH:mm:ss ZZ')

    # Send output to Alfred
    wf.send_feedback()
