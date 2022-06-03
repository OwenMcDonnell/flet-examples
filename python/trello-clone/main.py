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
    Divider,
    AppBar,
    PopupMenuButton,
    PopupMenuItem,
    TextField,
    alignment,
    border_radius,
    colors,
    icons,
    padding,
    margin,
    border
)

# trello app
# MVP  - Boards -> Lists -> Cards
# Views - Different views of boards (timeline, table, etc.)
cardLists = []
cardList = {}
boards = []


def main(page: Page):
    page.title = "Flet Trello clone"
    # page.theme_mode = "dark"
    page.bgcolor = colors.LIGHT_GREEN_400

    def search_board(e):
        "TODO"

    page.appbar = AppBar(
        leading=Icon(icons.GRID_GOLDENRATIO_ROUNDED),
        leading_width=100,
        title=Text("Trolli"),
        center_title=False,
        toolbar_height=75,
        bgcolor=colors.LIGHT_BLUE_ACCENT_700,
        actions=[
            Container(
                content=Row(
                    [
                        TextField(hint_text="Search this board", border="none",
                                  autofocus=False, on_submit=search_board, content_padding=padding.all(15), filled=False, suffix_icon=icons.SEARCH)
                    ],
                    alignment="spaceAround"
                ),
                bgcolor=colors.WHITE24,
                margin=margin.all(15),
                border=border.all(2, colors.WHITE),
                border_radius=border_radius.all(30)
            ),
            Container(
                content=PopupMenuButton(
                    items=[
                        PopupMenuItem(text="Profile"),
                        PopupMenuItem(),  # divider
                        PopupMenuItem(
                            text="Synchronize"
                        )
                    ]
                ),
                margin=margin.only(left=50, right=25)
            )
        ],
    )

    sidebar = NavigationRail(
        destinations=[
            NavigationRailDestination(

                padding=padding.all(5),
                # label_content=Row(
                #     [Text("Empty Board")]
                # )
                label_content=Text("Empty Board"),
                selected_icon=icons.CHEVRON_RIGHT_ROUNDED
            ),
            *boards
        ],
        bgcolor=colors.LIGHT_GREEN_700,
        leading=Container(
            content=Row(
                controls=[
                    TextButton("Add new board", icon=icons.ADD),
                    # Text("Add new board", text_align="center", weight="w500"),
                    # IconButton(icon=icons.ADD, icon_size=20)
                ],
                # alignment="spaceEvenly",
                # expand=True
            ),
            border_radius=border_radius.all(35),
            bgcolor=colors.WHITE12,
            padding=padding.all(0),
            margin=margin.all(0)
        ),
        selected_index=0,
        extended=True
    )

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
