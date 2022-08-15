from flet import (
    UserControl,
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
    def __init__(self, board, title: str, horizontal: bool, color: str = ""):
        self.board = board
        self.horizontal = horizontal
        self.title = title
        self.color = color
        self.editField = Row([
            TextField(label=self.title),
            TextButton(text="Save", on_click=self.save_title)
        ])
        self.cardInput = TextField(label="new card name", width=200)

    def build(self):

        header = Row(

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

        hrztlCardList = Row([self.cardInput, TextButton(
            "add card", icon=icons.ADD, on_click=self.addCard)])

        vrtclCardList = Column([self.cardInput, TextButton(
            "add card", icon=icons.ADD, on_click=self.addCard)])
        list = Column([
            Row([self.cardInput, TextButton(
                "add card", icon=icons.ADD, on_click=self.addCard)], visible=(self.horizontal)),
            Column([self.cardInput, TextButton(
                "add card", icon=icons.ADD, on_click=self.addCard)], visible=(not self.horizontal))

        ])

        view = Column([
            header,
            Container(
                content=list,
                # border_radius=border_radius.all(15),
                bgcolor=self.color if (
                    self.color != "") else colors.BACKGROUND,
                padding=padding.all(20),
                # visible=self.horizontal
            ),
            # Container(
            #     content=self.vrtclCardList,
            #     # border_radius=border_radius.all(15),
            #     bgcolor=self.color if (
            #         self.color != "") else colors.BACKGROUND,
            #     padding=padding.all(20),
            #     visible=(not self.horizontal)
            # )

        ], data=self.title)

        return view

    def toggleView(self, switch):
        self.list.controls[0].visible = (bool(self.horizontal))
        self.list.controls[1].visible = (not bool(self.horizontal))
        self.horizontal = switch

    def setView(self):
        print("switch value: ", self.horizontal)
        if self.horizontal:
            #self.header.controls[0].value += "x"
            #self.view.controls[1].border_radius = border_radius.all(15)
            self.board.horizontalWrap.visible = True
            self.board.verticalWrap.visible = False
            self.list.controls[0].visible = (True)
            self.list.controls[1].visible = (False)
        else:
            #self.header.controls[0].value += "y"
            #self.view.controls[1].border_radius = border_radius.all(0)
            self.board.horizontalWrap.visible = False
            self.board.verticalWrap.visible = True
            self.list.controls[1].visible = (True)
            self.list.controls[0].visible = (False)
        self.update()
        # self.board.mainView.update()

    def addCard(self, e):
        self.hrztlCardList.controls.insert(
            -1,
            Checkbox(
                label=self.cardInput.value, on_change=self.card_checked_H)
        )

        self.vrtclCardList.controls.insert(
            -1,
            Checkbox(
                label=self.cardInput.value, on_change=self.card_checked_V)
        )
        print("self.hrztlCardList: ", self.hrztlCardList.controls)
        print("self.vrtclCardList: ", self.vrtclCardList.controls)
        # self.board.boardListsHash[self.title][0].cardList.controls.append(
        #     Checkbox(label=self.cardInput.value, on_change=self.card_checked_H)
        # )
        # self.board.boardListsHash[self.title][1].cardList.controls.append(
        #     Checkbox(label=self.cardInput.value, on_change=self.card_checked_V)
        # )

        self.cardInput.value = ""
        self.update()

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
        self.board.removeList(self, e)
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
