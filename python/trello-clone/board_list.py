from flet import (
    Column,
    Row,
    Switch,
    Checkbox,
    Text,
    FloatingActionButton,
    Container,
    Card,
    icons,
    border_radius,
    colors,
    padding,
    margin
)


class BoardList:
    def __init__(self, board, title: str):
        self.board = board
        self.title = title
        self.cardList = [
            Checkbox(label="first item"),
            Checkbox(label="second item")
        ]
        #self.view = self.buildList()
        self.view = Container(
            content=Column(controls=self.cardList),
            border_radius=border_radius.all(15),
            bgcolor=colors.WHITE24,
            padding=padding.all(20),

            # margin=margin.all(10),
        )

        # Column(controls=[FloatingActionButton(
        #     icon=icons.ADD, text="add card", on_click=self.addCard)])

    def addCard(self, card):
        self.cardList.append(Checkbox(label=card))
        self.view = self.buildList()
        self.board.update()

    def buildList(self):
        return Container(
            content=Column(controls=self.cardList, expand=True),
            border_radius=border_radius.all(15),
            bgcolor=colors.WHITE24,
            padding=padding.all(20),
            margin=margin.all(10),
        )
        # return Column(
        # controls=[
        # Column(controls=[FloatingActionButton(
        #     icon=icons.ADD, text="add card", on_click=self.addCard)]),
        # Container(
        #     content=Column(
        #         controls=self.cardList),
        #     border_radius=border_radius.all(15),
        #     bgcolor=colors.WHITE24,
        #     padding=padding.all(20),
        #     margin=margin.all(10),
        # )
        # ],
        # expand=True
        # )
