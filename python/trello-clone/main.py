from cmath import exp
import logging
import os
from itertools import islice


import flet
from flet import (
    AlertDialog,
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
boardNav = [
    NavigationRailDestination(

        padding=padding.all(5),
        # label_content=Row(
        #     [Text("Empty Board")]
        # )
        label_content=Text("Empty Board"),
        selected_icon=icons.CHEVRON_RIGHT_ROUNDED
    )
]
boards = [
    Column([Text("Create a list!")],
           alignment="start", expand=True)
]


def main(page: Page):
    page.title = "Flet Trello clone"
    page.bgcolor = colors.LIGHT_GREEN_400
    currentBoardIndex: int = 0

    def search_board(e):
        "TODO"

    def createNewBoard(e):

        sidebar.destinations.append(
            NavigationRailDestination(

                padding=padding.all(5),
                # label_content=Row(
                #     [Text("Empty Board")]
                # )
                label_content=Text(e.control.value),
                label=e.control.value,
                selected_icon=icons.CHEVRON_RIGHT_ROUNDED
            )
        )

        boards.append(
            Column([Text("Welcome to your new board!")],
                   alignment="start", expand=True)
        )
        print(boards)
        currentBoardIndex = len(sidebar.destinations) - 1
        sidebar.selected_index = currentBoardIndex
        print(currentBoardIndex)
        page.update()

    def addBoard(e):
        def close_dlg(e):
            createNewBoard(e)
            dialog.open = False
            page.update()
        dialog = AlertDialog(
            title=Text("Name your new board"),
            content=Column(
                [TextField(label="New Board Name", on_submit=close_dlg)], tight=True),

            # actions=[
            #     TextButton("OK", on_click=close_dlg)
            # ],
            # actions_alignment="start",
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
        page.dialog = dialog
        dialog.open = True
        page.update()

    def navRail_change(e):
        currentBoardIndex = e.control.selected_index
        print("Selected destination: ",
              e.control.selected_index, currentBoardIndex)
        page.update()

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
        destinations=boardNav,
        bgcolor=colors.LIGHT_GREEN_700,
        leading=Container(
            content=Row(
                controls=[
                    TextButton("Add new board", icon=icons.ADD,
                               on_click=addBoard),
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
        on_change=navRail_change,
        selected_index=0,
        extended=True
    )

    page.add(
        Row(
            [
                sidebar,
                VerticalDivider(width=2),
                boards[currentBoardIndex]
            ],
            expand=True
        )
    )
    # page.add(Text("Sanity Check"))


flet.app(target=main)
