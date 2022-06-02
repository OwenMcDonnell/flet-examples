from cmath import exp
import logging
import os
from itertools import islice
from turtle import bgcolor


import flet
from flet import (
    Column,
    Container,
    GridView,
    Icon,
    IconButton,
    Page,
    Row,
    SnackBar,
    Text,
    TextButton,
    IconButton,
    FloatingActionButton,
    NavigationRail,
    NavigationRailDestination,
    VerticalDivider,
    AppBar,
    PopupMenuButton,
    PopupMenuItem,
    TextField,
    alignment,
    border_radius,
    colors,
    icons,
    padding
)

# trello app
# MVP  - Boards -> Lists -> Cards
# Views - Different views of boards (timeline, table, etc.)
cardLists = []
cardList = {}
boards = []


def main(page: Page):
    page.title = "Flet Trello clone"
    page.theme_mode = "dark"
    page.bgcolor = colors.AMBER_800
    page.appbar = AppBar(
        leading=Icon(icons.PALETTE),
        leading_width=40,
        title=Text("AppBar Example"),
        center_title=False,
        bgcolor=colors.SURFACE_VARIANT,
        actions=[
            IconButton(icons.WB_SUNNY_OUTLINED),
            IconButton(icons.FILTER_3),
            PopupMenuButton(
                items=[
                    PopupMenuItem(text="Item 1"),
                    PopupMenuItem(),  # divider
                    PopupMenuItem(
                        text="Checked item", checked=False
                    ),
                ]
            ),
        ],
    )
    sidebar = NavigationRail(
        destinations=[
            NavigationRailDestination(

                padding=padding.all(5),
                label_content=Container(content=Text("1st Board"), bgcolor=colors.WHITE12,
                                        border_radius=border_radius.all(30), padding=5, expand=True)
            ),
            *boards
        ],
        bgcolor=colors.WHITE24,
        leading=Row(controls=[
            Text("Add new board", text_align="center", weight="w500"),
            IconButton(icon=icons.ADD, icon_size=20,
                       icon_color="blue")
        ]
        ),
        extended=True
    )
    # sidebar = Column(
    #     [
    #         Container(
    #             expand=True,
    #             content=Row(controls=[
    #                 Text("Add new board", text_align="center", weight="w500"),
    #                 IconButton(icon=icons.ADD, icon_size=20,
    #                            icon_color="blue")
    #             ]),
    #             bgcolor=colors.BLUE_GREY_300,
    #             padding=padding.all(5)
    #         )
    #     ],
    #     width=200,
    #     expand=True
    # )

    def addBoard():
        "TODO"

    page.add(
        Row(
            [
                sidebar,
                VerticalDivider(width=2),
                Column([Text("Create a list!")],
                       alignment="start", expand=True)
            ],
            expand=True
        )
    )
    # page.add(Text("Sanity Check"))


flet.app(target=main)
