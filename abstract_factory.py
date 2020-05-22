from abc import ABC, abstractmethod
import random


class GuiFactory(ABC):
    """
        Interface for abstract factory. Concrete factories should implement all methods
    """

    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


class WinGui(GuiFactory):
    def create_button(self):
        return WinButton()

    def create_checkbox(self):
        return WinCheckbox()


class MacGui(GuiFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()


class Button(ABC):
    """
        Interface for Product_1 (Button)
    """
    @abstractmethod
    def click(self):
        pass


class WinButton(Button):
    def click(self):
        print('I am a windows button')


class MacButton(Button):
    def click(self):
        print('I am a mac button')


class Checkbox(ABC):
    """
        Interface for Product_2 (Checkbox)
    """

    @abstractmethod
    def select(self):
        pass


class WinCheckbox(Checkbox):
    def select(self):
        print('I am a windows checkbox')


class MacCheckbox(Checkbox):
    def select(self):
        print('I am a mac checkbox')


def client_code(gui: GuiFactory):
    print(f'Working Gui (factory) is {type(gui).__name__}')

    button = gui.create_button()
    checkbox = gui.create_checkbox()

    button.click()
    checkbox.select()


if __name__ == '__main__':
    if random.random() < 0.5:
        client_code(MacGui())
    else:
        client_code(WinGui())
