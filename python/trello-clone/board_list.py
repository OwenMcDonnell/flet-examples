from flet import (
    Column,
    Row,
    Switch,
    Checkbox,
    Text,
    FloatingActionButton,
    Container,
    TextButton,
    TextField,
    IconButton,
    Card,
    icons,
    border_radius,
    colors,
    padding,
    margin
)


class BoardList:
    def __init__(self, board, title: str, horizontal: bool = False, color: str = ""):
        self.board = board
        self.title = title
        self.editField = Row([
            TextField(label=self.title),
            TextButton(text="Save", on_click=self.save_title)
        ])
        self.cardInput = TextField(label="new card name", width=200)
        self.header = Row(
            # spacing=0,
            alignment="spaceBetween",
            controls=[
                Text(value=self.title, style="titleMedium"),
                IconButton(
                    icon=icons.CREATE_OUTLINED,
                    tooltip="Edit List Title",
                    on_click=self.edit_title,
                ),
                IconButton(
                    icons.DELETE_OUTLINE,
                    tooltip="Delete List",
                    on_click=self.delete_list,
                ),
            ],
        )
        self.cardList = (
            Column([self.cardInput, TextButton(
                "add card", icon=icons.ADD, on_click=self.addCard)]),
            Row([self.cardInput, TextButton(
                "add card", icon=icons.ADD, on_click=self.addCard)])
        )[horizontal]
        self.view = Column([
            self.header,
            Container(
                content=self.cardList,
                border_radius=border_radius.all(15),
                bgcolor=color if (color != "") else colors.BACKGROUND,
                padding=padding.all(20)
            )
        ])

    def addCard(self, e):
        self.board.boardListsHash[self.title][0].cardList.controls.append(
            Checkbox(label=self.cardInput.value, on_change=self.card_checked_H)
        )
        self.board.boardListsHash[self.title][1].cardList.controls.append(
            Checkbox(label=self.cardInput.value, on_change=self.card_checked_V)
        )
        self.cardInput.value = ""
        self.view.update()

    def card_checked_H(self, e):
        print("card_checked event: ", e.control)
        i = self.board.boardListsHash[self.title][0].cardList.controls.index(
            e.control)
        self.board.boardListsHash[self.title][1].cardList.controls[i].value = e.control.value
        pass

    def card_checked_V(self, e):
        print("card_checked event: ", e.control)
        i = self.board.boardListsHash[self.title][1].cardList.controls.index(
            e.control)
        self.board.boardListsHash[self.title][0].cardList.controls[i].value = e.control.value
        pass

    def edit_title(self, e):

        # self.header.controls[0] = self.editField
        # self.header.controls[1].visible = False
        # self.header.controls[2].visible = False

        # self.view.update()
        self.board.editListTitle(self)

    def save_title(self, e):
        # self.title = self.editField.controls[0].value
        # self.header.controls[0] = Text(
        #     value=self.title, style="titleMedium")
        # self.header.controls[1].visible = True
        # self.header.controls[2].visible = True
        # self.view.update()
        self.board.saveListTitle(self)

    def delete_list(self, e):
        self.board.removeList(self)
        # self.board.boardLists.remove(self)
        # self.board.boardListsView.controls.remove(self.view)
        # self.board.mainView.update()

    def buildList(self):
        return Container(
            content=Column(controls=self.cardList, expand=True),
            border_radius=border_radius.all(15),
            bgcolor=colors.WHITE24,
            padding=padding.all(20),
            margin=margin.all(10),
        )
