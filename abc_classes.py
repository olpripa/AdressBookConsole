from abc import ABC, abstractmethod
from classes import Record


class Interface_AB(ABC):
    def __init__(self, strtoprint: str):
        self.record = strtoprint

    @abstractmethod
    def get_summary(self):
        pass


class CLI_interface(Interface_AB):
    def get_summary(self):
        print(self.record)


class GUI_interface(Interface_AB):
    def get_summary(self):
        ...
