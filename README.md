# alfred-workflow-moment

Advanced time utility for alfred 2 workflow. Inspired by [moment.js] and [alfred-datetime-format-converter].

## command

### `now`

Get current timestamp and formatted time.

### `moment [arg]...`

Calculate timestamp by arguments. There is servals calculate command:

#### `<timestamp>`: 

Init/reset time. both UNIX timestamp and timestamp with milliseconds are supported. For example: `moment 1455624282913` or `moment 1455624282`.

![moment 1455624282913](https://raw.githubusercontent.com/perfectworks/screenshots/master/moment1.png)

#### `<operator> <attribute>`
Shift time. *operator* is like `+1`, `-100`. *attribute* is like `year`, `month`, `day`. For example: `moment +1 day`.

![moment +1 day](https://raw.githubusercontent.com/perfectworks/screenshots/master/moment2.png)

#### `set <attribute> <number> `

Replace specified attribute. For example: `moment set hour 4`

![moment set hour 4](https://raw.githubusercontent.com/perfectworks/screenshots/master/moment3.png)

#### `start of <attribute>`

Get start of the time span which split by specified *attribute*. For example `moment start of year`.

![moment start of year](https://raw.githubusercontent.com/perfectworks/screenshots/master/moment4.png)

#### `end of <attribute>`

Get end of the time span which split by specified *attribute*. For example `moment end of year`.

![moment end of year](https://raw.githubusercontent.com/perfectworks/screenshots/master/moment5.png)

## Combine command

Combination of commands is acceptable. For example: `moment 1455626556616 start of minute set hour 4 set day 1 end of minute`.

![combination of commands](https://raw.githubusercontent.com/perfectworks/screenshots/master/moment6.png)

## supported time attributes

| attribute        | alias           |
| ------------- |:-------------:|
|year|y|
|month|M|
|day|d|
|hour|h|
|minute|m|
|second|s|


![time shift and replace](https://raw.githubusercontent.com/perfectworks/screenshots/master/moment2.png)
![mutiple time shift](https://raw.githubusercontent.com/perfectworks/screenshots/master/moment2.png)
![time ceil and floor](https://raw.githubusercontent.com/perfectworks/screenshots/master/moment2.png)

[alfred-datetime-format]: https://github.com/mwaterfall/alfred-datetime-format-converter
[moment.js]: http://momentjs.com
