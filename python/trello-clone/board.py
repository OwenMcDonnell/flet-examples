from board_list import BoardList
from flet import (
    Column,
    Row,
    FloatingActionButton,
    Text,
    TextField,
    AlertDialog,
    Container,
    Switch,
    icons
)


class Board:

    def __init__(self, page, identifier: str):
        self.page = page
        self.identifier = identifier  # enforce uniqueness?
        self.switch = Switch(
            label="Horizontal/Veritcal List View", value=False, label_position="left", on_change=self.toggle_view)
        self.boardLists: list[BoardList] = [

        ]
        self.mainView = self.buildMainView(self.switch.value)

    def toggle_view(self, e):
        self.mainView = self.buildMainView(self.switch.value)

    def buildMainView(self, horizontal: bool):
        ctrls = []
        if horizontal:  # single column of boardList rows containing rows of cards
            for list in self.boardLists:
                ctrls.append(Row(controls=list.view, expand=True))
            print("ctrls: ", ctrls)
            view = Column(
                controls=ctrls,
                expand=True
            )
        else:  # single row of boardList columns containing columns of cards
            for list in self.boardLists:
                ctrls.append(Column(
                    controls=list.view, expand=True))
            print("ctrls: ", ctrls)
            view = Row(
                controls=ctrls,
                expand=True
            )

        view.controls.append(FloatingActionButton(
            icon=icons.ADD, text="add a list", on_click=self.addListDlg))
        return Column(
            controls=[
                self.switch,
                view
            ],
            expand=True,
            tight=True
        )

    def addList(self, list: BoardList):
        self.boardList.append(list)
        self.buildMainView(self.switch.value)
        self.page.update()

    def addListDlg(self, e):
        def close_dlg(e):
            print("in close_dlg")
            boardList = BoardList(self.page, e.control.value)
            self.addList(boardList)
            dialog.open = False
            self.page.update()
        dialog = AlertDialog(
            title=Text("Name your new list"),
            content=Column(
                [TextField(label="New List Name", on_submit=close_dlg)], tight=True),
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()

    def removeList(self, list: BoardList):
        self.boardList.remove(list)

    def moveBoard(self, list: BoardList, displacement: int):
        i = self.boardList.index(list)
        listToMove = self.boardList.pop(i)
        self.boardList.insert(i + displacement, list)

    def createBoardNavDestination(self):
        pass
