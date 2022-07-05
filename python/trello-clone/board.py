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
        self.switch = Switch(
            label="Horizontal/Veritcal List View", value=False, label_position="left", on_change=self.toggle_view)
        self.boardListsHorizontal: list[BoardList] = []
        self.boardListsVertical: list[BoardList] = []
        self.boardListHorizontal = Column(
            [
                FloatingActionButton(
                    icon=icons.ADD, text="add a list", height=30, on_click=self.addListDlg)
            ],
            # vertical_alignment="start",
            wrap=True,
            visible=False
        )
        self.boardListVertical = Row(
            [
                FloatingActionButton(
                    icon=icons.ADD, text="add a list", height=30, on_click=self.addListDlg)
            ],
            vertical_alignment="start",
            wrap=True,
            # width=self.app.page.window_width
        )
        # self.mainView = self.buildMainView(self.switch.value)
        self.mainView = Column(
            controls=[
                self.switch,
                self.boardListHorizontal,
                self.boardListVertical
            ])

    def toggle_view(self, e):

        self.boardListHorizontal.visible = e.control.value
        self.boardListVertical.visible = not e.control.value
        self.app.update()
        # self.mainView.update()

    def addList(self, list: BoardList):
        self.boardLists.append(list)
        # self.buildMainView(self.switch.value)
        self.app.update()

    def addListDlg(self, e):
        def close_dlg(e):
            boardListHorizontal = BoardList(self, e.control.value, True)
            boardListVertical = BoardList(self, e.control.value, False)
            # print("boardList: ", boardList.view, boardList.view.content)
            self.boardListsHorizontal.append(boardListHorizontal)
            self.boardListsVertical.append(boardListVertical)
            self.boardListHorizontal.controls.insert(
                len(self.boardListsHorizontal) - 1, boardListHorizontal.view)
            self.boardListVertical.controls.insert(
                len(self.boardListsVertical) - 1, boardListVertical.view)
            print("self.mainView.controls[1] before: ",
                  self.mainView.controls[1].controls)
            self.mainView.update()
            # self.mainView = self.buildMainView(self.switch.value)
            print("self.mainView.controls[1] after: ",
                  self.mainView.controls[1].controls)
            self.app.update()
            # self.mainView.update()
            # self.addList(boardList)
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
