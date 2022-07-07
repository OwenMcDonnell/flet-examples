from cProfile import label
import flet
from flet import (
    Column,
    ElevatedButton,
    Radio,
    RadioGroup,
    Text,
    Row,
    Icon,
    colors,
    icons)


def main(page):

    # should try gridview instead
    rg = RadioGroup(content=Row([
        Radio(value="amber"),
        Radio(value="indigo"),
        Radio(value="teal")]))
    options = Column([
        rg,
        Row([
            Icon(name=icons.CIRCLE, color=colors.AMBER),
            Icon(name=icons.CIRCLE, color=colors.INDIGO),
            Icon(name=icons.CIRCLE, color=colors.TEAL)
        ], spacing=20)
    ])

    page.add(Text("Select a color for your list:"), options)


flet.app(target=main)
