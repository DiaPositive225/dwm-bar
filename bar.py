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
        # set up to change WM_NAME
        self.display = Display()
        self.root = self.display.screen().root

        # modules, order of modules
        self.modules = {
            "battery": battery.get_str,
            "volume": volume.get_str,
            "date": date.get_str
        }
        self.order = ["battery", "volume", "date"]
        self.cache = ["" for _ in self.order]

        # starting "decorator", ending "decorator, separator
        self.style = (" < ", " > ", " >< ")

    def set_bar(self, text : list[str], start_sep : str = "[", end_sep : str = "]", sep : str = "][") -> None:
        to_be_displayed = start_sep + sep.join(text) + end_sep
        self.root.change_property(self.display.intern_atom('WM_NAME'), STRING, 8, to_be_displayed.encode('utf-8'))

    # basically, update all modules
    def populate(self) -> None:
        self.cache = [self.modules[i]() for i in self.order]
        self.set_bar(self.cache, *self.style)

    def update(self, module : str) -> None:
        index = self.order.index(module)
        self.cache[index] = self.modules[module]()
        self.set_bar(self.cache, *self.style)


bar = Bar()
if __name__ == "__main__":
    while True:
        bar.populate()
        sleep(1)
