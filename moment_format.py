#!/usr/bin/python
# encoding: utf-8

import arrow
import json

def process(wf, args):
    if len(args) == 0:
        list_format(wf)
    elif args[0] == 'add':
        if len(args) == 1:
            wf.add_item('For example: YYYY-MM-DD HH:mm:ss ZZ', subtitle = u'Press ⌘+C to copy document URL.', copytext = 'https://github.com/perfectworks/alfred-workflow-moment#supported-format-token')
        else:
            formatStr = ' '.join(args[1:])
            wf.add_item('Add format: "' + formatStr + '"', subtitle = 'For example: ' + arrow.now().format(formatStr), valid = True, arg = formatStr)
        wf.send_feedback()

def add_format(wf, args):
    formatStr = ' '.join(args)
    formats = load_format(wf)
    formats.append(formatStr)
    save_formats(wf, formats)

def del_format(wf, args):
    formats = load_format(wf)
    formatStr = ' '.join(args)
    formats.remove(formatStr)
    save_formats(wf, formats)

def load_format(wf):
    formats = wf.stored_data('formats')
    if formats is None:
        formats = []

    return formats

def save_formats(wf, formats):
    formats = list(set(formats))
    wf.store_data('formats', formats, serializer = 'json')

def list_format(wf):
    formats = load_format(wf)
    if len(formats) > 0:
        for formatStr in formats:
            value = arrow.now().format(formatStr)
            wf.add_item(formatStr, subtitle = u'For example: "' + value + u'", press ⌘ to delete.', valid = True, modifier_subtitles = {
                u'cmd': 'Delete format "' + formatStr + '"'
            }, arg = formatStr)
    else:
        wf.add_item('No saved format', subtitle = 'Use format-moment add <format string>" to add.', autocomplete = 'add ')
    wf.send_feedback()
