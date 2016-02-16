# alfred-workflow-moment

Alfred 2 workflow for process timestamp. Inspired by [alfred-datetime-format-converter] and [moment.js].

## command

### `now`

Get current timestamp and formatted time.

### `moment [arg]...`

Calculate timestamp by arguments. There is servals calculate command:

* `<timestamp>`: Reset time, both UNIX timestamp and timestamp with milliseconds are supported. For example: `moment 1455624282913` or `moment 1455624282`.
* `<operator> <attribute>`: Time shift. *operator* is like `+1`, `-100`. *attribute* is like `year`, `month`, `day`. For example: `moment +1 day`.
* `set <attribute> <number> `: Replace specified attribute. For example: `moment set hour 4`
* `start of <attribute>`: Get start of the time span which split by specified *attribute*. For example `moment start of year`.
* `end of <attribute>`: Get end of the time span which split by specified *attribute*. For example `moment end of year`.

## supported time attributes

![format timestamp](https://raw.githubusercontent.com/perfectworks/screenshots/master/moment1.png)
![time shift and replace](https://raw.githubusercontent.com/perfectworks/screenshots/master/moment2.png)
![mutiple time shift](https://raw.githubusercontent.com/perfectworks/screenshots/master/moment2.png)
![time ceil and floor](https://raw.githubusercontent.com/perfectworks/screenshots/master/moment2.png)

* [alfred-datetime-format](https://github.com/mwaterfall/alfred-datetime-format-converter)
* [moment.js](http://momentjs.com)

