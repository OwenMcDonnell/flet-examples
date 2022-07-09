from cProfile import label
import flet
from flet import (
    Column,
    ElevatedButton,
    Radio,
    RadioGroup,
    GridView,
    Text,
    Row,
    Icon,
    colors,
    icons)


def main(page):
    colorIcons = GridView(
        expand=1,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )
    # should try gridview instead
    rg = RadioGroup(content=Row([
        Radio(value="amber"),
        Radio(value="indigo"),
        Radio(value="teal")]))
    # options = Column([
    #     rg,
    #     Row([
    #         Icon(name=icons.CIRCLE, color=colors.AMBER),
    #         Icon(name=icons.CIRCLE, color=colors.INDIGO),
    #         Icon(name=icons.CIRCLE, color=colors.TEAL)
    #     ], spacing=20)
    # ])
    options = GridView(controls=[
        rg.content.controls[0],
        rg.content.controls[1],
        rg.content.controls[2],
        Icon(name=icons.CIRCLE, color=colors.AMBER),
        Icon(name=icons.CIRCLE, color=colors.INDIGO),
        Icon(name=icons.CIRCLE, color=colors.TEAL)

    ],
        expand=1,
        runs_count=3,
        max_extent=50,
        child_aspect_ratio=2.0,
        spacing=50,
        run_spacing=20
    )

    page.add(Text("Select a color for your list:"), options)


flet.app(target=main)
