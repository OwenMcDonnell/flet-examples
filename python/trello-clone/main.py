from cmath import exp
import logging
import os
from itertools import islice
from turtle import update

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
    # board placeholder untethered to nav item
    Column([Text("Create a list!")],
           alignment="start", expand=True)
]


def main(page: Page):
    page.title = "Flet Trello clone"
    page.bgcolor = colors.LIGHT_GREEN_400
    currentBoardIndex: int = 0
    currentBoard = boards[currentBoardIndex]

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
        nonlocal currentBoardIndex  # needed to access nested function "global"
        nonlocal currentBoard
        currentBoardIndex = len(sidebar.destinations) - 1
        mainView.controls.remove(currentBoard)
        currentBoard = boards[currentBoardIndex]
        mainView.controls.append(currentBoard)
        sidebar.selected_index = currentBoardIndex
        print(currentBoardIndex)

    def addBoard(e):
        def close_dlg(e):
            createNewBoard(e)
            dialog.open = False
            page.update()
        dialog = AlertDialog(
            title=Text("Name your new board"),
            content=Column(
                [TextField(label="New Board Name", on_submit=close_dlg)], tight=True),
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
        page.dialog = dialog
        dialog.open = True
        page.update()

    def navRail_change(e):
        nonlocal currentBoardIndex
        nonlocal currentBoard
        currentBoardIndex = e.control.selected_index
        if currentBoard in mainView.controls:
            mainView.controls.remove(currentBoard)
        currentBoard = boards[e.control.selected_index]
        mainView.controls.append(currentBoard)
        print("Selected destination: ",
              e.control.selected_index)
        page.update()
        print("navRail_change called")

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
                ]
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

    mainView = Row(
        [
            sidebar,
            VerticalDivider(width=2),
            currentBoard
        ],
        expand=True
    )
    page.add(mainView)
    # page.add(Text("Sanity Check"))


flet.app(target=main)
