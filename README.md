# alfred-workflow-moment

Advanced time utility for Alfred 2/3 workflow. Inspired by [moment.js] and [alfred-datetime-format-converter].

[DOWNLOAD LINK]

## command

### `now` `m`

Get current timestamp and formatted time.

### `format-moment`

List all saved time formats, press `CMD+ENTER` to delete.

### `format-moment add <format string>`

Add a time format to storage, which can be used for `moment`.

### `moment [arg]...` `m [arg]...`

Calculate timestamp by arguments. There is servals calculate command:

#### `<timestamp>`: 

Init/reset time. both UNIX timestamp and timestamp with milliseconds are supported. For example: `moment 1455624282913` or `moment 1455624282`.

![moment 1455624282913](https://raw.githubusercontent.com/perfectworks/screenshots/master/moment1.png)

#### `<operator> <attribute>`
Shift time. *operator* is like `+1`, `-100`. *attribute* is like `year`, `month`, `day`. For example: `moment +1 day`.

![moment +1 day](https://raw.githubusercontent.com/perfectworks/screenshots/master/moment2.png)

#### `set <attribute> <number> `

Replace specified attribute. For example: `moment set hour 4 set tz -7`

![moment set hour 4 set tz -7](https://raw.githubusercontent.com/perfectworks/screenshots/master/moment3.png)

#### `start of <attribute>`

Get start of the time span which split by specified *attribute*. For example `moment start of year`.

![moment start of year](https://raw.githubusercontent.com/perfectworks/screenshots/master/moment4.png)

#### `end of <attribute>`

Get end of the time span which split by specified *attribute*. For example `moment end of year`.

![moment end of year](https://raw.githubusercontent.com/perfectworks/screenshots/master/moment5.png)

#### `format <format string>`

Format time by specified *format*. If there is no `format` command, moment will use saved format string to format time, or a default format. For example `moment format MMMM DD, YYYY`.

![moment format MMMM DD, YYYY](https://raw.githubusercontent.com/perfectworks/screenshots/master/moment7.png)

## Combine command

Combination of commands is acceptable. For example: `moment 1455626556616 start of minute set hour 4 set day 1 end of minute `.

![combination of commands](https://raw.githubusercontent.com/perfectworks/screenshots/master/moment6.png)

Please note that the `format` command will all rest arguments as format string, so `format` command should always be the last command.

## supported time attributes

| attribute     | alias           | value                                 |
|---------------|-----------------|---------------------------------------|
| year          | y               |                                       |
| month         | M               | 1 - 12                                |
| day           | d               | 1 - 31                                |
| hour          | h               | 0 - 23                                |
| minute        | m               | 0 - 59                                |
| second        | s               | 0 - 59                                |
| timezone      | tz              | -12 - +12 (number without plus is ok) |

## supported format token

Because python library [arrow] is chosen to deal with time, you can use the following tokens for formatting and parseing time:

|                                  | Token          | Output                                      |
| -------------------------------- | -------------- | ------------------------------------------- |
| **Year**                         | YYYY           | 2000, 2001, 2002 ... 2012, 2013             |
|                                  | YY             | 00, 01, 02 ... 12, 13                       |
| **Month**                        | MMMM           | January, February, March ...                |
|                                  | MMM            | Jan, Feb, Mar ...                           |
|                                  | MM             | 01, 02, 03 ... 11, 12                       |
|                                  | M              | 1, 2, 3 ... 11, 12                          |
| **Day of Year**                  | DDDD           | 001, 002, 003 ... 364, 365                  |
|                                  | DDD            | 1, 2, 3 ... 4, 5                            |
| **Day of Month**                 | DD             | 01, 02, 03 ... 30, 31                       |
|                                  | D              | 1, 2, 3 ... 30, 31                          |
|                                  | Do             | 1st, 2nd, 3rd ... 30th, 31st                |
| **Day of Week**                  | dddd           | Monday, Tuesday, Wednesday ...              |
|                                  | ddd            | Mon, Tue, Wed ...                           |
|                                  | d              | 1, 2, 3 ... 6, 7                            |
| **Hour**                         | HH             | 00, 01, 02 ... 23, 24                       |
|                                  | H              | 0, 1, 2 ... 23, 24                          |
|                                  | hh             | 01, 02, 03 ... 11, 12                       |
|                                  | h              | 1, 2, 3 ... 11, 12                          |
| **AM / PM**                      | A              | AM, PM, am, pm                              |
|                                  | a              | am, pm                                      |
| **Minute**                       | mm             | 00, 01, 02 ... 58, 59                       |
|                                  | m              | 0, 1, 2 ... 58, 59                          |
| **Second**                       | ss             | 00, 01, 02 ... 58, 59                       |
|                                  | s              | 0, 1, 2 ... 58, 59                          |
|                                  | SS             | 00, 01, 02 ... 98, 99                       |
|                                  | S              | 0, 1, 2 ... 8, 9                            |
| **Timezone**                     | Z              | +0800                                       |
|                                  | ZZ             | +08:00                                      |
| **Timestamp**                    | X              | 1381685817                                  |

## License

MIT

[alfred-datetime-format]: https://github.com/mwaterfall/alfred-datetime-format-converter
[moment.js]: http://momentjs.com
[DOWNLOAD LINK]: https://github.com/perfectworks/alfred-workflow-moment/releases
[arrow]: http://crsmithdev.com/arrow/#tokens
