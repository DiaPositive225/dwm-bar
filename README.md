# simple dwm bar written in python
This project is the author's dwm status bar, it is not designed for general, plug and play use but feel free to use, modify and in general implement however you wish.


## dependencies
As things stand dependencies are
- x11
- python3
- psutils (python library)
- wpctl

## use
As it stands, it shows battery level, volume level of the default audio sink, date and time. New modules are easily added by writing a python function that outputs the string you want as module and adding it to the `self.modules` list in the `Bar` definition in [bar.py].

To use it you will need to start it at the start of your session, either .dwm/autostart.sh or .xinitrc or any method you prefer, I cannot guarantee it working with all these options but if you use a bash script like autostart.sh don't forget to parallelize the process, especially if you start other commands after it.

The script works by changing the `WM_NAME` property of the root window which means this could theoretically also be used for other x11 based window managers such as i3 etc.

## disclaimer
I can not stress enough how not designed for general use this is.
