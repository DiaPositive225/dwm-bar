#! /bin/python
from os import popen
from time import sleep
from Xlib.display import Display
from Xlib.Xatom import STRING
import volume
import date
import battery

class Bar:
    def __init__(self) -> None:

        self.display = Display()
        self.root = self.display.screen().root
        self.modules = [battery.get_str, volume.get_str, date.get_str]

    def set_bar(self, text : list[str], start_sep : str = "[", end_sep : str = "]", sep : str = "][") -> None:
        # popen(self.cmd + start_sep + sep.join(text) + end_sep + "'")
        to_be_displayed = start_sep + sep.join(text) + end_sep
        self.root.change_property(self.display.intern_atom('WM_NAME'), STRING, 8, to_be_displayed.encode('utf-8'))

    def update(self) -> None:
        self.set_bar([i() for i in self.modules], " < ", " > ", " >< ")


bar = Bar()
if __name__ == "__main__":
    while True:
        bar.update()
        sleep(1)
