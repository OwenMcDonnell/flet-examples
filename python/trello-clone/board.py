from flet import (
    Column,
    Row,
    FloatingActionButton,
    Text,
    Checkbox,
    Switch,
    Container,
    TextField,
    AlertDialog,
    Container,
    Switch,
    Page,
    icons,
    border_radius,
    colors,
    padding,
    margin
)
from board_list import BoardList


class Board:
    def __init__(self, app, identifier: str):
        self.app = app
        self.identifier = identifier  # enforce uniqueness?
        self.boardListsHash = {}

        self.switch = Switch(
            label="Horizontal/Veritcal List View", value=False, label_position="left", on_change=self.toggle_view)
        self.boardListsHorizontal = Column(
            [
                FloatingActionButton(
                    icon=icons.ADD, text="add a list", height=30, on_click=self.addListDlg)
            ],
            # vertical_alignment="start",
            wrap=True,
            visible=False
        )
        self.boardListsVertical = Row(
            [
                FloatingActionButton(
                    icon=icons.ADD, text="add a list", height=30, on_click=self.addListDlg)
            ],
            vertical_alignment="start",
            wrap=True,
            # width=self.app.page.window_width
        )

        self.mainView = Column(
            controls=[
                self.switch,
                self.boardListsHorizontal,
                self.boardListsVertical
            ])

    def toggle_view(self, e):
        self.boardListsHorizontal.visible = e.control.value
        self.boardListsVertical.visible = not e.control.value
        for l in self.boardListsHash.values():
            l[0].visible = e.control.value
            l[1].visible = not e.control.value
        self.app.update()
        # self.mainView.update()

    def addList(self, list: BoardList):
        self.boardLists.append(list)
        # self.buildMainView(self.switch.value)
        self.app.update()

    def addListDlg(self, e):

        def close_dlg(e):
            if (e.control.value in self.boardListsHash):
                print("duplicate list")
                return
            newListHorizontal = BoardList(self, e.control.value, True)
            newListVertical = BoardList(self, e.control.value, False)
            self.boardListsHash[e.control.value] = (
                newListHorizontal, newListVertical)
            print("self.boardListsHash: ", self.boardListsHash)

            self.boardListsHorizontal.controls.insert(
                len(self.boardListsHash) - 1, newListHorizontal.view)
            self.boardListsVertical.controls.insert(
                len(self.boardListsHash) - 1, newListVertical.view)

            self.mainView.update()

            self.app.update()
            dialog.open = False

            self.app.page.update()

        dialog = AlertDialog(
            title=Text("Name your new list"),
            content=Column(
                [TextField(label="New List Name", on_submit=close_dlg)], tight=True),
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
        self.app.page.dialog = dialog
        dialog.open = True
        self.app.page.update()

    def removeList(self, list: BoardList):
        self.boardList.remove(list)

    def moveBoard(self, list: BoardList, displacement: int):
        i = self.boardList.index(list)
        listToMove = self.boardList.pop(i)
        self.boardList.insert(i + displacement, list)

    def createBoardNavDestination(self):
        pass

    # BOARDLIST
    #     Container(
    #         content=Column([

    #             Checkbox(label="first item"),
    #             Checkbox(label="second item"),
    #             Checkbox(label="Third item")

    #         ], expand=True),
    #         border_radius=border_radius.all(15),
    #         bgcolor=colors.WHITE24,
    #         padding=padding.all(20),
    #         margin=margin.all(10),
    #     ),
    # BOARDLIST
