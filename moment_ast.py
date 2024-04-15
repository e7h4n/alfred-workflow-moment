import arrow

class ASTSyntaxError(Exception):
    def __init__(self, args, errorIdx):
        self.args = args
        self.errorIdx = errorIdx

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_shift(s):
    if s[0] != '+' and s[0] != '-':
        return False
    return is_number(s[1:])

timeKeywords = {
    'timezone': 'timezone',
    'tz': 'timezone',

    'year': 'year',
    'years': 'year',
    'y': 'year',

    'month': 'month',
    'months': 'month',
    'M': 'month',

    'day': 'day',
    'days': 'day',
    'd': 'day',

    'hour': 'hour',
    'hours': 'hour',
    'h': 'hour',

    'minute': 'minute',
    'minutes': 'minute',
    'm': 'minute',

    'second': 'second',
    'seconds': 'second',
    's': 'second',

    'microsecond': 'microsecond',
    'microseconds': 'microsecond',
    'ms': 'microsecond'
}

def is_time_keywords(s):
    return s in timeKeywords

def syntax_error(args, idx):
    raise ASTSyntaxError(args, idx)

KEYWORD_SET = 'set'
KEYWORD_TO = 'to'
KEYWORD_START = 'start'
KEYWORD_OF = 'of'
KEYWORD_END = 'end'
KEYWORD_FORMAT = 'format'

STATUS_INIT = 0
STATUS_SHIFT = 1
STATUS_SET = 2
STATUS_SET_UNIT = 3
STATUS_START = 4
STATUS_END = 5
STATUS_OF = 6

def parse(args):
    ast = []
    status = STATUS_INIT
    for idx, query in enumerate(args):
        if is_shift(query):
            if status == STATUS_SET_UNIT:
                ast[-1].append(float(query))
                status = STATUS_INIT
                continue
            elif status != STATUS_INIT:
                syntax_error(args, idx)

            ast.append(['shift', float(query)])
            status = STATUS_SHIFT

        elif is_time_keywords(query):
            if status == STATUS_SHIFT:
                ast[-1].append(timeKeywords[query])
                status = STATUS_INIT
            elif status == STATUS_SET:
                ast[-1].append(timeKeywords[query])
                status = STATUS_SET_UNIT
            elif status == STATUS_OF:
                ast[-1].append(timeKeywords[query])
                status = STATUS_INIT
            else:
                syntax_error(args, idx)

        elif is_number(query):
            if status == STATUS_INIT:
                ast.append(['reset', float(query)])
            elif status == STATUS_SET_UNIT:
                ast[-1].append(float(query))
                status = STATUS_INIT

        elif query == KEYWORD_SET:
            if status != STATUS_INIT:
                syntax_error(args, idx)

            ast.append(['set'])
            status = STATUS_SET

        elif query == KEYWORD_START:
            ast.append(['start_of'])
            status = STATUS_START

        elif query == KEYWORD_END:
            ast.append(['end_of'])
            status = STATUS_END

        elif query == KEYWORD_OF:
            if status != STATUS_START and status != STATUS_END:
                syntax_error(args, idx)

            status = STATUS_OF

        elif query == KEYWORD_FORMAT:
            if status != STATUS_INIT:
                syntax_error(args, idx)

            ast.append(['format'] + args[idx + 1:])
            break

        else:
            syntax_error(args, idx)

    if status != STATUS_INIT:
        syntax_error(args, -1)

    return ast
