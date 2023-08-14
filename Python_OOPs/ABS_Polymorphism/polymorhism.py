from abc import ABC, abstractmethod


class UIControl(ABC):

    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("Textbox")


class DropdownList(UIControl):
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropdownList()
print(isinstance(ddl, UIControl))
print(isinstance(ddl, DropdownList))
# draw(ddl)

textbox = TextBox()
# draw(textbox)
draw([ddl, textbox])
