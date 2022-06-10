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
# import pprint
# pp = pprint.PrettyPrinter(indent=2, depth=10)


class Board:

    def __init__(self, page, app, identifier: str):
        self.page = page
        self.app = app
        self.identifier = identifier  # enforce uniqueness?
        self.switch = Switch(
            label="Horizontal/Veritcal List View", value=False, label_position="left", on_change=self.toggle_view)
        self.boardLists: list[BoardList] = [BoardList(self, "Empty List")]
        self.mainView = self.buildMainView(self.switch.value)
        # self.mainView = Column(
        #     controls=[
        #         Switch(label="Horizontal/Veritcal List View",
        #                value=False, label_position="left"),
        #         Row(
        #             controls=[
        #                 #THIS IS A BOARDLIST
        #                 Container(
        #                     content=Column([

        #                         Checkbox(label="first item"),
        #                         Checkbox(label="second item"),
        #                         Checkbox(label="Third item")

        #                     ], expand=True),
        #                     border_radius=border_radius.all(15),
        #                     bgcolor=colors.WHITE24,
        #                     padding=padding.all(20),
        #                     margin=margin.all(10),
        #                 ),
        #                 #THIS IS A BOARDLIST
        #                 FloatingActionButton(
        #                     icon=icons.ADD, text="add a list", height=30, on_click=self.addListDlg),
        #             ],

        #             # expand=True
        #         )
        #     ]
        # )

    def toggle_view(self, e):
        self.mainView = self.buildMainView(self.switch.value)
        self.app.update()

    def buildMainView(self, horizontal: bool):
        ctrls = []
        if horizontal:  # single column of boardList rows containing rows of cards
            for list in self.boardLists:
                ctrls.append(Row(controls=list.view, expand=True))
            print("ctrls: ", ctrls)
            view = Column(
                controls=ctrls,
                # expand=True
            )
        else:  # single row of boardList columns containing columns of cards
            for list in self.boardLists:
                ctrls.append(list.view)
            print("ctrls: ", ctrls)
            view = Row(
                controls=ctrls
            )

        view.controls.append(FloatingActionButton(
            icon=icons.ADD, text="add a list", height=30, on_click=self.addListDlg))
        print("view.controls: ", view.controls)
        print("view: ", view)
        return Column(
            controls=[
                self.switch,
                view
            ],
        )

    def addList(self, list: BoardList):
        self.boardLists.append(list)
        self.buildMainView(self.switch.value)
        self.app.update()

    def addListDlg(self, e):
        def close_dlg(e):
            print("in close_dlg", e.control.value)
            print("self.boardLists before: ", self.boardLists)
            boardList = BoardList(self, e.control.value)
            #print("boardList: ", boardList.view, boardList.view.content)
            self.boardLists.append(boardList)
            print("self.boardLists after: ", self.boardLists)
            print("self.mainView.controls[1] before: ",
                  self.mainView.controls[1].controls)
            self.mainView = self.buildMainView(self.switch.value)
            print("self.mainView.controls[1] after: ",
                  self.mainView.controls[1].controls)
            print("about to update")
            self.app.update()
            # self.mainView.update()
            # self.addList(boardList)
            dialog.open = False

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
